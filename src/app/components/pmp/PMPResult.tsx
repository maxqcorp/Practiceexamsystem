import { useState } from 'react';
import { Question } from '../../data/questions';
import { ExamConfig } from './PMPExam';
import './pmp-exam.css';

interface Props {
  allQuestions: Question[];
  sets: Question[][];
  answers: Record<number, number>;
  flags: number[];
  remainingTime: number;
  config: ExamConfig;
  userName: string;
  onRestart: () => void;
}

function formatDuration(seconds: number): string {
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = seconds % 60;
  if (h > 0) return `${h}h ${m}m ${s}s`;
  return `${m}m ${s}s`;
}

export default function PMPResult({
  allQuestions, sets, answers, flags, remainingTime, config, userName, onRestart
}: Props) {
  const [reviewFilter, setReviewFilter] = useState<'incorrect' | 'correct' | 'all'>('incorrect');

  const total = allQuestions.length;
  const answered = allQuestions.filter(q => answers[q.id] !== undefined).length;
  const correct = allQuestions.filter(q => answers[q.id] !== undefined && answers[q.id] === q.correctAnswer).length;
  const incorrect = answered - correct;
  const unanswered = total - answered;
  const score = Math.round((correct / total) * 100);
  const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;
  const usedTime = config.totalTime - remainingTime;
  const isPassing = score >= 61;

  const setResults = sets.map((setQs, i) => {
    const c = setQs.filter(q => answers[q.id] !== undefined && answers[q.id] === q.correctAnswer).length;
    return { i, total: setQs.length, correct: c, pct: Math.round((c / setQs.length) * 100) };
  });

  const filteredQs = reviewFilter === 'correct'
    ? allQuestions.filter(q => answers[q.id] !== undefined && answers[q.id] === q.correctAnswer)
    : reviewFilter === 'incorrect'
    ? allQuestions.filter(q => answers[q.id] === undefined || answers[q.id] !== q.correctAnswer)
    : allQuestions;

  return (
    <div style={{
      width: '100%', minHeight: '100vh', background: '#f8fafc',
      display: 'flex', flexDirection: 'column',
      fontFamily: "'Segoe UI', system-ui, sans-serif",
    }}>
      {/* ── HEADER ── */}
      <div className="exam-header" style={{ justifyContent: 'space-between', paddingRight: '20px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <span className="exam-header-badge">PMP</span>
          <h1 style={{ margin: 0 }}>Examination Results</h1>
        </div>
        <span style={{ color: 'rgba(255,255,255,0.75)', fontSize: '12.5px' }}>{userName}</span>
      </div>

      {/* ── CONTENT ── */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '24px 20px' }}>
        <div style={{ maxWidth: '900px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>

          {/* Score card */}
          <div style={{
            background: '#fff',
            border: `1px solid ${isPassing ? '#bbf7d0' : '#fecaca'}`,
            borderTop: `4px solid ${isPassing ? '#22c55e' : '#ef4444'}`,
            borderRadius: '8px', padding: '28px 32px',
            display: 'flex', alignItems: 'center', gap: '32px',
            boxShadow: '0 2px 12px rgba(0,0,0,0.06)',
          }}>
            {/* Big score */}
            <div style={{ textAlign: 'center', flexShrink: 0 }}>
              <div style={{
                fontSize: '64px', fontWeight: 800, lineHeight: 1,
                color: isPassing ? '#16a34a' : '#dc2626',
                fontFamily: "'Segoe UI', system-ui",
              }}>
                {score}%
              </div>
              <div style={{
                fontSize: '12px', fontWeight: 700, marginTop: '8px',
                color: isPassing ? '#16a34a' : '#dc2626',
                letterSpacing: '0.06em', textTransform: 'uppercase',
                background: isPassing ? '#dcfce7' : '#fee2e2',
                padding: '3px 10px', borderRadius: '20px',
              }}>
                {isPassing ? 'Above Target' : 'Below Target'}
              </div>
            </div>

            <div style={{ width: '1px', height: '80px', background: '#e2e8f0', flexShrink: 0 }} />

            {/* Stats */}
            <div style={{ flex: 1, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '16px' }}>
              {[
                { label: 'Correct', value: correct, color: '#16a34a' },
                { label: 'Incorrect', value: incorrect, color: '#dc2626' },
                { label: 'Unanswered', value: unanswered, color: '#94a3b8' },
                { label: 'Accuracy', value: `${accuracy}%`, color: '#1d4ed8' },
                { label: 'Time Used', value: formatDuration(usedTime), color: '#7c3aed' },
                { label: 'Flagged', value: flags.length, color: '#d97706' },
              ].map(s => (
                <div key={s.label}>
                  <div style={{ fontSize: '22px', fontWeight: 700, color: s.color }}>{s.value}</div>
                  <div style={{ fontSize: '11px', color: '#94a3b8', fontWeight: 600, marginTop: '3px', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                    {s.label}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Set breakdown */}
          <div style={{
            background: '#fff', border: '1px solid #e2e8f0',
            borderRadius: '8px', padding: '18px 20px',
            boxShadow: '0 1px 4px rgba(0,0,0,0.04)',
          }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: '#94a3b8', letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: '14px' }}>
              Set Breakdown
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {setResults.map(r => (
                <div key={r.i}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
                    <span style={{ fontSize: '13px', color: '#374151', fontWeight: 500 }}>Set {r.i + 1}</span>
                    <span style={{ fontSize: '13px', fontWeight: 700, color: r.pct >= 61 ? '#16a34a' : '#dc2626' }}>
                      {r.correct}/{r.total} &nbsp;·&nbsp; {r.pct}%
                    </span>
                  </div>
                  <div style={{ height: '6px', background: '#f1f5f9', borderRadius: '3px', overflow: 'hidden' }}>
                    <div style={{
                      height: '100%', borderRadius: '3px',
                      background: r.pct >= 61 ? '#22c55e' : r.pct >= 40 ? '#f59e0b' : '#ef4444',
                      width: `${r.pct}%`, transition: 'width 0.6s ease',
                    }} />
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Question review */}
          <div style={{
            background: '#fff', borderRadius: '8px', overflow: 'hidden',
            border: '1px solid #e2e8f0', boxShadow: '0 1px 4px rgba(0,0,0,0.04)',
          }}>
            {/* Tabs */}
            <div style={{
              display: 'flex', borderBottom: '1px solid #e2e8f0',
              background: '#f8fafc',
            }}>
              {([
                { key: 'incorrect', label: 'Incorrect', count: incorrect + unanswered, color: '#dc2626' },
                { key: 'correct',   label: 'Correct',   count: correct,                 color: '#16a34a' },
                { key: 'all',       label: 'All',        count: total,                   color: '#2563eb' },
              ] as const).map(t => (
                <button
                  key={t.key}
                  onClick={() => setReviewFilter(t.key)}
                  style={{
                    height: '40px', padding: '0 18px', background: 'transparent',
                    border: 'none', borderBottom: reviewFilter === t.key ? `2px solid ${t.color}` : '2px solid transparent',
                    color: reviewFilter === t.key ? t.color : '#64748b',
                    fontSize: '13px', fontWeight: 600, cursor: 'pointer', fontFamily: 'inherit',
                    display: 'flex', alignItems: 'center', gap: '6px',
                  }}
                >
                  {t.label}
                  <span style={{
                    background: reviewFilter === t.key ? t.color : '#e2e8f0',
                    color: reviewFilter === t.key ? '#fff' : '#64748b',
                    borderRadius: '10px', padding: '1px 7px', fontSize: '11px', fontWeight: 700,
                  }}>{t.count}</span>
                </button>
              ))}
            </div>

            {/* Question rows */}
            <div style={{ maxHeight: '420px', overflowY: 'auto' }}>
              {filteredQs.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '32px', color: '#94a3b8', fontSize: '14px' }}>
                  No questions to display.
                </div>
              ) : (
                filteredQs.map(q => {
                  const ans = answers[q.id];
                  const isCorrect = ans !== undefined && ans === q.correctAnswer;
                  return (
                    <div key={q.id} style={{
                      padding: '14px 16px', borderBottom: '1px solid #f1f5f9',
                      background: ans === undefined ? '#fafafa' : isCorrect ? '#f0fdf4' : '#fff5f5',
                      display: 'flex', gap: '12px', alignItems: 'flex-start',
                    }}>
                      {/* Status dot */}
                      <div style={{
                        width: '7px', height: '7px', borderRadius: '50%', flexShrink: 0, marginTop: '6px',
                        background: ans === undefined ? '#94a3b8' : isCorrect ? '#22c55e' : '#ef4444',
                      }} />

                      <div style={{ flex: 1, minWidth: 0 }}>
                        <p style={{ margin: '0 0 8px', fontSize: '13.5px', color: '#1e293b', lineHeight: '1.6' }}>
                          {q.question}
                        </p>
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '3px', marginBottom: '8px' }}>
                          {q.options.map((opt, idx) => {
                            const isCorrectOpt = idx === q.correctAnswer;
                            const isUserOpt = ans === idx;
                            const isWrong = isUserOpt && !isCorrectOpt;
                            return (
                              <div key={idx} style={{
                                fontSize: '12px', padding: '5px 9px',
                                background: isCorrectOpt ? '#dcfce7' : isWrong ? '#fee2e2' : '#f8fafc',
                                border: `1px solid ${isCorrectOpt ? '#86efac' : isWrong ? '#fca5a5' : '#e2e8f0'}`,
                                borderRadius: '2px', color: isCorrectOpt ? '#14532d' : isWrong ? '#7f1d1d' : '#475569',
                                display: 'flex', alignItems: 'center', gap: '5px',
                              }}>
                                <span style={{ fontWeight: 700, flexShrink: 0 }}>{String.fromCharCode(65 + idx)}.</span>
                                {isCorrectOpt && <span style={{ color: '#16a34a' }}>✓</span>}
                                {isWrong && <span style={{ color: '#dc2626' }}>✗</span>}
                                <span>{opt}</span>
                              </div>
                            );
                          })}
                        </div>
                        {q.explanation && (
                          <div style={{
                            padding: '8px 10px', background: '#eff6ff',
                            border: '1px solid #bfdbfe', borderLeft: '3px solid #3b82f6',
                            borderRadius: '2px', fontSize: '12.5px', color: '#1e3a5f', lineHeight: '1.55',
                          }}>
                            <strong>Explanation:</strong> {q.explanation}
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          </div>

          {/* Back button */}
          <div style={{ textAlign: 'center', paddingBottom: '8px' }}>
            <button className="submit-btn" style={{ margin: '0 auto' }} onClick={onRestart}>
              ← Back to Simulation
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
