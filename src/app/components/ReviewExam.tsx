import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Button } from './ui/button';
import { Progress } from './ui/progress';
import { ArrowLeft, CheckCircle2, XCircle, AlertCircle, ArrowUp, RotateCcw, BookOpen } from 'lucide-react';
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from './ui/alert-dialog';
import { getExamSetProgress, saveExamSetProgressDebounced, clearExamSetProgress } from '../utils/storage';
import { getWrongAnswers, WrongAnswer, ReviewQuestion } from '../utils/review';
import { examSets } from '../data/questions';
import { examSets25 } from '../data/parseQuestions25';
import { examSetsRamD } from '../data/parseQuestionsRamD';
import { examSetsDavidYT } from '../data/parseQuestionsDavidYT';

// Map source string to exam sets data
const sourceMap: Record<string, { sets: Array<{ id: number; title: string; questions: ReviewQuestion[] }>; color: string; backLink: string; buttonClass: string }> = {
  main50: { sets: examSets, color: 'indigo', backLink: '/sets-50', buttonClass: 'bg-indigo-600 hover:bg-indigo-700' },
  quick25: { sets: examSets25, color: 'purple', backLink: '/sets-25', buttonClass: 'bg-purple-600 hover:bg-purple-700' },
  ramd: { sets: examSetsRamD, color: 'green', backLink: '/sets-ramd', buttonClass: 'bg-green-600 hover:bg-green-700' },
  davidyt: { sets: examSetsDavidYT, color: 'orange', backLink: '/sets-davidyt', buttonClass: 'bg-orange-600 hover:bg-orange-700' },
};

// Encode exam set ID (must match storage.ts logic)
function encodeExamSetId(source: string, setId: number): number {
  if (source === 'davidyt') return setId + 3000;
  if (source === 'ramd') return setId + 2000;
  if (source === 'quick25') return setId + 1000;
  return setId; // main50
}

