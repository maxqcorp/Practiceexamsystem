import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { examSetsDavidYT } from '../data/parseQuestionsDavidYT';
import { getExamSetProgress, saveExamSetProgressDebounced, clearExamSetProgress } from '../utils/storage';
import ExamView, { ExamQuestion } from './shared/ExamView';
import { Button } from './ui/button';

export default function DavidYTExam() {
  const { setId } = useParams();
  const examSet = examSetsDavidYT.find(s => s.id === Number(setId));
  const [answers, setAnswers] = useState<Map<number, number>>(new Map());

  useEffect(() => {
    if (examSet) getExamSetProgress(examSet.id + 3000).then(setAnswers);
  }, [examSet?.id]);

  useEffect(() => {
    if (examSet && answers.size > 0) saveExamSetProgressDebounced(examSet.id + 3000, answers);
  }, [answers, examSet?.id]);

  if (!examSet) return (
    <div className="min-h-screen bg-[#f8fafc] flex items-center justify-center">
      <div className="text-center"><p className="text-gray-500 mb-4">Set not found.</p>
        <Link to="/sets-davidyt"><Button>Back to Sets</Button></Link></div>
    </div>
  );

  const questions: ExamQuestion[] = examSet.questions.map(q => ({
    id: q.id, questionNumber: q.questionNumber, question: q.question,
    options: q.options, correctAnswer: q.correctAnswer, explanation: q.explanation,
  }));

  return (
    <ExamView
      title={examSet.title}
      questions={questions}
      answers={answers}
      onAnswer={(qId, idx) => setAnswers(prev => new Map(prev).set(qId, idx))}
      onReset={async () => { setAnswers(new Map()); await clearExamSetProgress(examSet.id + 3000); }}
      backLink="/sets-davidyt"
      backLabel="David YT Practice"
      accentClass="orange"
      modeStorageKey="exam-mode-davidyt"
    />
  );
}
