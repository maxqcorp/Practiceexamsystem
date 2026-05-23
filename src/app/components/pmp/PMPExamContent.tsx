import { useState, useRef, useCallback, useEffect } from 'react';
import './pmp-exam.css';
import { Question } from '../../data/questions';
import { TextAnnotation, ExamConfig } from './PMPExam';

const HIGHLIGHT_COLORS = [
  { name: 'Yellow', color: '#FEF08A' },
  { name: 'Green',  color: '#86EFAC' },
  { name: 'Blue',   color: '#93C5FD' },
  { name: 'Pink',   color: '#F9A8D4' },
  { name: 'Orange', color: '#FCA5A1' },
];

interface Props {
  currentQuestion: Question | undefined;
  questions: Question[];
  currentQuestionIndex: number;
  totalInSet: number;
  globalQuestionNum: number;
  currentSet: number;
  config: ExamConfig;
  answers: Record<number, number>;
  flags: number[];
  comments: Record<number, string>;
  annotations: Record<string, TextAnnotation[]>;
  activeTool: string;
  highlightColor: string;
  remainingTime: number;
  userName: string;
  lastQuestionAnswered: boolean;
  onAnswer: (questionId: number, optionIndex: number) => void;
  onFlagToggle: (questionId: number) => void;
  onCommentChange: (questionId: number, comment: string) => void;
  onNext: () => void;
  onPrevious: () => void;
  onGoToQuestion: (index: number) => void;
  onReview: () => void;
  onAddAnnotation: (questionId: number, annotation: TextAnnotation) => void;
  onActiveToolChange: (tool: 'none' | 'strikethrough' | 'highlight') => void;
  onHighlightColorChange: (color: string) => void;
}

