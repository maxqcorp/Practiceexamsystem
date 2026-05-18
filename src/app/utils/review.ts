import { getExamSetProgress } from './storage';

// Generic question interface that works across all exam sources
export interface ReviewQuestion {
  id: number;
  questionNumber: number | string;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
}

export interface ExamSet {
  id: number;
  title: string;
  questions: ReviewQuestion[];
}

export interface WrongAnswer {
  originalSetId: number;
  originalSetTitle: string;
  questionId: number;
  question: ReviewQuestion;
  userAnswer: number;
}

export interface WrongAnswerSummary {
  totalWrong: number;
  bySet: Map<number, number>;
}

// Encode exam set ID with source prefix (must match storage.ts logic)
function encodeExamSetId(source: string, setId: number): number {
  if (source === 'davidyt') return setId + 3000;
  if (source === 'ramd') return setId + 2000;
  if (source === 'quick25') return setId + 1000;
  return setId; // main50
}

/**
 * Collect all wrong answers across all exam sets for a given source.
 */
export async function getWrongAnswers(
  source: string,
  examSets: ExamSet[]
): Promise<WrongAnswer[]> {
  const wrongAnswers: WrongAnswer[] = [];

  for (const set of examSets) {
    const encodedSetId = encodeExamSetId(source, set.id);
    const progress = await getExamSetProgress(encodedSetId);

    for (const [questionId, selectedAnswer] of progress) {
      const question = set.questions.find(q => q.id === questionId);
      if (question && selectedAnswer !== question.correctAnswer) {
        wrongAnswers.push({
          originalSetId: set.id,
          originalSetTitle: set.title,
          questionId,
          question,
          userAnswer: selectedAnswer,
        });
      }
    }
  }

  return wrongAnswers;
}

/**
 * Get a summary of wrong answers (total count + per set breakdown).
 */
export async function getWrongAnswerSummary(
  source: string,
  examSets: ExamSet[]
): Promise<WrongAnswerSummary> {
  const wrongAnswers = await getWrongAnswers(source, examSets);
  const bySet = new Map<number, number>();

  for (const wa of wrongAnswers) {
    bySet.set(wa.originalSetId, (bySet.get(wa.originalSetId) || 0) + 1);
  }

  return {
    totalWrong: wrongAnswers.length,
    bySet,
  };
}
