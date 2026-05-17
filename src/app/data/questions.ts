import questionsMarkdown from '../../imports/project-management-questions-1.md?raw';
import { parseQuestionsFromMarkdown, createExamSets } from './parseQuestions';

export interface Question {
  id: number;
  questionNumber: number; // The actual question number from the markdown file
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
}

export interface ExamSet {
  id: number;
  title: string;
  questions: Question[];
}

// Parse all questions from the markdown file
const allQuestions = parseQuestionsFromMarkdown(questionsMarkdown);

// Create exam sets: 8 sets of 200 questions + remaining questions in the last set
export const examSets: ExamSet[] = createExamSets(allQuestions);