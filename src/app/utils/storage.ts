// Storage utility for persisting exam progress
import { supabase } from './supabase/client';

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

export async function loadProgress(): Promise<ExamProgress> {
  try {
    const userId = await getCurrentUserId();
    if (!userId) {
      return {};
    }

    const { data, error } = await supabase
      .from('kv_store_b9034bdd')
      .select('value')
      .eq('key', `progress-${userId}`)
      .maybeSingle();

    if (error) {
      console.error('Error loading progress:', error);
      return {};
    }

    return data?.value || {};
  } catch (error) {
    console.error('Error loading progress from database:', error);
    return {};
  }
}

export async function saveProgress(progress: ExamProgress): Promise<void> {
  try {
    const userId = await getCurrentUserId();
    if (!userId) {
      return;
    }

    const { error } = await supabase
      .from('kv_store_b9034bdd')
      .upsert({
        key: `progress-${userId}`,
        value: progress,
      });

    if (error) {
      console.error('Error saving progress:', error);
    }
  } catch (error) {
    console.error('Error saving progress to database:', error);
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