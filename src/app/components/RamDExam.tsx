import { useParams, Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { examSetsRamD, Question } from '../data/parseQuestionsRamD';
import { Button } from './ui/button';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { ArrowLeft, CheckCircle, XCircle, RotateCcw } from 'lucide-react';
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

export default function RamDExam() {
  const { setId } = useParams();
  const examSet = examSetsRamD.find(set => set.id === Number(setId));
  const [answers, setAnswers] = useState<Map<number, number>>(new Map());

  useEffect(() => {
    if (examSet) {
      getExamSetProgress(examSet.id + 2000).then(savedProgress => {
        setAnswers(savedProgress);
      });
    }
  }, [examSet]);

  useEffect(() => {
    if (examSet && answers.size > 0) {
      saveExamSetProgressDebounced(examSet.id + 2000, answers);
    }
  }, [answers, examSet]);

  if (!examSet) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-green-50 to-teal-100 p-6 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">Set not found</h1>
          <Link to="/sets-ramd">
            <Button>Back to RamD Sets</Button>
          </Link>
        </div>
      </div>
    );
  }

  const handleAnswerSelect = (questionId: number, answerIndex: number) => {
    if (answers.has(questionId)) return;
    const newAnswers = new Map(answers);
    newAnswers.set(questionId, answerIndex);
    setAnswers(newAnswers);
  };

  const handleReset = async () => {
    setAnswers(new Map());
    if (examSet) {
      await clearExamSetProgress(examSet.id + 2000);
    }
  };

  const renderQuestion = (question: Question, index: number) => {
    const selectedAnswer = answers.get(question.id);
    const isSubmitted = selectedAnswer !== undefined;
    const isCorrect = isSubmitted && selectedAnswer === question.correctAnswer;

    return (
      <Card key={question.id} className="mb-6">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <span className="text-green-600">Question {question.questionNumber}</span>
            {isSubmitted && (
              isCorrect ?
                <CheckCircle className="size-5 text-green-600" /> :
                <XCircle className="size-5 text-red-600" />
            )}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-gray-800 mb-4">{question.question}</p>

          <div className="space-y-2">
            {question.options.map((option, optionIndex) => {
              const isSelected = selectedAnswer === optionIndex;
              const isCorrectAnswer = optionIndex === question.correctAnswer;
              const showCorrect = isSubmitted && isCorrectAnswer;
              const showIncorrect = isSubmitted && isSelected && !isCorrectAnswer;

              return (
                <button
                  key={optionIndex}
                  onClick={() => handleAnswerSelect(question.id, optionIndex)}
                  disabled={isSubmitted}
                  className={`w-full text-left p-4 rounded-lg border-2 transition-all ${
                    showCorrect ? 'bg-green-50 border-green-500' :
                    showIncorrect ? 'bg-red-50 border-red-500' :
                    isSelected ? 'bg-green-50 border-green-300' :
                    'bg-white border-gray-200 hover:border-green-300'
                  } ${isSubmitted ? 'cursor-default' : 'cursor-pointer'}`}
                >
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-gray-700">
                      {String.fromCharCode(65 + optionIndex)}.
                    </span>
                    <span className="text-gray-800">{option}</span>
                    {showCorrect && <CheckCircle className="size-5 text-green-600 ml-auto" />}
                    {showIncorrect && <XCircle className="size-5 text-red-600 ml-auto" />}
                  </div>
                </button>
              );
            })}
          </div>

          {isSubmitted && (
            <div className="mt-4 p-4 bg-blue-50 rounded-lg border border-blue-200">
              <p className="font-semibold text-blue-900 mb-2">Explanation:</p>
              <p className="text-blue-800">{question.explanation}</p>
            </div>
          )}
        </CardContent>
      </Card>
    );
  };

  const totalQuestions = examSet.questions.length;
  const answeredQuestions = answers.size;
  const correctAnswers = Array.from(answers.entries()).filter(([questionId, answer]) => {
    const question = examSet.questions.find(q => q.id === questionId);
    return question && question.correctAnswer === answer;
  }).length;

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-teal-100 p-6">
      <div className="max-w-4xl mx-auto">
        <div className="mb-6">
          <Link to="/sets-ramd">
            <Button variant="outline" size="sm">
              <ArrowLeft className="size-4 mr-2" />
              Back to RamD Sets
            </Button>
          </Link>
        </div>

        <div className="bg-white rounded-lg p-6 shadow-md mb-6">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-3xl font-bold text-gray-900">{examSet.title}</h1>
            {answeredQuestions > 0 && (
              <AlertDialog>
                <AlertDialogTrigger asChild>
                  <Button variant="outline" size="sm" className="text-red-600 border-red-300 hover:bg-red-50">
                    <RotateCcw className="size-4 mr-2" />
                    Reset Progress
                  </Button>
                </AlertDialogTrigger>
                <AlertDialogContent>
                  <AlertDialogHeader>
                    <AlertDialogTitle>Reset this set?</AlertDialogTitle>
                    <AlertDialogDescription>
                      This will clear all your answers and progress for {examSet.title}. This action cannot be undone.
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
            )}
          </div>
          <div className="flex flex-wrap gap-6 text-sm">
            <div className="flex items-center gap-2">
              <span className="text-gray-600">Progress:</span>
              <span className="font-semibold text-green-600">
                {answeredQuestions} / {totalQuestions}
              </span>
            </div>
            {answeredQuestions > 0 && (
              <div className="flex items-center gap-2">
                <span className="text-gray-600">Score:</span>
                <span className="font-semibold text-green-600">
                  {correctAnswers} / {totalQuestions} ({Math.round((correctAnswers / totalQuestions) * 100)}%)
                </span>
              </div>
            )}
          </div>
        </div>

        <div>
          {examSet.questions.map((question, index) => renderQuestion(question, index))}
        </div>
      </div>
    </div>
  );
}
