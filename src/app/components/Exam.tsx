import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { examSets, Question } from '../data/questions';
import { Button } from './ui/button';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Progress } from './ui/progress';
import { ArrowLeft, CheckCircle2, XCircle, AlertCircle, RotateCcw, ArrowUp } from 'lucide-react';
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

export default function Exam() {
  const { setId } = useParams();
  const examSet = examSets.find(set => set.id === Number(setId));
  
  // Track which questions have been answered and what was selected
  const [answers, setAnswers] = useState<Map<number, number>>(new Map());
  const [showBackToTop, setShowBackToTop] = useState(false);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Load saved progress on mount
  useEffect(() => {
    if (examSet) {
      getExamSetProgress(examSet.id).then(savedProgress => {
        setAnswers(savedProgress);
      });
    }
  }, [examSet]);

  // Save progress whenever answers change (debounced)
  useEffect(() => {
    if (examSet && answers.size > 0) {
      saveExamSetProgressDebounced(examSet.id, answers);
    }
  }, [answers, examSet]);

  // Scroll to top when opening a new practice set
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  // Show back-to-top button when near bottom
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

  if (!examSet) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">Exam set not found</h1>
          <Link to="/">
            <Button>Return to Home</Button>
          </Link>
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
    setAnswers(new Map());
    await clearExamSetProgress(examSet.id);
  };

  const answeredCount = answers.size;
  const progressPercentage = (answeredCount / examSet.questions.length) * 100;

  const correctCount = Array.from(answers.entries()).filter(
    ([questionId, answer]) => {
      const question = examSet.questions.find(q => q.id === questionId);
      return question && question.correctAnswer === answer;
    }
  ).length;

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6 sticky top-6 z-10">
          <div className="flex items-center justify-between mb-4">
            <Link to="/sets-50">
              <Button variant="outline" size="sm">
                <ArrowLeft className="size-4 mr-2" />
                Back to Sets
              </Button>
            </Link>
            <h1 className="text-2xl font-bold text-gray-900">{examSet.title}</h1>
            <AlertDialog>
              <AlertDialogTrigger asChild>
                <Button variant="outline" size="sm" className="text-red-600 hover:text-red-700 hover:bg-red-50">
                  <RotateCcw className="size-4 mr-2" />
                  Reset
                </Button>
              </AlertDialogTrigger>
              <AlertDialogContent>
                <AlertDialogHeader>
                  <AlertDialogTitle>Reset Practice Set</AlertDialogTitle>
                  <AlertDialogDescription>
                    Are you sure you want to reset this practice set? All your answers and progress will be lost. This action cannot be undone.
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
              <span>Progress: {answeredCount} / {examSet.questions.length}</span>
              <span>Score: {correctCount} / {answeredCount}</span>
            </div>
            <Progress value={progressPercentage} className="h-2" />
          </div>
        </div>

        {/* Questions */}
        <div className="space-y-6">
          {examSet.questions.map((question) => (
            <QuestionCard
              key={question.id}
              question={question}
              selectedAnswer={answers.get(question.id)}
              onAnswerClick={handleAnswerClick}
            />
          ))}
        </div>

        {/* Footer Summary */}
        {answeredCount === examSet.questions.length && (
          <Card className="mt-6 bg-green-50 border-green-200">
            <CardContent className="p-6">
              <div className="flex items-center gap-3">
                <CheckCircle2 className="size-8 text-green-600" />
                <div>
                  <h3 className="text-xl font-bold text-gray-900">Exam Complete!</h3>
                  <p className="text-gray-700">
                    You scored {correctCount} out of {examSet.questions.length} ({Math.round((correctCount / examSet.questions.length) * 100)}%)
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
            className="fixed bottom-6 right-6 z-50 rounded-full shadow-lg bg-indigo-600 hover:bg-indigo-700"
            size="icon"
          >
            <ArrowUp className="size-5" />
          </Button>
        )}
      </div>
    </div>
  );
}

interface QuestionCardProps {
  question: Question;
  selectedAnswer: number | undefined;
  onAnswerClick: (questionId: number, optionIndex: number) => void;
}

function QuestionCard({ question, selectedAnswer, onAnswerClick }: QuestionCardProps) {
  const isAnswered = selectedAnswer !== undefined;
  const isCorrect = isAnswered && selectedAnswer === question.correctAnswer;

  return (
    <Card className={`${isAnswered ? (isCorrect ? 'border-green-300 bg-green-50' : 'border-red-300 bg-red-50') : ''}`}>
      <CardHeader>
        <div className="flex items-start gap-3">
          <div className="flex-shrink-0 w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center font-semibold">
            {question.questionNumber}
          </div>
          <CardTitle className="flex-1 text-lg">{question.question}</CardTitle>
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
                buttonClass += 'bg-white border-gray-300 border-2 hover:bg-indigo-50 hover:border-indigo-400';
              }

              return (
                <Button
                  key={optionIndex}
                  variant="outline"
                  className={buttonClass}
                  onClick={() => !isAnswered && onAnswerClick(question.id, optionIndex)}
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
                    {isCorrect ? 'Correct!' : 'Incorrect'}
                  </p>
                  <p className={`text-sm ${isCorrect ? 'text-green-800' : 'text-amber-800'}`}>
                    {question.explanation}
                  </p>
                </div>
              </div>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}