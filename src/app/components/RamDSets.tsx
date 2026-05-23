import { Link, useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { examSetsRamD } from '../data/parseQuestionsRamD';
import { Button } from './ui/button';
import { FileText, PlayCircle, RefreshCw, ArrowLeft, RotateCcw, BookOpen } from 'lucide-react';
import {
  AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent,
  AlertDialogDescription, AlertDialogFooter, AlertDialogHeader,
  AlertDialogTitle, AlertDialogTrigger,
} from './ui/alert-dialog';
import { getExamStats, clearExamSetProgress, clearWrongAnswersForSet, ExamStats } from '../utils/storage';
import { getWrongAnswerSummary } from '../utils/review';

export default function RamDSets() {
  const [refreshKey, setRefreshKey] = useState(0);
  const [statsMap, setStatsMap] = useState<Map<number, ExamStats>>(new Map());
  const [wrongAnswerCount, setWrongAnswerCount] = useState(0);
  const [wrongBySet, setWrongBySet] = useState<Map<number, number>>(new Map());
  const [filter, setFilter] = useState<'all' | 'progress' | 'done' | 'new'>('all');
  const location = useLocation();
  const totalQuestions = examSetsRamD.reduce((sum, set) => sum + set.questions.length, 0);

  useEffect(() => {
    const loadStats = async () => {
      const newStatsMap = new Map<number, ExamStats>();
      for (const set of examSetsRamD) {
        const stats = await getExamStats(set.id + 2000, set.questions);
        newStatsMap.set(set.id, stats);
      }
      setStatsMap(newStatsMap);

      const summary = await getWrongAnswerSummary('ramd', examSetsRamD);
      setWrongAnswerCount(summary.totalWrong);
      setWrongBySet(summary.bySet);
    };
    loadStats();
  }, [refreshKey, location.key]);

  const handleResetAll = async () => {
    for (const set of examSetsRamD) {
      await clearExamSetProgress(set.id + 2000);
    }
    setRefreshKey(k => k + 1);
  };

  const filteredSets = examSetsRamD.filter(set => {
    const stats = statsMap.get(set.id) || { attempted: 0, correct: 0, total: set.questions.length };
    if (filter === 'progress') return stats.attempted > 0 && stats.attempted < stats.total;
    if (filter === 'done') return stats.attempted === stats.total;
    if (filter === 'new') return stats.attempted === 0;
    return true;
  });

  const continueSet = examSetsRamD.find(set => {
    const stats = statsMap.get(set.id);
    return stats && stats.attempted > 0 && stats.attempted < stats.total;
  });

  return (
    <div className="min-h-screen bg-[#f8fafc] p-4 sm:p-6">
      <div className="max-w-5xl mx-auto">

        {/* Top nav */}
        <div className="flex items-center justify-between mb-6">
          <Link to="/">
            <Button variant="outline" size="sm" className="gap-1.5">
              <ArrowLeft className="size-4" /> Home
            </Button>
          </Link>
          <AlertDialog>
            <AlertDialogTrigger asChild>
              <Button variant="outline" size="sm" className="text-red-600 border-red-200 hover:bg-red-50 gap-1.5">
                <RotateCcw className="size-4" /> Reset All
              </Button>
            </AlertDialogTrigger>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>Reset all RamD Practice sets?</AlertDialogTitle>
                <AlertDialogDescription>This clears all answers and progress. Cannot be undone.</AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
                <AlertDialogAction onClick={handleResetAll} className="bg-red-600 hover:bg-red-700">Reset All</AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        </div>

        {/* Page title */}
        <div className="mb-6">
          <div className="flex items-center gap-2.5 mb-1">
            <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-green-100 text-green-700 border border-green-200">RamD Practice</span>
          </div>
          <h1 className="text-xl font-semibold text-gray-900">RamD Practice</h1>
          <p className="text-sm text-gray-400 mt-0.5">{totalQuestions.toLocaleString()} questions · {examSetsRamD.length} sets</p>
        </div>

        {/* Questions to revisit */}
        {wrongAnswerCount > 0 && (
          <Link to="/review/ramd">
            <div className="mb-4 flex items-center gap-3 bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 hover:bg-amber-100 transition-colors cursor-pointer">
              <BookOpen className="size-5 text-amber-600 flex-shrink-0" />
              <div className="flex-1 min-w-0">
                <div className="text-sm font-semibold text-amber-900">Questions to Revisit</div>
                <div className="text-xs text-amber-700">{wrongAnswerCount} incorrect answer{wrongAnswerCount !== 1 ? 's' : ''} ready for review</div>
              </div>
              <span className="text-xs font-semibold bg-amber-200 text-amber-800 px-2.5 py-1 rounded-full">Review →</span>
            </div>
          </Link>
        )}

        {/* Continue card */}
        {continueSet && (() => {
          const stats = statsMap.get(continueSet.id)!;
          const pct = Math.round((stats.attempted / stats.total) * 100);
          return (
            <Link to={`/ramd/${continueSet.id}`}>
              <div className="mb-4 flex items-center gap-3 bg-white border border-indigo-200 rounded-xl px-4 py-3 hover:border-indigo-400 hover:shadow-sm transition-all cursor-pointer">
                <div className="flex-1 min-w-0">
                  <div className="text-xs font-semibold text-indigo-500 uppercase tracking-wide mb-0.5">Continue where you left off</div>
                  <div className="text-sm font-semibold text-gray-900">{continueSet.title}</div>
                  <div className="flex items-center gap-2 mt-1.5">
                    <div className="flex-1 bg-gray-100 rounded-full h-1.5">
                      <div className="bg-indigo-500 h-1.5 rounded-full" style={{ width: `${pct}%` }} />
                    </div>
                    <span className="text-xs text-gray-400 flex-shrink-0">{stats.attempted}/{stats.total}</span>
                  </div>
                </div>
                <RefreshCw className="size-4 text-indigo-400 flex-shrink-0" />
              </div>
            </Link>
          );
        })()}

        {/* Filter tabs */}
        <div className="flex items-center gap-1 mb-4 bg-white border border-gray-200 rounded-lg p-1 w-fit">
          {([['all', 'All'], ['progress', 'In Progress'], ['done', 'Completed'], ['new', 'Not Started']] as const).map(([key, label]) => (
            <button
              key={key}
              onClick={() => setFilter(key)}
              className={`px-3 py-1.5 rounded-md text-xs font-semibold transition-colors whitespace-nowrap ${
                filter === key
                  ? 'bg-indigo-600 text-white'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              {label}
            </button>
          ))}
        </div>

        {/* Sets grid */}
        {filteredSets.length === 0 ? (
          <div className="text-center py-16 text-gray-400 text-sm">No sets match this filter.</div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {filteredSets.map(set => {
              const stats = statsMap.get(set.id) || { attempted: 0, correct: 0, total: set.questions.length };
              const isStarted = stats.attempted > 0;
              const isDone = stats.attempted === stats.total;
              const pct = Math.round((stats.attempted / stats.total) * 100);
              const scorePct = stats.attempted > 0 ? Math.round((stats.correct / stats.total) * 100) : 0;
              const wrongCount = wrongBySet.get(set.id) || 0;

              return (
                <div key={set.id} className="bg-white border border-gray-200 rounded-xl p-4 flex flex-col gap-3 hover:border-green-300 hover:shadow-sm transition-all">
                  {/* Set header */}
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex items-center gap-2 min-w-0">
                      <FileText className="size-4 text-green-600 flex-shrink-0" />
                      <span className="text-sm font-semibold text-gray-900 truncate">{set.title}</span>
                    </div>
                    {isDone && <span className="text-xs font-semibold text-green-700 bg-green-50 border border-green-200 px-2 py-0.5 rounded-full flex-shrink-0">✓ Done</span>}
                  </div>

                  {/* Progress */}
                  {isStarted && (
                    <div>
                      <div className="flex justify-between text-xs text-gray-400 mb-1">
                        <span>{stats.attempted}/{stats.total} answered</span>
                        <span className={scorePct >= 70 ? 'text-green-600 font-semibold' : scorePct >= 50 ? 'text-amber-600 font-semibold' : 'text-red-500 font-semibold'}>{scorePct}%</span>
                      </div>
                      <div className="w-full bg-gray-100 rounded-full h-1.5">
                        <div className="bg-green-500 h-1.5 rounded-full transition-all" style={{ width: `${pct}%` }} />
                      </div>
                    </div>
                  )}
                  {!isStarted && (
                    <p className="text-xs text-gray-400">{set.questions.length} questions</p>
                  )}

                  {/* Actions */}
                  <div className="flex flex-col gap-1.5 mt-auto">
                    <Link to={`/ramd/${set.id}`}>
                      <Button className="w-full bg-green-600 hover:bg-green-700 h-9 text-sm gap-1.5">
                        {isStarted ? <><RefreshCw className="size-3.5" />{isDone ? 'Review' : 'Continue'}</> : <><PlayCircle className="size-3.5" />Start</>}
                      </Button>
                    </Link>
                    {wrongCount > 0 && (
                      <AlertDialog>
                        <AlertDialogTrigger asChild>
                          <Button variant="outline" size="sm" className="w-full h-8 text-xs text-amber-700 border-amber-200 hover:bg-amber-50 gap-1">
                            <RotateCcw className="size-3" /> Reset {wrongCount} wrong
                          </Button>
                        </AlertDialogTrigger>
                        <AlertDialogContent>
                          <AlertDialogHeader>
                            <AlertDialogTitle>Reset wrong answers for {set.title}?</AlertDialogTitle>
                            <AlertDialogDescription>Clears only incorrect answers, keeping correct ones. Cannot be undone.</AlertDialogDescription>
                          </AlertDialogHeader>
                          <AlertDialogFooter>
                            <AlertDialogCancel>Cancel</AlertDialogCancel>
                            <AlertDialogAction
                              onClick={async () => { await clearWrongAnswersForSet(set.id + 2000, set.questions); setRefreshKey(k => k + 1); }}
                              className="bg-amber-600 hover:bg-amber-700"
                            >Reset Wrong Answers</AlertDialogAction>
                          </AlertDialogFooter>
                        </AlertDialogContent>
                      </AlertDialog>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