export default function ReviewExam() {
  const { source } = useParams<{ source: string }>();
  const sourceConfig = sourceMap[source || ''];

  const [wrongAnswers, setWrongAnswers] = useState<WrongAnswer[]>([]);
  const [answers, setAnswers] = useState<Map<number, number>>(new Map());
  const [showBackToTop, setShowBackToTop] = useState(false);
  const [loading, setLoading] = useState(true);

  // Build a question index to original set mapping for saving progress
  const [questionToSetMap, setQuestionToSetMap] = useState<Map<number, number>>(new Map());

  useEffect(() => {
    if (!sourceConfig) return;

    const loadWrongAnswers = async () => {
      setLoading(true);
      const wrongs = await getWrongAnswers(source!, sourceConfig.sets);
      setWrongAnswers(wrongs);

      // Build mapping from question index (0..N-1) to original set ID
      const map = new Map<number, number>();
      wrongs.forEach((wa, idx) => {
        map.set(idx, wa.originalSetId);
      });
      setQuestionToSetMap(map);

      // Load any existing progress for these original sets
      const allAnswers = new Map<number, number>();
      for (const wa of wrongs) {
        const encodedId = encodeExamSetId(source!, wa.originalSetId);
        const progress = await getExamSetProgress(encodedId);
        const currentAnswer = progress.get(wa.questionId);
        if (currentAnswer !== undefined) {
          allAnswers.set(wa.questionId, currentAnswer);
        }
      }
      setAnswers(allAnswers);
      setLoading(false);
    };

    loadWrongAnswers();
  }, [source]);

  // Save progress whenever answers change
  useEffect(() => {
    if (!sourceConfig || answers.size === 0) return;

    // Save progress to each original set
    const setAnswersMap = new Map<number, Map<number, number>>();
    answers.forEach((answer, questionId) => {
      const idx = wrongAnswers.findIndex(wa => wa.questionId === questionId);
      if (idx === -1) return;
      const originalSetId = questionToSetMap.get(idx);
      if (originalSetId === undefined) return;

      if (!setAnswersMap.has(originalSetId)) {
        setAnswersMap.set(originalSetId, new Map());
      }
      setAnswersMap.get(originalSetId)!.set(questionId, answer);
    });

    // Debounced save for each affected set
    setAnswersMap.forEach((setAnswers, originalSetId) => {
      const encodedId = encodeExamSetId(source!, originalSetId);
      saveExamSetProgressDebounced(encodedId, setAnswers);
    });
  }, [answers, wrongAnswers, questionToSetMap, source]);

  // Scroll to top on mount
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  // Show back-to-top button
  useEffect(() => {
    const handleScroll = () => {
      const scrollHeight = document.documentElement.scrollHeight;
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const clientHeight = window.innerHeight;
      setShowBackToTop(scrollTop + clientHeight >= scrollHeight - 200);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (!sourceConfig) {
    return (
      <div className="min-h-screen bg-[#f8fafc] p-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-xl font-semibold text-gray-900 mb-4">Review not available</h1>
          <Link to="/">
            <Button>Return to Home</Button>
          </Link>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-[#f8fafc] p-6 flex items-center justify-center">
        <div className="text-center">
          <BookOpen className="size-12 text-gray-400 mx-auto mb-4 animate-pulse" />
          <p className="text-gray-600">Loading wrong answers...</p>
        </div>
      </div>
    );
  }

  if (wrongAnswers.length === 0) {
    return (
      <div className="min-h-screen bg-[#f8fafc] p-6">
        <div className="max-w-4xl mx-auto">
          <div className="mb-6">
            <Link to={sourceConfig.backLink}>
              <Button variant="outline" size="sm">
                <ArrowLeft className="size-4 mr-2" />
                Back to Sets
              </Button>
            </Link>
          </div>
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-12 text-center">
            <CheckCircle2 className="size-16 text-green-500 mx-auto mb-4" />
            <h1 className="text-xl font-semibold text-gray-900 mb-2">Great job!</h1>
            <p className="text-base text-gray-600">
              You don't have any wrong answers to review. Keep up the good work!
            </p>
          </div>
        </div>
      </div>
    );
  }

  const handleAnswerClick = (questionId: number, optionIndex: number) => {
    const newAnswers = new Map(answers);
    newAnswers.set(questionId, optionIndex);
    setAnswers(newAnswers);
  };

  const handleReset = async () => {
    // Clear only the wrong answer questions from their original sets
    for (const wa of wrongAnswers) {
      const encodedId = encodeExamSetId(source!, wa.originalSetId);
      const progress = await getExamSetProgress(encodedId);
      progress.delete(wa.questionId);
      await saveExamSetProgressDebounced(encodedId, progress);
    }
    setAnswers(new Map());
  };

  const answeredCount = answers.size;
  const progressPercentage = (answeredCount / wrongAnswers.length) * 100;

  const correctCount = Array.from(answers.entries()).filter(
    ([questionId, answer]) => {
      const wa = wrongAnswers.find(w => w.questionId === questionId);
      return wa && wa.question.correctAnswer === answer;
    }
  ).length;

  return (
    <div className="min-h-screen bg-[#f8fafc]">
      {/* Sticky header */}
      <div className="bg-white border-b border-gray-200 px-4 sm:px-6 py-3 sticky top-0 z-10">
        <div className="max-w-4xl mx-auto">
          <div className="flex items-center gap-3 mb-2">
            <Link to={sourceConfig.backLink}>
              <Button variant="outline" size="sm">
                <ArrowLeft className="size-4 mr-1" />
                <span className="hidden sm:inline">Back to Sets</span>
              </Button>
            </Link>
            <div className="flex-1 min-w-0">
              <h1 className="text-sm font-semibold text-gray-900 truncate">Questions to Revisit</h1>
              <p className="text-xs text-gray-500">{wrongAnswers.length} questions from previous sessions</p>
            </div>
            <AlertDialog>
              <AlertDialogTrigger asChild>
                <Button variant="outline" size="sm" className="text-red-600 border-red-200 hover:bg-red-50 gap-1 flex-shrink-0">
                  <RotateCcw className="size-3.5" />
                  <span className="hidden sm:inline text-xs">Reset</span>
                </Button>
              </AlertDialogTrigger>
              <AlertDialogContent>
                <AlertDialogHeader>
                  <AlertDialogTitle>Reset Review Set</AlertDialogTitle>
                  <AlertDialogDescription>
                    Are you sure you want to reset this review set? Your answers will be cleared from the original sets too. This action cannot be undone.
                  </AlertDialogDescription>
                </AlertDialogHeader>
                <AlertDialogFooter>
                  <AlertDialogCancel>Cancel</AlertDialogCancel>
                  <AlertDialogAction onClick={handleReset} className="bg-red-600 hover:bg-red-700">
                    Reset
                  </AlertDialogAction>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialog>
          </div>

          <div className="flex items-center gap-2">
            <div className="flex-1 bg-gray-100 rounded-full h-1.5">
              <div
                className="bg-indigo-500 h-1.5 rounded-full transition-all"
                style={{ width: `${progressPercentage}%` }}
              />
            </div>
            <span className="text-xs text-gray-400 flex-shrink-0">{answeredCount}/{wrongAnswers.length}</span>
            {answeredCount > 0 && (
              <span className={`text-xs font-semibold flex-shrink-0 ${Math.round((correctCount / answeredCount) * 100) >= 70 ? 'text-green-600' : Math.round((correctCount / answeredCount) * 100) >= 50 ? 'text-amber-600' : 'text-red-500'}`}>
                {Math.round((correctCount / answeredCount) * 100)}%
              </span>
            )}
          </div>
        </div>
      </div>

      {/* Questions */}
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-6 space-y-4">
        {wrongAnswers.map((wa, index) => (
          <ReviewQuestionCard
            key={`${wa.originalSetId}-${wa.questionId}`}
            index={index + 1}
            wrongAnswer={wa}
            selectedAnswer={answers.get(wa.questionId)}
            onAnswerClick={handleAnswerClick}
            color={sourceConfig.color}
          />
        ))}

        {/* Footer Summary */}
        {answeredCount === wrongAnswers.length && (
          <div className="bg-green-50 border border-green-200 rounded-xl p-5 flex items-center gap-3">
            <CheckCircle2 className="size-8 text-green-600 flex-shrink-0" />
            <div>
              <div className="font-semibold text-gray-900">Review Complete!</div>
              <div className="text-sm text-gray-600">
                You corrected {correctCount} out of {wrongAnswers.length} ({Math.round((correctCount / wrongAnswers.length) * 100)}%)
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Back to Top Button */}
      {showBackToTop && (
        <Button
          onClick={scrollToTop}
          className={`fixed bottom-6 right-6 z-50 rounded-full shadow-lg ${sourceConfig.buttonClass}`}
          size="icon"
        >
          <ArrowUp className="size-5" />
        </Button>
      )}
    </div>
  );
}

interface ReviewQuestionCardProps {
  index: number;
  wrongAnswer: WrongAnswer;
  selectedAnswer: number | undefined;
  onAnswerClick: (questionId: number, optionIndex: number) => void;
  color: string;
}

function ReviewQuestionCard({ index, wrongAnswer, selectedAnswer, onAnswerClick, color }: ReviewQuestionCardProps) {
  const question = wrongAnswer.question;
  const isAnswered = selectedAnswer !== undefined;
  const isCorrect = isAnswered && selectedAnswer === question.correctAnswer;

  const colorMap: Record<string, { badge: string }> = {
    indigo: { badge: 'bg-indigo-600' },
    purple: { badge: 'bg-purple-600' },
    green: { badge: 'bg-green-600' },
    orange: { badge: 'bg-orange-600' },
  };
  const colors = colorMap[color] || colorMap.indigo;

  return (
    <div className={`bg-white rounded-xl border-2 p-5 shadow-sm transition-colors ${isAnswered ? (isCorrect ? 'border-green-200' : 'border-red-200') : 'border-gray-200'}`}>
      <div className="flex items-start gap-3 mb-4">
        <div className={`flex-shrink-0 w-8 h-8 ${colors.badge} text-white rounded-full flex items-center justify-center text-xs font-bold`}>
          {index}
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-sm sm:text-base font-medium text-gray-900 leading-relaxed">{question.question}</p>
          <p className="text-xs text-gray-400 mt-1">From: {wrongAnswer.originalSetTitle}</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-3">
        {/* Options */}
        <div className="space-y-2">
          {question.options.map((option, optionIndex) => {
            const isSelected = selectedAnswer === optionIndex;
            const isCorrectOption = optionIndex === question.correctAnswer;

            let cls = 'w-full text-left px-4 py-2.5 rounded-lg border-2 flex items-center gap-2.5 text-sm transition-colors ';
            if (!isAnswered) {
              cls += 'border-gray-200 hover:border-indigo-300 hover:bg-indigo-50 cursor-pointer bg-white';
            } else if (isCorrectOption) {
              cls += 'border-green-400 bg-green-50 cursor-default';
            } else if (isSelected) {
              cls += 'border-red-400 bg-red-50 cursor-default';
            } else {
              cls += 'border-gray-100 bg-gray-50 opacity-50 cursor-default';
            }

            return (
              <button
                key={optionIndex}
                className={cls}
                onClick={() => !isAnswered && onAnswerClick(wrongAnswer.questionId, optionIndex)}
                disabled={isAnswered}
              >
                <span className="font-bold text-gray-400 flex-shrink-0 w-5">{String.fromCharCode(65 + optionIndex)}.</span>
                <span className="flex-1 text-gray-800 break-words whitespace-normal">{option}</span>
                {isAnswered && isCorrectOption && <CheckCircle2 className="size-4 text-green-500 flex-shrink-0" />}
                {isAnswered && isSelected && !isCorrectOption && <XCircle className="size-4 text-red-500 flex-shrink-0" />}
              </button>
            );
          })}
        </div>

        {/* Explanation */}
        {isAnswered && (
          <div className={`p-4 rounded-lg border text-sm leading-relaxed h-fit ${isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-amber-50 border-amber-200 text-amber-900'}`}>
            <div className="flex items-start gap-2">
              <AlertCircle className={`size-4 flex-shrink-0 mt-0.5 ${isCorrect ? 'text-green-600' : 'text-amber-600'}`} />
              <div>
                <p className="font-semibold mb-1">
                  {isCorrect ? 'Corrected!' : 'Incorrect'}
                </p>
                <p>{question.explanation}</p>
                {!isCorrect && (
                  <p className="mt-2 text-amber-700">
                    Your previous answer was: <strong>{String.fromCharCode(65 + wrongAnswer.userAnswer)}</strong>
                  </p>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
