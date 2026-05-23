import { useState, useEffect, useMemo, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { examSets } from '../../data/questions';
import { useAuth } from '../../contexts/AuthContext';
import PMPExamContent from './PMPExamContent';
import PMPReview from './PMPReview';
import { Coffee, Play, CheckCircle } from 'lucide-react';

export interface TextAnnotation {
  id: string;
  start: number;
  end: number;
  type: 'highlight' | 'strikethrough';
  color?: string;
  targetId?: string; // 'question' | 'opt_0' | 'opt_1' | 'opt_2' | 'opt_3'
}

export interface ExamConfig {
  totalQuestions: number;
  perSet: number;
  totalTime: number;
  label: string;
}

const FULL_CONFIG: ExamConfig = { totalQuestions: 180, perSet: 60, totalTime: 14400, label: 'Full Exam' };
const QUICK_CONFIG: ExamConfig = { totalQuestions: 60, perSet: 20, totalTime: 4800, label: 'Quick Exam' };

function QuitConfirmModal({ onCancel, onConfirm }: { onCancel: () => void; onConfirm: () => void }) {
  return (
    <div className="modal-overlay" onClick={onCancel}>
      <div className="modal-box modal-box-sm" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <span className="modal-title">Quit Simulation?</span>
          <button className="modal-close" onClick={onCancel}>✕</button>
        </div>
        <div className="modal-body">
          <p style={{ margin: '0 0 10px', fontSize: '14.5px', color: '#1e293b', fontWeight: 600 }}>
            Are you sure you want to quit?
          </p>
          <p style={{ margin: 0, fontSize: '13.5px', color: '#475569', lineHeight: '1.6' }}>
            Your progress will be lost and you will be returned to the simulation selection screen.
          </p>
        </div>
        <div className="modal-footer">
          <button
            className="nav-btn"
            style={{ color: '#374151', background: '#f1f5f9', border: '1px solid #d1d5db' }}
            onClick={onCancel}
          >
            Cancel
          </button>
          <button className="submit-btn danger" onClick={onConfirm}>
            Yes, Quit
          </button>
        </div>
      </div>
    </div>
  );
}

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

  const [phase, setPhase] = useState<'exam' | 'review' | 'post-submit' | 'break' | 'completed'>('exam');
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
  const [showQuit, setShowQuit] = useState(false);

  const handleQuit = useCallback(() => navigate('/pmp-simulation'), [navigate]);

  useEffect(() => {
    if (phase === 'completed' || isBreakActive) return;
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
  const lastQuestionAnswered = isLastQuestionOfSet;

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
      setPhase('completed');
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

  const sharedHeader = (
    <div className="exam-header" style={{ flexShrink: 0 }}>
      <span className="exam-header-badge">PMP</span>
      <h1>PROJECT MANAGEMENT PROFESSIONAL EXAMINATION</h1>
      <button
        onClick={() => setShowQuit(true)}
        style={{
          height: '30px', padding: '0 14px',
          background: 'rgba(255,255,255,0.12)',
          border: '1px solid rgba(255,255,255,0.25)', borderRadius: '4px',
          color: 'rgba(255,255,255,0.85)', fontSize: '12.5px', cursor: 'pointer',
          fontFamily: 'inherit', fontWeight: 500, flexShrink: 0, whiteSpace: 'nowrap',
        }}
      >
        Quit
      </button>
    </div>
  );

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
        onQuit={handleQuit}
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
        {sharedHeader}
        <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{
            background: '#fff', border: '1px solid #e2e8f0',
            borderRadius: '8px', padding: 'clamp(20px, 5vw, 48px)',
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
                  background: '#fff', color: '#374151', border: '1px solid #e2e8f0',
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
        {showQuit && <QuitConfirmModal onCancel={() => setShowQuit(false)} onConfirm={handleQuit} />}
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
        {sharedHeader}
        <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{
            background: '#fff', border: '1px solid #e2e8f0',
            borderRadius: '8px', padding: 'clamp(20px, 5vw, 48px)',
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
        {showQuit && <QuitConfirmModal onCancel={() => setShowQuit(false)} onConfirm={handleQuit} />}
      </div>
    );
  }

  if (phase === 'completed') {
    return (
      <div style={{
        width: '100%', minHeight: '100vh', background: '#f8fafc',
        display: 'flex', flexDirection: 'column',
        fontFamily: "'Segoe UI', system-ui, sans-serif",
      }}>
        <div className="exam-header" style={{ flexShrink: 0 }}>
          <span className="exam-header-badge">PMP</span>
          <h1>PROJECT MANAGEMENT PROFESSIONAL EXAMINATION</h1>
        </div>
        <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{
            background: '#fff', border: '1px solid #e2e8f0',
            borderRadius: '8px', padding: 'clamp(24px, 5vw, 56px)',
            maxWidth: '500px', width: '100%', textAlign: 'center',
            boxShadow: '0 4px 24px rgba(0,0,0,0.07)',
          }}>
            <CheckCircle size={52} style={{ color: '#16a34a', margin: '0 auto 20px', display: 'block' }} />
            <p style={{ fontSize: '24px', fontWeight: 700, color: '#111827', margin: '0 0 10px 0' }}>
              Simulation Complete
            </p>
            <p style={{ fontSize: '14.5px', color: '#64748b', margin: '0 0 8px 0', lineHeight: '1.7' }}>
              You have completed all 3 sets of the {config.label}.
            </p>
            <p style={{ fontSize: '13.5px', color: '#94a3b8', margin: '0 0 36px 0', lineHeight: '1.6' }}>
              Thank you for completing this practice simulation. Your responses have been recorded.
            </p>
            <button
              onClick={() => navigate('/pmp-simulation')}
              style={{
                background: '#1d4ed8', color: '#fff', border: 'none',
                borderRadius: '6px', height: '44px', fontSize: '14px', fontWeight: 600,
                cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                gap: '8px', width: '100%', fontFamily: 'inherit',
              }}
            >
              ← Back to Simulation Centre
            </button>
          </div>
        </div>
      </div>
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
      onQuit={handleQuit}
    />
  );
}
