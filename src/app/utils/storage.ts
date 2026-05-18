// Storage utility for persisting exam progress
// Uses a normalized relational table (user_progress) instead of JSON blobs.
// Falls back to localStorage if Supabase is unavailable or user is not logged in.
import { supabase } from './supabase/client';

const LOCAL_STORAGE_KEY = 'practice-exam-progress';
const PENDING_CLOUD_SYNC_KEY = 'practice-exam-pending-sync';

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

// --------------------------------------------------------------------------
// Exam-set ID helpers
// Components pass offset IDs to avoid collisions. We decode them into a clean
// (source, set_id) pair for the relational table.
// --------------------------------------------------------------------------
function decodeExamSetId(examSetId: number): { source: string; setId: number } {
  if (examSetId >= 3000) return { source: 'davidyt', setId: examSetId - 3000 };
  if (examSetId >= 2000) return { source: 'ramd',    setId: examSetId - 2000 };
  if (examSetId >= 1000) return { source: 'quick25', setId: examSetId - 1000 };
  return { source: 'main50', setId: examSetId };
}

function encodeExamSetId(source: string, setId: number): number {
  if (source === 'davidyt') return setId + 3000;
  if (source === 'ramd')    return setId + 2000;
  if (source === 'quick25') return setId + 1000;
  return setId; // main50
}

// --------------------------------------------------------------------------
// Auth helper
// --------------------------------------------------------------------------
async function getCurrentUserId(): Promise<string | null> {
  const { data: { session } } = await supabase.auth.getSession();
  return session?.user?.id || null;
}

// --------------------------------------------------------------------------
// localStorage cache (offline-first)
// --------------------------------------------------------------------------
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

