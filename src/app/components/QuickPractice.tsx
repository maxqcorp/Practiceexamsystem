import { Link, useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { examSets25 } from '../data/parseQuestions25';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { BookOpen, FileText, PlayCircle, RefreshCw, ArrowLeft, RotateCcw, AlertCircle } from 'lucide-react';
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
import { getExamStats, clearExamSetProgress, clearWrongAnswersForSet, ExamStats } from '../utils/storage';
import { getWrongAnswerSummary } from '../utils/review';

export default function QuickPractice() {
  const totalQuestions = examSets25.reduce((sum, set) => sum + set.questions.length, 0);
  const [refreshKey, setRefreshKey] = useState(0);
  const [statsMap, setStatsMap] = useState<Map<number, ExamStats>>(new Map());
  const [wrongAnswerCount, setWrongAnswerCount] = useState(0);
  const [wrongBySet, setWrongBySet] = useState<Map<number, number>>(new Map());
  const location = useLocation();

  useEffect(() => {
    const loadStats = async () => {
      const newStatsMap = new Map<number, ExamStats>();
      for (const set of examSets25) {
        const stats = await getExamStats(set.id + 1000, set.questions);
        newStatsMap.set(set.id, stats);
      }
      setStatsMap(newStatsMap);

      const summary = await getWrongAnswerSummary('quick25', examSets25);
      setWrongAnswerCount(summary.totalWrong);
      setWrongBySet(summary.bySet);
    };
    loadStats();
  }, [refreshKey, location.key]);

  const handleResetAll = async () => {
    for (const set of examSets25) {
      await clearExamSetProgress(set.id + 1000);
    }
    setRefreshKey(prev => prev + 1);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-pink-100 p-6">
      <div className="max-w-6xl mx-auto">
        <div className="mb-6 flex items-center justify-between">
          <Link to="/">
            <Button variant="outline" size="sm">
              <ArrowLeft className="size-4 mr-2" />
              Back to Home
            </Button>
          </Link>
          <AlertDialog>
            <AlertDialogTrigger asChild>
              <Button variant="outline" size="sm" className="text-red-600 border-red-300 hover:bg-red-50">
                <RotateCcw className="size-4 mr-2" />
                Reset All Progress
              </Button>
            </AlertDialogTrigger>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>Reset all DumpsGate Quick Practice sets?</AlertDialogTitle>
                <AlertDialogDescription>
                  This will clear all your answers and progress for all 25-question sets. This action cannot be undone.
                </AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
                <AlertDialogAction onClick={handleResetAll} className="bg-red-600 hover:bg-red-700">
                  Reset All
                </AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        </div>

        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <BookOpen className="size-12 text-purple-600" />
            <h1 className="text-4xl font-bold text-gray-900">DumpsGate Quick Practice Mode</h1>
          </div>
          <p className="text-lg text-gray-600 mb-2">
            {totalQuestions} questions across {examSets25.length} quick practice sets (25 questions each)
          </p>
          <p className="text-sm text-gray-500">
            Your progress is automatically saved and will persist across sessions
          </p>
        </div>

        {/* Review Wrong Answers Card */}
        {wrongAnswerCount > 0 && (
          <Card className="mb-8 border-2 border-red-200 bg-red-50 hover:shadow-lg transition-shadow">
            <CardHeader>
              <div className="flex items-center gap-2 mb-2">
                <AlertCircle className="size-6 text-red-600" />
                <CardTitle className="text-xl text-red-800">Review Wrong Answers</CardTitle>
              </div>
              <CardDescription className="text-red-700">
                You have {wrongAnswerCount} incorrect answer{wrongAnswerCount > 1 ? 's' : ''} across all Quick Practice sets. Review them to improve!
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Link to="/review/quick25">
                <Button className="w-full bg-red-600 hover:bg-red-700">
                  <AlertCircle className="size-4 mr-2" />
                  Review {wrongAnswerCount} Wrong Answer{wrongAnswerCount > 1 ? 's' : ''}
                </Button>
              </Link>
            </CardContent>
          </Card>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {examSets25.map((set) => {
            const stats = statsMap.get(set.id) || { attempted: 0, correct: 0, total: set.questions.length };
            const isStarted = stats.attempted > 0;
            const progressPercentage = (stats.attempted / stats.total) * 100;
            const scorePercentage = stats.attempted > 0 ? (stats.correct / stats.total) * 100 : 0;

            return (
              <Card key={set.id} className="hover:shadow-lg transition-shadow">
                <CardHeader>
                  <div className="flex items-center gap-2 mb-2">
                    <FileText className="size-5 text-purple-600" />
                    <CardTitle>{set.title}</CardTitle>
                  </div>
                  <CardDescription>
                    {set.questions.length} questions
                  </CardDescription>
                  {isStarted && (
                    <div className="mt-3 space-y-2">
                      <div className="flex justify-between text-xs font-semibold">
                        <span className="text-gray-700">Score: {stats.correct} / {stats.total}</span>
                        <span className={`${scorePercentage >= 70 ? 'text-green-600' : scorePercentage >= 50 ? 'text-amber-600' : 'text-red-600'}`}>
                          {Math.round(scorePercentage)}%
                        </span>
                      </div>
                      <div className="flex justify-between text-xs text-gray-600">
                        <span>Attempted: {stats.attempted} / {stats.total}</span>
                        <span>{Math.round(progressPercentage)}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div 
                          className="bg-purple-600 h-2 rounded-full transition-all"
                          style={{ width: `${progressPercentage}%` }}
                        />
                      </div>
                    </div>
                  )}
                </CardHeader>
                <CardContent>
                  <Link to={`/quick-practice/${set.id}`}>
                    <Button className="w-full bg-purple-600 hover:bg-purple-700">
                      {isStarted ? (
                        <>
                          <RefreshCw className="size-4 mr-2" />
                          Resume Practice
                        </>
                      ) : (
                        <>
                          <PlayCircle className="size-4 mr-2" />
                          Start Practice
                        </>
                      )}
                    </Button>
                  </Link>
                  {(wrongBySet.get(set.id) || 0) > 0 && (
                    <AlertDialog>
                      <AlertDialogTrigger asChild>
                        <Button variant="outline" size="sm" className="w-full mt-2 text-amber-600 border-amber-300 hover:bg-amber-50">
                          <RotateCcw className="size-4 mr-2" />
                          Reset {wrongBySet.get(set.id)} Wrong
                        </Button>
                      </AlertDialogTrigger>
                      <AlertDialogContent>
                        <AlertDialogHeader>
                          <AlertDialogTitle>Reset wrong answers for {set.title}?</AlertDialogTitle>
                          <AlertDialogDescription>
                            This will clear only your incorrect answers in this set, keeping your correct answers intact. This action cannot be undone.
                          </AlertDialogDescription>
                        </AlertDialogHeader>
                        <AlertDialogFooter>
                          <AlertDialogCancel>Cancel</AlertDialogCancel>
                          <AlertDialogAction
                            onClick={async () => {
                              await clearWrongAnswersForSet(set.id + 1000, set.questions);
                              setRefreshKey(prev => prev + 1);
                            }}
                            className="bg-amber-600 hover:bg-amber-700"
                          >
                            Reset Wrong Answers
                          </AlertDialogAction>
                        </AlertDialogFooter>
                      </AlertDialogContent>
                    </AlertDialog>
                  )}
                </CardContent>
              </Card>
            );
          })}
        </div>

        <div className="mt-12 bg-white rounded-lg p-6 shadow-md">
          <h2 className="text-xl font-semibold mb-3 text-gray-900">About DumpsGate Quick Practice Mode</h2>
          <ul className="space-y-2 text-gray-700">
            <li className="flex items-start gap-2">
              <span className="text-purple-600 font-bold">•</span>
              <span>Each set contains 25 questions for shorter, focused practice sessions</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-purple-600 font-bold">•</span>
              <span>Perfect for quick review or when you have limited time</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-purple-600 font-bold">•</span>
              <span>Your progress is tracked separately from the 50-question sets</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}