function formatTime(seconds: number): string {
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = seconds % 60;
  if (h > 0) return `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

function renderAnnotatedText(text: string, anns: TextAnnotation[]) {
  if (!anns || anns.length === 0) return text;
  const sorted = [...anns].sort((a, b) => a.start - b.start);
  const parts: React.ReactNode[] = [];
  let lastEnd = 0;
  for (const ann of sorted) {
    if (ann.start > lastEnd) parts.push(text.slice(lastEnd, ann.start));
    if (ann.start < text.length && ann.end <= text.length) {
      const seg = text.slice(ann.start, ann.end);
      parts.push(
        ann.type === 'highlight'
          ? <mark key={ann.id} style={{ backgroundColor: ann.color || '#FEF08A', padding: '1px 0' }}>{seg}</mark>
          : <span key={ann.id} style={{ textDecoration: 'line-through', textDecorationThickness: '2px' }}>{seg}</span>
      );
    }
    lastEnd = ann.end;
  }
  if (lastEnd < text.length) parts.push(text.slice(lastEnd));
  return parts;
}

export default function PMPExamContent(props: Props) {
  const {
    currentQuestion, questions, globalQuestionNum, currentSet, config,
    answers, flags, comments, annotations, activeTool, highlightColor,
    remainingTime, userName, lastQuestionAnswered, currentQuestionIndex, totalInSet,
    onAnswer, onFlagToggle, onCommentChange, onNext, onPrevious,
    onGoToQuestion, onReview, onAddAnnotation, onActiveToolChange, onHighlightColorChange,
  } = props;

  const [showNavigator, setShowNavigator] = useState(false);
  const [showCalculator, setShowCalculator] = useState(false);
  const [showComment, setShowComment] = useState(false);
  const [showHighlightPicker, setShowHighlightPicker] = useState(false);
  const [commentText, setCommentText] = useState('');
  const questionTextRef = useRef<HTMLDivElement>(null);
  const pickerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (currentQuestion) setCommentText(comments[currentQuestion.id] || '');
  }, [currentQuestion?.id, comments]);

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (pickerRef.current && !pickerRef.current.contains(e.target as Node)) {
        setShowHighlightPicker(false);
      }
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  const handleTextMouseUp = useCallback(() => {
    if (activeTool === 'none' || !currentQuestion) return;
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed) return;
    const range = sel.getRangeAt(0);
    const text = range.toString();
    if (!text.trim()) return;
    const container = questionTextRef.current;
    if (!container) return;
    const preCaretRange = range.cloneRange();
    preCaretRange.selectNodeContents(container);
    preCaretRange.setEnd(range.startContainer, range.startOffset);
    const start = preCaretRange.toString().length;
    onAddAnnotation(currentQuestion.id, {
      id: `ann_${Date.now()}`,
      start,
      end: start + text.length,
      type: activeTool as 'highlight' | 'strikethrough',
      color: activeTool === 'highlight' ? highlightColor : undefined,
    });
    sel.removeAllRanges();
    onActiveToolChange('none');
  }, [activeTool, highlightColor, currentQuestion, onAddAnnotation, onActiveToolChange]);

  if (!currentQuestion) {
    return (
      <div className="exam-container" style={{ alignItems: 'center', justifyContent: 'center' }}>
        <p style={{ color: '#94a3b8', fontSize: '18px' }}>No questions available.</p>
      </div>
    );
  }

  const selectedAnswer = answers[currentQuestion.id];
  const isFlagged = flags.includes(currentQuestion.id);
  const questionAnns = annotations[String(currentQuestion.id)] || [];
  const startNum = currentSet * config.perSet + 1;
  const isTimeLow = remainingTime < 600;

  return (
    <div className="exam-container">

      {/* ── HEADER ── */}
      <div className="exam-header">
        <span className="exam-header-badge">PMP</span>
        <h1>PROJECT MANAGEMENT PROFESSIONAL EXAMINATION</h1>
        <span className="exam-header-candidate">{userName}</span>
      </div>

      {/* ── TOOLBAR ── */}
      <div className="exam-toolbar">
        <div className="toolbar-left">
          <button
            className="tool-btn"
            onClick={() => setShowComment(true)}
            title="Add a note to this question"
          >
            ✎ Note
          </button>

          <button
            className={`tool-btn ${activeTool === 'strikethrough' ? 'active' : ''}`}
            onClick={() => onActiveToolChange(activeTool === 'strikethrough' ? 'none' : 'strikethrough')}
            title="Select text to strikethrough"
          >
            {activeTool === 'strikethrough' ? '✓ ' : ''}Strikethrough
          </button>

          <div style={{ position: 'relative' }} ref={pickerRef}>
            <button
              className={`tool-btn ${activeTool === 'highlight' ? 'active' : ''}`}
              onClick={() => setShowHighlightPicker(v => !v)}
              title="Highlight selected text"
            >
              <span style={{
                display: 'inline-block', width: '10px', height: '10px',
                background: highlightColor, borderRadius: '2px', border: '1px solid rgba(255,255,255,0.3)'
              }} />
              {activeTool === 'highlight' ? '✓ ' : ''}Highlight
            </button>

            {showHighlightPicker && (
              <div className="highlight-picker">
                <div className="highlight-picker-label">Colour</div>
                <div className="highlight-colors">
                  {HIGHLIGHT_COLORS.map(c => (
                    <button
                      key={c.color}
                      className={`highlight-color-swatch ${highlightColor === c.color ? 'selected' : ''}`}
                      style={{ background: c.color }}
                      onClick={() => onHighlightColorChange(c.color)}
                      title={c.name}
                    />
                  ))}
                </div>
                <button
                  className={`highlight-activate-btn ${activeTool === 'highlight' ? 'active' : ''}`}
                  onClick={() => {
                    onActiveToolChange(activeTool === 'highlight' ? 'none' : 'highlight');
                    setShowHighlightPicker(false);
                  }}
                >
                  {activeTool === 'highlight' ? 'Deactivate' : 'Activate Highlight'}
                </button>
              </div>
            )}
          </div>

          <div className="toolbar-sep" />

          <button
            className="tool-btn"
            onClick={() => setShowCalculator(true)}
            title="Open calculator"
          >
            ⊞ Calculator
          </button>
        </div>

        <div className="toolbar-right">
          <div className={`status-timer ${isTimeLow ? 'warning' : ''}`}>
            ⏱ {formatTime(remainingTime)}
          </div>
          <div className="status-counter">
            <strong>{globalQuestionNum}</strong>&nbsp;/ {config.totalQuestions}
          </div>
          <button
            className={`flag-btn ${isFlagged ? 'flagged' : ''}`}
            onClick={() => onFlagToggle(currentQuestion.id)}
          >
            {isFlagged ? '⚑ Flagged' : '⚐ Flag'}
          </button>
        </div>
      </div>

      {/* ── QUESTION PANEL ── */}
      <div
        className="question-panel"
        onMouseUp={handleTextMouseUp}
        style={{ cursor: activeTool !== 'none' ? 'text' : undefined }}
      >
        <div className="question-content">
          <div className="question-meta">
            <span>Set {currentSet + 1} of 3</span>
            <span className="question-meta-dot" />
            <span>Question {currentQuestionIndex + 1} of {totalInSet}</span>
            {isFlagged && (
              <>
                <span className="question-meta-dot" />
                <span className="question-meta-flag">⚑ Flagged for Review</span>
              </>
            )}
          </div>

          <div
            ref={questionTextRef}
            className="question-text"
            style={{ userSelect: activeTool !== 'none' ? 'text' : undefined }}
          >
            {renderAnnotatedText(currentQuestion.question, questionAnns)}
          </div>

          <div>
            {currentQuestion.options.map((option, idx) => {
              const isSelected = selectedAnswer === idx;
              return (
                <button
                  key={idx}
                  className={`option-btn ${isSelected ? 'selected' : ''}`}
                  onClick={() => onAnswer(currentQuestion.id, idx)}
                >
                  <span className="option-label">{String.fromCharCode(65 + idx)}</span>
                  <span className="option-text">
                    {renderAnnotatedText(option, questionAnns)}
                  </span>
                </button>
              );
            })}
          </div>

          {comments[currentQuestion.id] && (
            <div className="remark-display">
              <strong>Note:</strong> {comments[currentQuestion.id]}
            </div>
          )}
        </div>
      </div>

      {/* ── FOOTER ── */}
      <div className="exam-footer">
        <button
          className="nav-btn"
          onClick={onPrevious}
          disabled={currentQuestionIndex === 0}
        >
          ← Previous
        </button>
        <button
          className="nav-btn nav-btn-navigator"
          onClick={() => setShowNavigator(true)}
        >
          ⊞ Navigator
        </button>
        <div className="nav-spacer" />
        {lastQuestionAnswered && (
          <button className="review-question-btn" onClick={onReview}>
            Review & Submit →
          </button>
        )}
        <button
          className="nav-btn"
          onClick={onNext}
          disabled={currentQuestionIndex >= totalInSet - 1}
        >
          Next →
        </button>
      </div>

      {/* ── NAVIGATOR MODAL ── */}
      {showNavigator && (
        <div className="modal-overlay" onClick={() => setShowNavigator(false)}>
          <div className="modal-box" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <span className="modal-title">Question Navigator — Set {currentSet + 1}</span>
              <button className="modal-close" onClick={() => setShowNavigator(false)}>✕</button>
            </div>
            <div className="modal-body">
              <div className="nav-legend">
                <div className="nav-legend-item">
                  <div className="nav-legend-swatch" style={{ background: '#1d4ed8' }} />
                  Current
                </div>
                <div className="nav-legend-item">
                  <div className="nav-legend-swatch" style={{ background: '#dcfce7', border: '1px solid #4ade80' }} />
                  Answered
                </div>
                <div className="nav-legend-item">
                  <div className="nav-legend-swatch" style={{ background: '#fef9c3', border: '1px solid #facc15' }} />
                  Flagged
                </div>
                <div className="nav-legend-item">
                  <div className="nav-legend-swatch" style={{ background: '#fff', border: '1px solid #d0d7de' }} />
                  Unanswered
                </div>
              </div>
              <div className="question-grid">
                {questions.map((q, idx) => {
                  const isAnswered = answers[q.id] !== undefined;
                  const isFlag = flags.includes(q.id);
                  const isCurrent = idx === currentQuestionIndex;
                  let cls = 'question-grid-btn';
                  if (isCurrent) cls += ' current';
                  else if (isFlag) cls += ' flagged';
                  else if (isAnswered) cls += ' answered';
                  return (
                    <button
                      key={q.id}
                      className={cls}
                      onClick={() => { onGoToQuestion(idx); setShowNavigator(false); }}
                    >
                      {startNum + idx}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ── COMMENT MODAL ── */}
      {showComment && (
        <div className="modal-overlay" onClick={() => setShowComment(false)}>
          <div className="modal-box" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <span className="modal-title">Note — Question {globalQuestionNum}</span>
              <button
                className="modal-close"
                onClick={() => {
                  setShowComment(false);
                  setCommentText(comments[currentQuestion.id] || '');
                }}
              >✕</button>
            </div>
            <div className="modal-body">
              <textarea
                style={{
                  width: '100%', minHeight: '120px', padding: '10px 12px',
                  border: '1px solid #d1d5db', borderRadius: '3px',
                  fontSize: '14px', lineHeight: '1.6', resize: 'vertical',
                  fontFamily: 'inherit', color: '#1e293b', outline: 'none',
                }}
                value={commentText}
                onChange={e => setCommentText(e.target.value)}
                placeholder="Write a note about this question…"
                autoFocus
              />
            </div>
            <div className="modal-footer">
              <button
                className="nav-btn"
                style={{ color: '#374151', background: '#f1f5f9', border: '1px solid #d1d5db' }}
                onClick={() => {
                  setShowComment(false);
                  setCommentText(comments[currentQuestion.id] || '');
                }}
              >
                Cancel
              </button>
              <button
                className="submit-btn"
                onClick={() => {
                  onCommentChange(currentQuestion.id, commentText);
                  setShowComment(false);
                }}
              >
                Save Note
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ── CALCULATOR ── */}
      {showCalculator && <CalculatorModal onClose={() => setShowCalculator(false)} />}
    </div>
  );
}

function CalculatorModal({ onClose }: { onClose: () => void }) {
  const [display, setDisplay] = useState('0');
  const [expr, setExpr] = useState('');
  const [prevValue, setPrevValue] = useState<number | null>(null);
  const [operation, setOperation] = useState<string | null>(null);
  const [waitingForOperand, setWaitingForOperand] = useState(false);

  const inputDigit = (d: string) => {
    if (waitingForOperand) { setDisplay(d); setWaitingForOperand(false); }
    else setDisplay(display === '0' ? d : display + d);
  };

  const inputDecimal = () => {
    if (waitingForOperand) { setDisplay('0.'); setWaitingForOperand(false); return; }
    if (!display.includes('.')) setDisplay(display + '.');
  };

  const clear = () => {
    setDisplay('0'); setPrevValue(null); setOperation(null);
    setWaitingForOperand(false); setExpr('');
  };

  const compute = (a: number, b: number, op: string) => {
    switch (op) {
      case '+': return a + b;
      case '−': return a - b;
      case '×': return a * b;
      case '÷': return b !== 0 ? a / b : 0;
      default: return b;
    }
  };

  const performOp = (nextOp: string) => {
    const current = parseFloat(display);
    if (prevValue === null) {
      setPrevValue(current);
      setExpr(`${current} ${nextOp}`);
    } else if (operation) {
      const result = compute(prevValue, current, operation);
      const r = parseFloat(result.toPrecision(10));
      setDisplay(String(r));
      setPrevValue(r);
      setExpr(`${r} ${nextOp}`);
    }
    setOperation(nextOp);
    setWaitingForOperand(true);
  };

  const handleEquals = () => {
    const current = parseFloat(display);
    if (prevValue !== null && operation) {
      const result = compute(prevValue, current, operation);
      const r = parseFloat(result.toPrecision(10));
      setDisplay(String(r));
      setExpr('');
      setPrevValue(null);
      setOperation(null);
      setWaitingForOperand(true);
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-box modal-box-sm" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <span className="modal-title">Calculator</span>
          <button className="modal-close" onClick={onClose}>✕</button>
        </div>
        <div className="modal-body" style={{ padding: '12px' }}>
          <div className="calculator-display">
            <div className="calculator-expr">{expr || ' '}</div>
            <div className="calculator-value">{display}</div>
          </div>
          <div className="calculator-grid">
            <button className="clear-btn" onClick={clear}>C</button>
            <button className="op-btn" onClick={() => performOp('÷')}>÷</button>
            <button className="op-btn" onClick={() => performOp('×')}>×</button>
            <button className="op-btn" onClick={() => performOp('−')}>−</button>
            <button onClick={() => inputDigit('7')}>7</button>
            <button onClick={() => inputDigit('8')}>8</button>
            <button onClick={() => inputDigit('9')}>9</button>
            <button className="op-btn" style={{ gridRow: 'span 2' }} onClick={() => performOp('+')}>+</button>
            <button onClick={() => inputDigit('4')}>4</button>
            <button onClick={() => inputDigit('5')}>5</button>
            <button onClick={() => inputDigit('6')}>6</button>
            <button onClick={() => inputDigit('1')}>1</button>
            <button onClick={() => inputDigit('2')}>2</button>
            <button onClick={() => inputDigit('3')}>3</button>
            <button className="equals-btn" style={{ gridRow: 'span 2' }} onClick={handleEquals}>=</button>
            <button style={{ gridColumn: 'span 2' }} onClick={() => inputDigit('0')}>0</button>
            <button onClick={inputDecimal}>.</button>
          </div>
        </div>
      </div>
    </div>
  );
}
