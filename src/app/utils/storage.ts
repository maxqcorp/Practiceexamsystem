// Storage utility for persisting exam progress
// Falls back to localStorage if Supabase is unavailable or user is not logged in
import { supabase } from './supabase/client';

const LOCAL_STORAGE_KEY = 'practice-exam-progress';

export interface ExamProgress {
  [examSetId: number]: {
    [questionId: number]: number; // questionId -> selected answer index
  };
}

export interface ExamStats {
  attempted: number;
  correct: number;
  total: number;
}

async function getCurrentUserId(): Promise<string | null> {
  const { data: { session } } = await supabase.auth.getSession();
  return session?.user?.id || null;
}

// Load from localStorage
function loadLocalProgress(): ExamProgress {
  try {
    const raw = localStorage.getItem(LOCAL_STORAGE_KEY);
    if (raw) {
      return JSON.parse(raw) as ExamProgress;
    }
  } catch (e) {
    console.error('Error loading local progress:', e);
  }
  return {};
}

// Save to localStorage
function saveLocalProgress(progress: ExamProgress): void {
  try {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {
    console.error('Error saving local progress:', e);
  }
}

export async function loadProgress(): Promise<ExamProgress> {
  // Always load from localStorage first (fast, works offline)
  const localProgress = loadLocalProgress();

  try {
    const userId = await getCurrentUserId();
    if (!userId) {
      // Not logged in: return localStorage only
      return localProgress;
    }

    // Try to load from Supabase
    const { data, error } = await supabase
      .from('kv_store_b9034bdd')
      .select('value')
      .eq('key', `progress-${userId}`)
      .maybeSingle();

    if (error) {
      console.error('Error loading progress from Supabase:', error);
      // Fall back to localStorage
      return localProgress;
    }

    const cloudProgress = data?.value || {};

    // Merge: prefer localStorage if it has more data (user answered more questions locally)
    // This handles the case where user answered questions while offline
    const mergedProgress: ExamProgress = { ...cloudProgress };
    for (const examSetId in localProgress) {
      const localSet = localProgress[examSetId];
      const cloudSet = cloudProgress[examSetId] || {};
      const mergedSet = { ...cloudSet, ...localSet };
      mergedProgress[Number(examSetId)] = mergedSet;
    }

    // If local had extra data, sync back to cloud
    const localKeys = Object.keys(localProgress);
    const cloudKeys = Object.keys(cloudProgress);
    const needsSync = localKeys.some(
      (key) => Object.keys(localProgress[Number(key)]).length > Object.keys(cloudProgress[Number(key)] || {}).length
    );

    if (needsSync) {
      // Don't await - let it happen in background
      saveProgressToCloud(mergedProgress).catch(console.error);
    }

    return mergedProgress;
  } catch (error) {
    console.error('Error loading progress from database:', error);
    return localProgress;
  }
}

// Save to Supabase only (background sync)
async function saveProgressToCloud(progress: ExamProgress): Promise<void> {
  const userId = await getCurrentUserId();
  if (!userId) return;

  const { error } = await supabase
    .from('kv_store_b9034bdd')
    .upsert(
      {
        key: `progress-${userId}`,
        value: progress,
      },
      { onConflict: 'key' }
    );

  if (error) {
    console.error('Error saving progress to cloud:', error);
  }
}

export async function saveProgress(progress: ExamProgress): Promise<void> {
  // Always save to localStorage first (fast, reliable)
  saveLocalProgress(progress);

  // Then try to sync to Supabase in background
  try {
    await saveProgressToCloud(progress);
  } catch (error) {
    console.error('Error syncing progress to cloud:', error);
    // Local storage already saved, so progress is not lost
  }
}

export async function getExamSetProgress(examSetId: number): Promise<Map<number, number>> {
  const allProgress = await loadProgress();
  const examProgress = allProgress[examSetId] || {};
  return new Map(Object.entries(examProgress).map(([k, v]) => [parseInt(k), v]));
}

export async function saveExamSetProgress(examSetId: number, answers: Map<number, number>): Promise<void> {
  const allProgress = await loadProgress();
  allProgress[examSetId] = Object.fromEntries(answers);
  await saveProgress(allProgress);
}

// Debounced version to prevent rapid-fire saves
const pendingSaves = new Map<number, ReturnType<typeof setTimeout>>();

export function saveExamSetProgressDebounced(examSetId: number, answers: Map<number, number>, delay = 300): Promise<void> {
  return new Promise((resolve) => {
    const existingTimeout = pendingSaves.get(examSetId);
    if (existingTimeout) {
      clearTimeout(existingTimeout);
    }

    const timeoutId = setTimeout(async () => {
      await saveExamSetProgress(examSetId, answers);
      pendingSaves.delete(examSetId);
      resolve();
    }, delay);

    pendingSaves.set(examSetId, timeoutId);
  });
}

export async function clearExamSetProgress(examSetId: number): Promise<void> {
  const allProgress = await loadProgress();
  delete allProgress[examSetId];
  await saveProgress(allProgress);
}

export async function getAttemptedCount(examSetId: number): Promise<number> {
  const examProgress = await getExamSetProgress(examSetId);
  return examProgress.size;
}

export async function getExamStats(examSetId: number, questions: Array<{ id: number; correctAnswer: number }>): Promise<ExamStats> {
  const examProgress = await getExamSetProgress(examSetId);
  const attempted = examProgress.size;

  let correct = 0;
  examProgress.forEach((selectedAnswer, questionId) => {
    const question = questions.find(q => q.id === questionId);
    if (question && question.correctAnswer === selectedAnswer) {
      correct++;
    }
  });

  return {
    attempted,
    correct,
    total: questions.length
  };
}