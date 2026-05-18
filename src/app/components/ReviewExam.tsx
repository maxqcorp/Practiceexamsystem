import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Button } from './ui/button';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
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
const sourceMap: Record<string, { sets: Array<{ id: number; title: string; questions: ReviewQuestion[] }>; color: string; bgGradient: string; backLink: string; buttonClass: string }> = {
  main50: { sets: examSets, color: 'indigo', bgGradient: 'from-blue-50 to-indigo-100', backLink: '/sets-50', buttonClass: 'bg-indigo-600 hover:bg-indigo-700' },
  quick25: { sets: examSets25, color: 'purple', bgGradient: 'from-purple-50 to-pink-100', backLink: '/sets-25', buttonClass: 'bg-purple-600 hover:bg-purple-700' },
  ramd: { sets: examSetsRamD, color: 'green', bgGradient: 'from-green-50 to-teal-100', backLink: '/sets-ramd', buttonClass: 'bg-green-600 hover:bg-green-700' },
  davidyt: { sets: examSetsDavidYT, color: 'orange', bgGradient: 'from-orange-50 to-amber-100', backLink: '/sets-davidyt', buttonClass: 'bg-orange-600 hover:bg-orange-700' },
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
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">Review not available</h1>
          <Link to="/">
            <Button>Return to Home</Button>
          </Link>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div className={`min-h-screen bg-gradient-to-br ${sourceConfig.bgGradient} p-6 flex items-center justify-center`}>
        <div className="text-center">
          <BookOpen className="size-12 text-gray-400 mx-auto mb-4 animate-pulse" />
          <p className="text-gray-600">Loading wrong answers...</p>
        </div>
      </div>
    );
  }

  if (wrongAnswers.length === 0) {
    return (
      <div className={`min-h-screen bg-gradient-to-br ${sourceConfig.bgGradient} p-6`}>
        <div className="max-w-4xl mx-auto">
          <div className="mb-6">
            <Link to={sourceConfig.backLink}>
              <Button variant="outline" size="sm">
                <ArrowLeft className="size-4 mr-2" />
                Back to Sets
              </Button>
            </Link>
          </div>
          <div className="bg-white rounded-lg shadow-md p-12 text-center">
            <CheckCircle2 className="size-16 text-green-500 mx-auto mb-4" />
            <h1 className="text-3xl font-bold text-gray-900 mb-2">Great job!</h1>
            <p className="text-lg text-gray-600">
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
    <div className={`min-h-screen bg-gradient-to-br ${sourceConfig.bgGradient} p-6`}>
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6 sticky top-6 z-10">
          <div className="flex items-center justify-between mb-4">
            <Link to={sourceConfig.backLink}>
              <Button variant="outline" size="sm">
                <ArrowLeft className="size-4 mr-2" />
                Back to Sets
              </Button>
            </Link>
            <div className="text-center">
              <h1 className="text-2xl font-bold text-gray-900">Review Wrong Answers</h1>
              <p className="text-sm text-gray-500">{wrongAnswers.length} questions you got wrong</p>
            </div>
            <AlertDialog>
              <AlertDialogTrigger asChild>
                <Button variant="outline" size="sm" className="text-red-600 hover:text-red-700 hover:bg-red-50">
                  <RotateCcw className="size-4 mr-2" />
                  Reset
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

          <div className="space-y-2">
            <div className="flex justify-between text-sm text-gray-600">
              <span>Progress: {answeredCount} / {wrongAnswers.length}</span>
              <span>Corrected: {correctCount} / {answeredCount}</span>
            </div>
            <Progress value={progressPercentage} className="h-2" />
          </div>
        </div>

        {/* Questions */}
        <div className="space-y-6">
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
        </div>

        {/* Footer Summary */}
        {answeredCount === wrongAnswers.length && (
          <Card className="mt-6 bg-green-50 border-green-200">
            <CardContent className="p-6">
              <div className="flex items-center gap-3">
                <CheckCircle2 className="size-8 text-green-600" />
                <div>
                  <h3 className="text-xl font-bold text-gray-900">Review Complete!</h3>
                  <p className="text-gray-700">
                    You corrected {correctCount} out of {wrongAnswers.length} ({Math.round((correctCount / wrongAnswers.length) * 100)}%)
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        )}

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

  const colorMap: Record<string, { bg: string; border: string; badge: string }> = {
    indigo: { bg: 'bg-indigo-50', border: 'border-indigo-200', badge: 'bg-indigo-600' },
    purple: { bg: 'bg-purple-50', border: 'border-purple-200', badge: 'bg-purple-600' },
    green: { bg: 'bg-green-50', border: 'border-green-200', badge: 'bg-green-600' },
    orange: { bg: 'bg-orange-50', border: 'border-orange-200', badge: 'bg-orange-600' },
  };
  const colors = colorMap[color] || colorMap.indigo;

  return (
    <Card className={`${isAnswered ? (isCorrect ? 'border-green-300 bg-green-50' : 'border-red-300 bg-red-50') : ''}`}>
      <CardHeader>
        <div className="flex items-start gap-3">
          <div className={`flex-shrink-0 w-8 h-8 ${colors.badge} text-white rounded-full flex items-center justify-center font-semibold`}>
            {index}
          </div>
          <div className="flex-1">
            <CardTitle className="text-lg">{question.question}</CardTitle>
            <p className="text-xs text-gray-500 mt-1">
              From: {wrongAnswer.originalSetTitle}
            </p>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Left side - Question options */}
          <div className="space-y-3">
            {question.options.map((option, optionIndex) => {
              const isSelected = selectedAnswer === optionIndex;
              const isCorrectOption = optionIndex === question.correctAnswer;

              let buttonClass = 'w-full justify-start text-left h-auto py-3 px-4 ';

              if (isAnswered) {
                if (isCorrectOption) {
                  buttonClass += 'bg-green-100 border-green-500 border-2 hover:bg-green-100';
                } else if (isSelected && !isCorrectOption) {
                  buttonClass += 'bg-red-100 border-red-500 border-2 hover:bg-red-100';
                } else {
                  buttonClass += 'bg-gray-100 border-gray-300 border opacity-60';
                }
              } else {
                buttonClass += 'bg-white border-gray-300 border-2 hover:bg-gray-50 hover:border-gray-400';
              }

              return (
                <Button
                  key={optionIndex}
                  variant="outline"
                  className={buttonClass}
                  onClick={() => !isAnswered && onAnswerClick(wrongAnswer.questionId, optionIndex)}
                  disabled={isAnswered}
                >
                  <div className="flex items-center gap-3 w-full">
                    <span className="font-semibold text-gray-700 flex-shrink-0">
                      {String.fromCharCode(65 + optionIndex)}.
                    </span>
                    <span className="flex-1 text-left break-words whitespace-normal">{option}</span>
                    {isAnswered && isCorrectOption && (
                      <CheckCircle2 className="size-5 text-green-600 flex-shrink-0" />
                    )}
                    {isAnswered && isSelected && !isCorrectOption && (
                      <XCircle className="size-5 text-red-600 flex-shrink-0" />
                    )}
                  </div>
                </Button>
              );
            })}
          </div>

          {/* Right side - Explanation (shown after answer is selected) */}
          {isAnswered && (
            <div className={`p-4 rounded-lg h-fit ${isCorrect ? 'bg-green-100 border border-green-300' : 'bg-amber-100 border border-amber-300'}`}>
              <div className="flex items-start gap-2">
                <AlertCircle className={`size-5 flex-shrink-0 mt-0.5 ${isCorrect ? 'text-green-700' : 'text-amber-700'}`} />
                <div>
                  <p className={`font-semibold mb-1 ${isCorrect ? 'text-green-900' : 'text-amber-900'}`}>
                    {isCorrect ? 'Corrected!' : 'Incorrect'}
                  </p>
                  <p className={`text-sm ${isCorrect ? 'text-green-800' : 'text-amber-800'}`}>
                    {question.explanation}
                  </p>
                  {!isCorrect && (
                    <p className="text-sm text-amber-700 mt-2">
                      Your previous answer was: <strong>{String.fromCharCode(65 + wrongAnswer.userAnswer)}</strong>
                    </p>
                  )}
                </div>
              </div>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
