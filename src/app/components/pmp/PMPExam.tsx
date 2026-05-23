import { useState, useEffect, useMemo, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { examSets } from '../../data/questions';
import { useAuth } from '../../contexts/AuthContext';
import PMPExamContent from './PMPExamContent';
import PMPReview from './PMPReview';
import PMPResult from './PMPResult';
import { Coffee, Play } from 'lucide-react';

export interface TextAnnotation {
  id: string;
  start: number;
  end: number;
  type: 'highlight' | 'strikethrough';
  color?: string;
}

export interface ExamConfig {
  totalQuestions: number;
  perSet: number;
  totalTime: number;
  label: string;
}

const FULL_CONFIG: ExamConfig = { totalQuestions: 180, perSet: 60, totalTime: 14400, label: 'Full Exam' };
const QUICK_CONFIG: ExamConfig = { totalQuestions: 60, perSet: 20, totalTime: 4800, label: 'Quick Exam' };

export default function PMPExam() {
  const { mode } = useParams<{ mode: string }>();
  const navigate = useNavigate();
  const { user } = useAuth();
  const isFull = mode === 'full';
  const config = isFull ? FULL_CONFIG : QUICK_CONFIG;

  useEffect(() => {
    if (mode !== 'full' && mode !== 'quick') {
      navigate('/pmp-simulation', { replace: true });
    }
  }, [mode, navigate]);

  const allQuestions = useMemo(() => {
    const all = examSets.flatMap(s => s.questions);
    return all.slice(0, config.totalQuestions);
  }, [config.totalQuestions]);

  const sets = useMemo(() => [
    allQuestions.slice(0, config.perSet),
    allQuestions.slice(config.perSet, config.perSet * 2),
    allQuestions.slice(config.perSet * 2, config.perSet * 3),
  ], [allQuestions, config.perSet]);

  const [phase, setPhase] = useState<'exam' | 'review' | 'post-submit' | 'break' | 'results'>('exam');
  const [currentSet, setCurrentSet] = useState(0);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [flags, setFlags] = useState<number[]>([]);
  const [comments, setComments] = useState<Record<number, string>>({});
  const [remainingTime, setRemainingTime] = useState(config.totalTime);
  const [isBreakActive, setIsBreakActive] = useState(false);
  const [breakElapsed, setBreakElapsed] = useState(0);
  const [annotations, setAnnotations] = useState<Record<string, TextAnnotation[]>>({});
  const [activeTool, setActiveTool] = useState<'none' | 'strikethrough' | 'highlight'>('none');
  const [highlightColor, setHighlightColor] = useState('#FFEB3B');

  useEffect(() => {
    if (phase === 'results' || isBreakActive) return;
    const interval = setInterval(() => {
      setRemainingTime(prev => Math.max(0, prev - 1));
    }, 1000);
    return () => clearInterval(interval);
  }, [phase, isBreakActive]);

  useEffect(() => {
    if (!isBreakActive) return;
    const interval = setInterval(() => {
      setBreakElapsed(prev => {
        const next = prev + 1;
        if (next >= 600) {
          setIsBreakActive(false);
          return 600;
        }
        return next;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [isBreakActive]);

  useEffect(() => {
    if (!isBreakActive && breakElapsed > 0 && phase === 'break') {
      setPhase('exam');
      setCurrentSet(prev => prev + 1);
      setCurrentQuestionIndex(0);
      setBreakElapsed(0);
    }
  }, [isBreakActive, breakElapsed, phase]);

  const currentQuestions = sets[currentSet] || [];
  const totalInSet = currentQuestions.length;
  const currentQuestion = currentQuestions[currentQuestionIndex];
  const globalQuestionNum = currentSet * config.perSet + currentQuestionIndex + 1;
  const isLastQuestionOfSet = currentQuestionIndex === totalInSet - 1;
  const lastQuestionAnswered = isLastQuestionOfSet && currentQuestion && answers[currentQuestion.id] !== undefined;

  const handleAnswer = useCallback((questionId: number, optionIndex: number) => {
    setAnswers(prev => ({ ...prev, [questionId]: optionIndex }));
  }, []);

  const handleFlagToggle = useCallback((questionId: number) => {
    setFlags(prev => {
      if (prev.includes(questionId)) return prev.filter(id => id !== questionId);
      return [...prev, questionId];
    });
  }, []);

  const handleCommentChange = useCallback((questionId: number, comment: string) => {
    setComments(prev => ({ ...prev, [questionId]: comment }));
  }, []);

  const handleNext = useCallback(() => {
    if (currentQuestionIndex < totalInSet - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
    }
  }, [currentQuestionIndex, totalInSet]);

  const handlePrevious = useCallback(() => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prev => prev - 1);
    }
  }, [currentQuestionIndex]);

  const handleGoToQuestion = useCallback((index: number) => {
    setCurrentQuestionIndex(index);
  }, []);

  const handleReview = useCallback(() => {
    setPhase('review');
  }, []);

  const handleSubmitReview = useCallback(() => {
    if (currentSet >= 2) {
      setPhase('results');
    } else {
      setPhase('post-submit');
    }
  }, [currentSet]);

  const handleStartBreak = useCallback(() => {
    setPhase('break');
    setIsBreakActive(true);
    setBreakElapsed(0);
  }, []);

  const handleResume = useCallback(() => {
    setPhase('exam');
    setCurrentSet(prev => prev + 1);
    setCurrentQuestionIndex(0);
    setIsBreakActive(false);
    setBreakElapsed(0);
  }, []);

  const handleAddAnnotation = useCallback((questionId: number, annotation: TextAnnotation) => {
    const key = String(questionId);
    setAnnotations(prev => ({
      ...prev,
      [key]: [...(prev[key] || []), annotation],
    }));
  }, []);

  if (phase === 'review') {
    return (
      <PMPReview
        questions={currentQuestions}
        answers={answers}
        flags={flags}
        comments={comments}
        currentSet={currentSet}
        config={config}
        onBack={() => setPhase('exam')}
        onSubmit={handleSubmitReview}
      />
    );
  }

  if (phase === 'post-submit') {
    return (
      <div style={{
        width: '100%', minHeight: '100vh', background: '#f8fafc',
        display: 'flex', flexDirection: 'column',
        fontFamily: "'Segoe UI', system-ui, sans-serif",
      }}>
        <div style={{
          height: '52px', background: '#1d4ed8',
          display: 'flex', alignItems: 'center', padding: '0 20px', gap: '14px', flexShrink: 0,
        }}>
          <span style={{ background: 'rgba(255,255,255,0.2)', color: '#fff', fontSize: '10.5px', fontWeight: 800, padding: '3px 9px', borderRadius: '3px', letterSpacing: '0.12em' }}>PMP</span>
          <span style={{ color: '#fff', fontSize: '13.5px', fontWeight: 600 }}>PROJECT MANAGEMENT PROFESSIONAL EXAMINATION</span>
        </div>
        <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{
            background: '#fff', border: '1px solid #e2e8f0',
            borderRadius: '8px', padding: '40px 48px',
            maxWidth: '460px', width: '100%', textAlign: 'center',
            boxShadow: '0 4px 24px rgba(0,0,0,0.07)',
          }}>
            <div style={{
              width: '52px', height: '52px', background: '#dcfce7', borderRadius: '50%',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              margin: '0 auto 16px', fontSize: '22px',
            }}>✓</div>
            <p style={{ fontSize: '20px', fontWeight: 700, color: '#111827', margin: '0 0 6px 0' }}>
              Set {currentSet + 1} Complete
            </p>
            <p style={{ fontSize: '14px', color: '#64748b', margin: '0 0 28px 0', lineHeight: '1.6' }}>
              {currentSet + 1} of 3 sets finished. Take a break or continue to the next set.
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <button
                onClick={handleStartBreak}
                style={{
                  background: '#fff', color: '#374151',
                  border: '1px solid #e2e8f0',
                  borderRadius: '6px', height: '44px', fontSize: '14px', fontWeight: 500,
                  cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
                  fontFamily: 'inherit',
                }}
              >
                <Coffee className="size-4" /> Start 10-Minute Break
              </button>
              <button
                onClick={handleResume}
                style={{
                  background: '#1d4ed8', color: '#fff', border: 'none',
                  borderRadius: '6px', height: '44px', fontSize: '14px', fontWeight: 600,
                  cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
                  fontFamily: 'inherit',
                }}
              >
                <Play className="size-4" /> Continue to Set {currentSet + 2}
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (phase === 'break') {
    const breakRemaining = Math.max(0, 600 - breakElapsed);
    const minutes = Math.floor(breakRemaining / 60);
    const seconds = breakRemaining % 60;
    const pct = (breakElapsed / 600) * 100;
    return (
      <div style={{
        width: '100%', minHeight: '100vh', background: '#f8fafc',
        display: 'flex', flexDirection: 'column',
        fontFamily: "'Segoe UI', system-ui, sans-serif",
      }}>
        <div style={{
          height: '52px', background: '#1d4ed8',
          display: 'flex', alignItems: 'center', padding: '0 20px', gap: '14px', flexShrink: 0,
        }}>
          <span style={{ background: 'rgba(255,255,255,0.2)', color: '#fff', fontSize: '10.5px', fontWeight: 800, padding: '3px 9px', borderRadius: '3px', letterSpacing: '0.12em' }}>PMP</span>
          <span style={{ color: '#fff', fontSize: '13.5px', fontWeight: 600 }}>PROJECT MANAGEMENT PROFESSIONAL EXAMINATION</span>
        </div>
        <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{
            background: '#fff', border: '1px solid #e2e8f0',
            borderRadius: '8px', padding: '40px 48px',
            maxWidth: '420px', width: '100%', textAlign: 'center',
            boxShadow: '0 4px 24px rgba(0,0,0,0.07)',
          }}>
            <Coffee style={{ margin: '0 auto 14px', display: 'block', color: '#1d4ed8' }} size={36} />
            <p style={{ fontSize: '20px', fontWeight: 700, color: '#111827', margin: '0 0 6px 0' }}>
              Break Time
            </p>
            <p style={{ fontSize: '34px', fontWeight: 800, color: '#1d4ed8', margin: '0 0 20px 0', fontFamily: 'Consolas, monospace', letterSpacing: '0.05em' }}>
              {String(minutes).padStart(2, '0')}:{String(seconds).padStart(2, '0')}
            </p>
            <div style={{ height: '6px', background: '#f1f5f9', borderRadius: '3px', overflow: 'hidden', marginBottom: '24px' }}>
              <div style={{
                height: '100%', background: '#1d4ed8', borderRadius: '3px',
                width: `${pct}%`, transition: 'width 1s linear',
              }} />
            </div>
            <button
              onClick={handleResume}
              style={{
                background: '#1d4ed8', color: '#fff', border: 'none',
                borderRadius: '6px', height: '42px', fontSize: '14px', fontWeight: 600,
                cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                gap: '8px', width: '100%', fontFamily: 'inherit',
              }}
            >
              <Play size={15} /> Resume Now
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (phase === 'results') {
    return (
      <PMPResult
        allQuestions={allQuestions}
        sets={sets}
        answers={answers}
        flags={flags}
        remainingTime={remainingTime}
        config={config}
        userName={user?.name || 'Candidate'}
        onRestart={() => navigate('/pmp-simulation')}
      />
    );
  }

  return (
    <PMPExamContent
      currentQuestion={currentQuestion}
      questions={currentQuestions}
      currentQuestionIndex={currentQuestionIndex}
      totalInSet={totalInSet}
      globalQuestionNum={globalQuestionNum}
      currentSet={currentSet}
      config={config}
      answers={answers}
      flags={flags}
      comments={comments}
      annotations={annotations}
      activeTool={activeTool}
      highlightColor={highlightColor}
      remainingTime={remainingTime}
      userName={user?.name || 'Candidate'}
      lastQuestionAnswered={lastQuestionAnswered}
      onAnswer={handleAnswer}
      onFlagToggle={handleFlagToggle}
      onCommentChange={handleCommentChange}
      onNext={handleNext}
      onPrevious={handlePrevious}
      onGoToQuestion={handleGoToQuestion}
      onReview={handleReview}
      onAddAnnotation={handleAddAnnotation}
      onActiveToolChange={setActiveTool}
      onHighlightColorChange={setHighlightColor}
    />
  );
}