function saveLocalProgress(progress: ExamProgress): void {
  try {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {
    console.error('Error saving local progress:', e);
  }
}

function saveLocalProgressForSet(examSetId: number, answers: Map<number, number>): void {
  const allProgress = loadLocalProgress();
  allProgress[examSetId] = Object.fromEntries(answers);
  saveLocalProgress(allProgress);
}

// --------------------------------------------------------------------------
// Legacy KV-store helpers (for one-time migration)
// --------------------------------------------------------------------------
async function loadProgressFromKVStore(userId: string, localProgress: ExamProgress): Promise<ExamProgress> {
  const { data, error } = await supabase
    .from('kv_store_b9034bdd')
    .select('value')
    .eq('key', `progress-${userId}`)
    .maybeSingle();

  if (error) {
    console.error('Error loading progress from legacy KV store:', error);
    return localProgress;
  }

  const cloudProgress = (data?.value as ExamProgress) || {};

  // Merge: local wins (offline-first)
  const mergedProgress: ExamProgress = { ...cloudProgress };
  for (const examSetId in localProgress) {
    const localSet = localProgress[examSetId];
    const cloudSet = cloudProgress[Number(examSetId)] || {};
    mergedProgress[Number(examSetId)] = { ...cloudSet, ...localSet };
  }

  return mergedProgress;
}

async function migrateOldProgressToNewTable(userId: string, progress: ExamProgress): Promise<void> {
  try {
    const rows: Array<{
      user_id: string;
      exam_source: string;
      exam_set_id: number;
      question_id: number;
      selected_answer: number;
    }> = [];

    for (const examSetIdStr in progress) {
      const examSetId = Number(examSetIdStr);
      const { source, setId } = decodeExamSetId(examSetId);
      const questions = progress[examSetId];
      for (const questionIdStr in questions) {
        rows.push({
          user_id: userId,
          exam_source: source,
          exam_set_id: setId,
          question_id: Number(questionIdStr),
          selected_answer: questions[questionIdStr],
        });
      }
    }

    if (rows.length > 0) {
      const { error } = await supabase
        .from('user_progress')
        .upsert(rows, { onConflict: 'user_id, exam_source, exam_set_id, question_id' });

      if (error) {
        console.error('Error migrating old progress to new table:', error);
      } else {
        console.log(`Migrated ${rows.length} answers from KV store to user_progress`);
      }
    }
  } catch (error) {
    console.error('Error during migration:', error);
  }
}

// --------------------------------------------------------------------------
// Load progress (relational table with KV fallback + auto-migration)
// --------------------------------------------------------------------------
export async function loadProgress(): Promise<ExamProgress> {
  const localProgress = loadLocalProgress();

  try {
    const userId = await getCurrentUserId();
    if (!userId) {
      return localProgress;
    }

    // Query the new normalized table
    const { data: rows, error } = await supabase
      .from('user_progress')
      .select('exam_source, exam_set_id, question_id, selected_answer')
      .eq('user_id', userId);

    if (error) {
      console.error('Error loading progress from user_progress:', error);
      return loadProgressFromKVStore(userId, localProgress);
    }

    const cloudProgress: ExamProgress = {};
    for (const row of rows || []) {
      const examSetId = encodeExamSetId(row.exam_source, row.exam_set_id);
      if (!cloudProgress[examSetId]) {
        cloudProgress[examSetId] = {};
      }
      cloudProgress[examSetId][row.question_id] = row.selected_answer;
    }

    // If nothing in the new table yet, check the legacy KV store and migrate
    if (Object.keys(cloudProgress).length === 0) {
      const oldProgress = await loadProgressFromKVStore(userId, localProgress);
      if (Object.keys(oldProgress).length > 0) {
        await migrateOldProgressToNewTable(userId, oldProgress);
      }
      return oldProgress;
    }

    // Merge: local wins (offline-first)
    const mergedProgress: ExamProgress = { ...cloudProgress };
    for (const examSetId in localProgress) {
      const localSet = localProgress[examSetId];
      const cloudSet = cloudProgress[Number(examSetId)] || {};
      mergedProgress[Number(examSetId)] = { ...cloudSet, ...localSet };
    }

    // If local has extra data, sync back to cloud in the background
    const needsSync = Object.keys(localProgress).some(
      (key) => Object.keys(localProgress[Number(key)]).length > Object.keys(cloudProgress[Number(key)] || {}).length
    );

    if (needsSync) {
      saveProgressToCloud(mergedProgress).catch(console.error);
    }

    return mergedProgress;
  } catch (error) {
    console.error('Error loading progress from database:', error);
    return localProgress;
  }
}

// --------------------------------------------------------------------------
// Save to Supabase relational table
// --------------------------------------------------------------------------
async function saveProgressToCloud(progress: ExamProgress): Promise<void> {
  const userId = await getCurrentUserId();
  if (!userId) return;

  const rows: Array<{
    user_id: string;
    exam_source: string;
    exam_set_id: number;
    question_id: number;
    selected_answer: number;
  }> = [];

  for (const examSetIdStr in progress) {
    const examSetId = Number(examSetIdStr);
    const { source, setId } = decodeExamSetId(examSetId);
    const questions = progress[examSetId];
    for (const questionIdStr in questions) {
      rows.push({
        user_id: userId,
        exam_source: source,
        exam_set_id: setId,
        question_id: Number(questionIdStr),
        selected_answer: questions[questionIdStr],
      });
    }
  }

  if (rows.length > 0) {
    const { error } = await supabase
      .from('user_progress')
      .upsert(rows, { onConflict: 'user_id, exam_source, exam_set_id, question_id' });

    if (error) {
      console.error('Error saving progress to cloud:', error);
      throw error;
    }
  }

  // Clear pending sync flag on success
  try {
    localStorage.removeItem(PENDING_CLOUD_SYNC_KEY);
  } catch (e) {
    // ignore
  }
}

// --------------------------------------------------------------------------
// Public save API
// --------------------------------------------------------------------------
export async function saveProgress(progress: ExamProgress): Promise<void> {
  saveLocalProgress(progress);

  try {
    await saveProgressToCloud(progress);
  } catch (error) {
    console.error('Error syncing progress to cloud:', error);
    try {
      localStorage.setItem(PENDING_CLOUD_SYNC_KEY, Date.now().toString());
    } catch (e) {
      // ignore
    }
  }
}

// Force immediate sync to cloud (call before logout)
export async function forceSyncProgress(): Promise<boolean> {
  flushPendingCloudSaves();

  const localProgress = loadLocalProgress();
  if (Object.keys(localProgress).length === 0) return true;

  try {
    await saveProgressToCloud(localProgress);
    return true;
  } catch (error) {
    console.error('Force sync failed:', error);
    return false;
  }
}

// --------------------------------------------------------------------------
// Per-exam-set helpers
// --------------------------------------------------------------------------
export async function getExamSetProgress(examSetId: number): Promise<Map<number, number>> {
  // Always start with local data (fast + offline support)
  const localProgress = loadLocalProgress();
  const localSet = localProgress[examSetId] || {};
  const result = new Map<number, number>(Object.entries(localSet).map(([k, v]) => [parseInt(k), v]));

  try {
    const userId = await getCurrentUserId();
    if (!userId) {
      return result;
    }

    const { source, setId } = decodeExamSetId(examSetId);
    const { data: rows, error } = await supabase
      .from('user_progress')
      .select('question_id, selected_answer')
      .eq('user_id', userId)
      .eq('exam_source', source)
      .eq('exam_set_id', setId);

    if (error) {
      console.error('Error loading exam set progress:', error);
      // Fall back to legacy KV load via loadProgress (which handles migration)
      const allProgress = await loadProgress();
      const examProgress = allProgress[examSetId] || {};
      return new Map(Object.entries(examProgress).map(([k, v]) => [parseInt(k), v]));
    }

    // Merge DB rows on top of local (local wins for offline-first)
    for (const row of rows || []) {
      // Only add from DB if local doesn't already have this question
      if (!result.has(row.question_id)) {
        result.set(row.question_id, row.selected_answer);
      }
    }

    return result;
  } catch (error) {
    console.error('Error loading exam set progress:', error);
    return result;
  }
}

export async function saveExamSetProgress(examSetId: number, answers: Map<number, number>): Promise<void> {
  saveLocalProgressForSet(examSetId, answers);
  await saveProgress(loadLocalProgress());
}

// Debounce only the cloud sync. Local writes happen immediately.
const pendingCloudSaves = new Map<number, ReturnType<typeof setTimeout>>();

export function saveExamSetProgressDebounced(examSetId: number, answers: Map<number, number>, delay = 300): Promise<void> {
  // Synchronous local write — guarantees persistence even if cloud sync is pending
  saveLocalProgressForSet(examSetId, answers);

  return new Promise((resolve) => {
    const existingTimeout = pendingCloudSaves.get(examSetId);
    if (existingTimeout) {
      clearTimeout(existingTimeout);
    }

    const timeoutId = setTimeout(async () => {
      pendingCloudSaves.delete(examSetId);
      try {
        await saveProgressToCloud(loadLocalProgress());
      } catch (error) {
        console.error('Error syncing progress to cloud:', error);
        try {
          localStorage.setItem(PENDING_CLOUD_SYNC_KEY, Date.now().toString());
        } catch (e) {
          // ignore
        }
      }
      resolve();
    }, delay);

    pendingCloudSaves.set(examSetId, timeoutId);
  });
}

function flushPendingCloudSaves(): void {
  for (const timeoutId of pendingCloudSaves.values()) {
    clearTimeout(timeoutId);
  }
  pendingCloudSaves.clear();
}

export async function clearExamSetProgress(examSetId: number): Promise<void> {
  // Clear localStorage immediately
  const allProgress = loadLocalProgress();
  delete allProgress[examSetId];
  saveLocalProgress(allProgress);

  // Clear from cloud
  try {
    const userId = await getCurrentUserId();
    if (!userId) return;

    const { source, setId } = decodeExamSetId(examSetId);
    const { error } = await supabase
      .from('user_progress')
      .delete()
      .eq('user_id', userId)
      .eq('exam_source', source)
      .eq('exam_set_id', setId);

    if (error) {
      console.error('Error clearing cloud progress:', error);
    }
  } catch (error) {
    console.error('Error clearing exam set progress:', error);
  }
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
