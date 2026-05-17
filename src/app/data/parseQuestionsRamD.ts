import questionsData from '../../imports/pasted_text/project-management-quiz.md?raw';

export interface Question {
  id: number;
  questionNumber: number;
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

function parseTSVQuestions(tsv: string): Question[] {
  const questions: Question[] = [];
  const lines = tsv.split('\n');

  // Skip header line
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;

    const columns = line.split('\t');
    if (columns.length < 9) continue;

    const questionNumber = parseInt(columns[0]) || i;
    const questionText = columns[1];
    const optionA = columns[2];
    const optionB = columns[3];
    const optionC = columns[4];
    const optionD = columns[5];
    // Option E (columns[6]) is often empty
    const answerLetter = columns[7].trim();
    const explanation = columns[8];

    if (!questionText || !optionA || !optionB || !optionC || !optionD || !answerLetter) {
      continue;
    }

    const options = [optionA, optionB, optionC, optionD].filter(opt => opt && opt.trim());

    // Convert answer letter to index (A=0, B=1, C=2, D=3)
    let correctAnswer = 0;
    if (answerLetter === 'B') correctAnswer = 1;
    else if (answerLetter === 'C') correctAnswer = 2;
    else if (answerLetter === 'D') correctAnswer = 3;

    questions.push({
      id: i,
      questionNumber: questionNumber,
      question: questionText,
      options: options,
      correctAnswer: correctAnswer,
      explanation: explanation || 'No explanation provided.'
    });
  }

  return questions;
}

export function createExamSetsRamD(allQuestions: Question[]): ExamSet[] {
  const examSets: ExamSet[] = [];
  const questionsPerSet = 15;

  let setNumber = 1;
  for (let i = 0; i < allQuestions.length; i += questionsPerSet) {
    const setQuestions = allQuestions.slice(i, i + questionsPerSet);
    if (setQuestions.length > 0) {
      examSets.push({
        id: setNumber,
        title: `RamD Set ${setNumber}`,
        questions: setQuestions
      });
      setNumber++;
    }
  }

  return examSets;
}

let allQuestions: Question[] = [];
try {
  allQuestions = parseTSVQuestions(questionsData);
} catch (error) {
  console.error('Error parsing RamD questions:', error);
  allQuestions = [];
}

export const examSetsRamD = createExamSetsRamD(allQuestions);
