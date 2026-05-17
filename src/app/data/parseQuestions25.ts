import questionsMarkdown from '../../imports/project-management-questions-1.md?raw';

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

function parseMarkdownQuestions(markdown: string): Question[] {
  const questions: Question[] = [];
  
  // Split by "Question X" pattern and capture the question number
  const questionPattern = /\"Question (\d+)/g;
  const matches = [...markdown.matchAll(questionPattern)];
  const questionBlocks = markdown.split(/\"Question \d+/);
  
  for (let i = 1; i < questionBlocks.length; i++) {
    const block = questionBlocks[i];
    const questionNumber = matches[i - 1] ? parseInt(matches[i - 1][1]) : i;
    
    // Extract question text (everything before options)
    const optionAIndex = block.indexOf('\na. ');
    if (optionAIndex === -1) continue;
    
    const questionText = block.substring(0, optionAIndex).trim();
    
    // Extract options
    const optionAMatch = block.match(/\na\. (.+?)(?=\nb\. )/s);
    const optionBMatch = block.match(/\nb\. (.+?)(?=\nc\. )/s);
    const optionCMatch = block.match(/\nc\. (.+?)(?=\nd\. )/s);
    const optionDMatch = block.match(/\nd\. (.+?)(?=\n)/s);
    
    if (!optionAMatch || !optionBMatch || !optionCMatch || !optionDMatch) continue;
    
    const options = [
      optionAMatch[1].trim(),
      optionBMatch[1].trim(),
      optionCMatch[1].trim(),
      optionDMatch[1].trim()
    ];
    
    // Extract answer
    const answerMatch = block.match(/Answer: ([A-D])/);
    if (!answerMatch) continue;
    
    const answerLetter = answerMatch[1];
    const correctAnswer = answerLetter.charCodeAt(0) - 65; // Convert A-D to 0-3
    
    // Extract explanation
    const explanationMatch = block.match(/Explanation: (.+?)(?=\"|$)/s);
    const explanation = explanationMatch ? explanationMatch[1].trim() : 'No explanation provided.';
    
    questions.push({
      id: i,
      questionNumber: questionNumber,
      question: questionText,
      options: options,
      correctAnswer: correctAnswer,
      explanation: explanation
    });
  }
  
  return questions;
}

export function createExamSets25(allQuestions: Question[]): ExamSet[] {
  const examSets: ExamSet[] = [];
  const questionsPerSet = 25;
  
  let setNumber = 1;
  for (let i = 0; i < allQuestions.length; i += questionsPerSet) {
    const setQuestions = allQuestions.slice(i, i + questionsPerSet);
    examSets.push({
      id: setNumber,
      title: `Set ${setNumber}`,
      questions: setQuestions
    });
    setNumber++;
  }
  
  return examSets;
}

const allQuestions = parseMarkdownQuestions(questionsMarkdown);
export const examSets25 = createExamSets25(allQuestions);