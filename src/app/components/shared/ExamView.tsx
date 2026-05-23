import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Button } from '../ui/button';
import { ArrowLeft, CheckCircle2, XCircle, ChevronLeft, ChevronRight, RotateCcw } from 'lucide-react';
import {
  AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent,
  AlertDialogDescription, AlertDialogFooter, AlertDialogHeader,
  AlertDialogTitle, AlertDialogTrigger,
} from '../ui/alert-dialog';

export interface ExamQuestion {
  id: number;
  questionNumber: number | string;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
}

interface ExamViewProps {
  title: string;
  questions: ExamQuestion[];
  answers: Map<number, number>;
  onAnswer: (questionId: number, optionIndex: number) => void;
  onReset: () => void;
  backLink: string;
  backLabel: string;
  accentClass: string;        // e.g. 'indigo' | 'purple' | 'green' | 'orange'
  modeStorageKey: string;     // localStorage key for mode preference
}

export default function ExamView({
  title, questions, answers, onAnswer, onReset, backLink, backLabel, accentClass, modeStorageKey,
}: ExamViewProps) {
  const [mode, setMode] = useState<'study' | 'scroll'>(() => {
    return (localStorage.getItem(modeStorageKey) as 'study' | 'scroll') || 'study';
  });
  const [studyIndex, setStudyIndex] = useState(() => {
    // Start at first unanswered question
    const firstUnanswered = questions.findIndex(q => !answers.has(q.id));
    return firstUnanswered >= 0 ? firstUnanswered : 0;
  });

  useEffect(() => {
    localStorage.setItem(modeStorageKey, mode);
  }, [mode, modeStorageKey]);

  const handleModeChange = (newMode: 'study' | 'scroll') => {
    setMode(newMode);
    if (newMode === 'study') {
      // Jump to first unanswered
      const firstUnanswered = questions.findIndex(q => !answers.has(q.id));
      setStudyIndex(firstUnanswered >= 0 ? firstUnanswered : 0);
    }
  };

  const answeredCount = answers.size;
  const correctCount = Array.from(answers.entries()).filter(([qId, ans]) => {
    const q = questions.find(q => q.id === qId);
    return q && q.correctAnswer === ans;
  }).length;
  const progressPct = questions.length > 0 ? (answeredCount / questions.length) * 100 : 0;
  const scorePct = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;

  // ACCENT COLOR CLASSES — must be full strings (Tailwind purge)
  const accentColors: Record<string, { bg: string; hover: string; ring: string; light: string; text: string; bar: string }> = {
    indigo: { bg: 'bg-indigo-600', hover: 'hover:bg-indigo-700', ring: 'ring-indigo-500', light: 'bg-indigo-50', text: 'text-indigo-600', bar: 'bg-indigo-500' },
    purple: { bg: 'bg-purple-600', hover: 'hover:bg-purple-700', ring: 'ring-purple-500', light: 'bg-purple-50', text: 'text-purple-600', bar: 'bg-purple-500' },
    green:  { bg: 'bg-green-600',  hover: 'hover:bg-green-700',  ring: 'ring-green-500',  light: 'bg-green-50',  text: 'text-green-600',  bar: 'bg-green-500' },
    orange: { bg: 'bg-orange-600', hover: 'hover:bg-orange-700', ring: 'ring-orange-500', light: 'bg-orange-50', text: 'text-orange-600', bar: 'bg-orange-500' },
  };
  const accent = accentColors[accentClass] || accentColors.indigo;

  // Shared header used in both modes
  const Header = (
    <div className="bg-white border-b border-gray-200 px-4 sm:px-6 py-3 flex items-center gap-3 sticky top-0 z-10">
      <Link to={backLink}>
        <Button variant="outline" size="sm" className="gap-1.5 flex-shrink-0">
          <ArrowLeft className="size-4" /><span className="hidden sm:inline">{backLabel}</span>
        </Button>
      </Link>
      <div className="flex-1 min-w-0">
        <div className="text-sm font-semibold text-gray-900 truncate">{title}</div>
        <div className="flex items-center gap-2 mt-0.5">
          <div className="flex-1 bg-gray-100 rounded-full h-1.5 max-w-[200px]">
            <div className={`${accent.bar} h-1.5 rounded-full transition-all`} style={{ width: `${progressPct}%` }} />
          </div>
          <span className="text-xs text-gray-400 flex-shrink-0">{answeredCount}/{questions.length}</span>
          {answeredCount > 0 && (
            <span className={`text-xs font-semibold flex-shrink-0 ${scorePct >= 70 ? 'text-green-600' : scorePct >= 50 ? 'text-amber-600' : 'text-red-500'}`}>{scorePct}%</span>
          )}
        </div>
      </div>
      {/* Mode toggle */}
      <div className="flex items-center bg-gray-100 rounded-lg p-0.5 gap-0.5 flex-shrink-0">
        <button
          onClick={() => handleModeChange('study')}
          className={`px-3 py-1.5 rounded-md text-xs font-semibold transition-colors ${mode === 'study' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500'}`}
        >
          Study
        </button>
        <button
          onClick={() => handleModeChange('scroll')}
          className={`px-3 py-1.5 rounded-md text-xs font-semibold transition-colors ${mode === 'scroll' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500'}`}
        >
          Scroll
        </button>
      </div>
      {/* Reset */}
      <AlertDialog>
        <AlertDialogTrigger asChild>
          <Button variant="outline" size="sm" className="text-red-600 border-red-200 hover:bg-red-50 gap-1 flex-shrink-0">
            <RotateCcw className="size-3.5" /><span className="hidden sm:inline text-xs">Reset</span>
          </Button>
        </AlertDialogTrigger>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Reset this set?</AlertDialogTitle>
            <AlertDialogDescription>All answers and progress will be cleared. This cannot be undone.</AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction onClick={onReset} className="bg-red-600 hover:bg-red-700">Reset</AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );

  if (mode === 'study') {
    const currentQ = questions[studyIndex];
    if (!currentQ) return null;
    const selectedAnswer = answers.get(currentQ.id);
    const isAnswered = selectedAnswer !== undefined;
    const isCorrect = isAnswered && selectedAnswer === currentQ.correctAnswer;
    const unansweredCount = questions.length - answeredCount;

    return (
      <div className="min-h-screen bg-[#f8fafc] flex flex-col">
        {Header}
        <div className="flex-1 flex flex-col max-w-3xl mx-auto w-full px-4 sm:px-6 py-6">

          {/* Question number nav */}
          <div className="flex items-center justify-between mb-5">
            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wide">
              Question {studyIndex + 1} of {questions.length}
            </span>
            {unansweredCount > 0 && unansweredCount < questions.length && (
              <button
                onClick={() => {
                  const nextUnanswered = questions.findIndex((q, i) => i > studyIndex && !answers.has(q.id));
                  const firstUnanswered = questions.findIndex(q => !answers.has(q.id));
                  setStudyIndex(nextUnanswered >= 0 ? nextUnanswered : firstUnanswered >= 0 ? firstUnanswered : studyIndex);
                }}
                className="text-xs font-semibold text-indigo-600 hover:text-indigo-800"
              >
                Skip to unanswered →
              </button>
            )}
          </div>

          {/* Question card */}
          <div className="bg-white rounded-xl border border-gray-200 p-6 mb-4 shadow-sm">
            <p className="text-base sm:text-lg font-medium text-gray-900 leading-relaxed mb-6">{currentQ.question}</p>
            <div className="space-y-2.5">
              {currentQ.options.map((option, idx) => {
                const isSelected = selectedAnswer === idx;
                const isCorrectOpt = idx === currentQ.correctAnswer;
                let cls = 'w-full text-left px-4 py-3 rounded-lg border-2 transition-all flex items-center gap-3 text-sm ';
                if (!isAnswered) {
                  cls += 'border-gray-200 bg-white hover:border-indigo-300 hover:bg-indigo-50 cursor-pointer';
                } else if (isCorrectOpt) {
                  cls += 'border-green-400 bg-green-50 cursor-default';
                } else if (isSelected) {
                  cls += 'border-red-400 bg-red-50 cursor-default';
                } else {
                  cls += 'border-gray-100 bg-gray-50 opacity-60 cursor-default';
                }
                return (
                  <button
                    key={idx}
                    className={cls}
                    onClick={() => !isAnswered && onAnswer(currentQ.id, idx)}
                    disabled={isAnswered}
                  >
                    <span className={`flex-shrink-0 w-7 h-7 rounded-full border-2 flex items-center justify-center text-xs font-bold
                      ${!isAnswered ? 'border-gray-300 text-gray-500' : isCorrectOpt ? 'border-green-500 bg-green-500 text-white' : isSelected ? 'border-red-500 bg-red-500 text-white' : 'border-gray-200 text-gray-300'}`}>
                      {String.fromCharCode(65 + idx)}
                    </span>
                    <span className={`flex-1 ${isAnswered && !isCorrectOpt && !isSelected ? 'text-gray-400' : 'text-gray-800'}`}>{option}</span>
                    {isAnswered && isCorrectOpt && <CheckCircle2 className="size-5 text-green-500 flex-shrink-0" />}
                    {isAnswered && isSelected && !isCorrectOpt && <XCircle className="size-5 text-red-500 flex-shrink-0" />}
                  </button>
                );
              })}
            </div>

            {/* Explanation */}
            {isAnswered && (
              <div className={`mt-5 p-4 rounded-lg border text-sm leading-relaxed ${isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-amber-50 border-amber-200 text-amber-900'}`}>
                <p className="font-semibold mb-1">{isCorrect ? '✓ Correct!' : '✗ Incorrect'}</p>
                <p>{currentQ.explanation}</p>
              </div>
            )}
          </div>

          {/* Navigation */}
          <div className="flex items-center justify-between">
            <Button
              variant="outline"
              onClick={() => setStudyIndex(i => Math.max(0, i - 1))}
              disabled={studyIndex === 0}
              className="gap-1.5"
            >
              <ChevronLeft className="size-4" /> Previous
            </Button>
            {answeredCount === questions.length && (
              <div className="text-center px-3">
                <div className="text-sm font-semibold text-gray-900">All done! Score: {correctCount}/{questions.length} ({Math.round((correctCount / questions.length) * 100)}%)</div>
              </div>
            )}
            <Button
              onClick={() => setStudyIndex(i => Math.min(questions.length - 1, i + 1))}
              disabled={studyIndex === questions.length - 1}
              className={`${accent.bg} ${accent.hover} text-white gap-1.5`}
            >
              Next <ChevronRight className="size-4" />
            </Button>
          </div>
        </div>
      </div>
    );
  }

  // SCROLL MODE — all questions visible
  return (
    <div className="min-h-screen bg-[#f8fafc]">
      {Header}
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-6 space-y-4">
        {questions.map((q) => {
          const sel = answers.get(q.id);
          const isAnswered = sel !== undefined;
          const isCorrect = isAnswered && sel === q.correctAnswer;
          return (
            <div key={q.id} className={`bg-white rounded-xl border-2 p-5 shadow-sm transition-colors ${isAnswered ? (isCorrect ? 'border-green-200' : 'border-red-200') : 'border-gray-200'}`}>
              <div className="flex items-start gap-3 mb-4">
                <span className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold text-white ${accent.bg}`}>
                  {q.questionNumber}
                </span>
                <p className="text-sm sm:text-base font-medium text-gray-900 leading-relaxed flex-1">{q.question}</p>
              </div>
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-3">
                <div className="space-y-2">
                  {q.options.map((opt, idx) => {
                    const isSelected = sel === idx;
                    const isCorrectOpt = idx === q.correctAnswer;
                    let cls = 'w-full text-left px-4 py-2.5 rounded-lg border-2 flex items-center gap-2.5 text-sm transition-colors ';
                    if (!isAnswered) cls += 'border-gray-200 hover:border-indigo-300 hover:bg-indigo-50 cursor-pointer bg-white';
                    else if (isCorrectOpt) cls += 'border-green-400 bg-green-50 cursor-default';
                    else if (isSelected) cls += 'border-red-400 bg-red-50 cursor-default';
                    else cls += 'border-gray-100 bg-gray-50 opacity-50 cursor-default';
                    return (
                      <button key={idx} className={cls} onClick={() => !isAnswered && onAnswer(q.id, idx)} disabled={isAnswered}>
                        <span className="font-bold text-gray-400 flex-shrink-0 w-5">{String.fromCharCode(65 + idx)}.</span>
                        <span className="flex-1 text-gray-800">{opt}</span>
                        {isAnswered && isCorrectOpt && <CheckCircle2 className="size-4 text-green-500 flex-shrink-0" />}
                        {isAnswered && isSelected && !isCorrectOpt && <XCircle className="size-4 text-red-500 flex-shrink-0" />}
                      </button>
                    );
                  })}
                </div>
                {isAnswered && (
                  <div className={`p-4 rounded-lg border text-sm leading-relaxed h-fit ${isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-amber-50 border-amber-200 text-amber-900'}`}>
                    <p className="font-semibold mb-1">{isCorrect ? '✓ Correct' : '✗ Incorrect'}</p>
                    <p>{q.explanation}</p>
                  </div>
                )}
              </div>
            </div>
          );
        })}
        {answeredCount === questions.length && questions.length > 0 && (
          <div className="bg-green-50 border border-green-200 rounded-xl p-5 flex items-center gap-3">
            <CheckCircle2 className="size-8 text-green-600 flex-shrink-0" />
            <div>
              <div className="font-semibold text-gray-900">Set Complete!</div>
              <div className="text-sm text-gray-600">Score: {correctCount} / {questions.length} — {Math.round((correctCount / questions.length) * 100)}%</div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
