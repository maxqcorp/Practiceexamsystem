import { useState } from 'react';
import { Question } from '../../data/questions';
import { ExamConfig } from './PMPExam';
import './pmp-exam.css';

interface Props {
  questions: Question[];
  answers: Record<number, number>;
  flags: number[];
  comments: Record<number, string>;
  currentSet: number;
  config: ExamConfig;
  onBack: () => void;
  onSubmit: () => void;
  onQuit: () => void;
}

export default function PMPReview({
  questions, answers, flags, comments, currentSet, config, onBack, onSubmit, onQuit
}: Props) {
  const [activeTab, setActiveTab] = useState<'all' | 'flagged'>('all');
  const [showConfirm, setShowConfirm] = useState(false);
  const [showQuitConfirm, setShowQuitConfirm] = useState(false);

  const flaggedQuestions = questions.filter(q => flags.includes(q.id));
  const totalAnswered = questions.filter(q => answers[q.id] !== undefined).length;
  const unanswered = questions.length - totalAnswered;
  const startNum = currentSet * config.perSet + 1;
  const isLastSet = currentSet >= 2;
  const displayQs = activeTab === 'all' ? questions : flaggedQuestions;

  return (
    <div className="review-container">

      {/* ── HEADER ── */}
      <div className="exam-header" style={{ justifyContent: 'space-between', paddingRight: '20px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <span className="exam-header-badge">PMP</span>
          <h1 style={{ margin: 0 }}>Review — Set {currentSet + 1} of 3</h1>
        </div>
        <div style={{ display: 'flex', gap: '16px', fontSize: '12.5px', alignItems: 'center' }}>
          <span style={{ color: 'rgba(255,255,255,0.9)', fontWeight: 500 }}>{totalAnswered}/{questions.length} answered</span>
          {unanswered > 0 && (
            <span style={{ color: '#fca5a5', fontWeight: 600 }}>{unanswered} unanswered</span>
          )}
          {flaggedQuestions.length > 0 && (
            <span style={{ color: '#fde68a', fontWeight: 500 }}>{flaggedQuestions.length} flagged</span>
          )}
          <button
            onClick={() => setShowQuitConfirm(true)}
            style={{
              height: '30px', padding: '0 14px',
              background: 'rgba(255,255,255,0.12)',
              border: '1px solid rgba(255,255,255,0.25)', borderRadius: '4px',
              color: 'rgba(255,255,255,0.85)', fontSize: '12.5px', cursor: 'pointer',
              fontFamily: 'inherit', fontWeight: 500,
            }}
          >
            Quit
          </button>
        </div>
      </div>

      {/* ── TABS ── */}
      <div className="tab-bar">
        <button
          className={`tab-btn ${activeTab === 'all' ? 'active' : ''}`}
          onClick={() => setActiveTab('all')}
        >
          All Questions
          <span style={{
            background: activeTab === 'all' ? '#dbeafe' : '#f1f5f9',
            color: activeTab === 'all' ? '#1d4ed8' : '#64748b',
            borderRadius: '10px', padding: '1px 7px', fontSize: '11px', fontWeight: 700,
          }}>{questions.length}</span>
        </button>
        <button
          className={`tab-btn ${activeTab === 'flagged' ? 'active' : ''}`}
          onClick={() => setActiveTab('flagged')}
        >
          ⚑ Flagged
          <span style={{
            background: activeTab === 'flagged' ? '#fef9c3' : '#f1f5f9',
            color: activeTab === 'flagged' ? '#b45309' : '#64748b',
            borderRadius: '10px', padding: '1px 7px', fontSize: '11px', fontWeight: 700,
          }}>{flaggedQuestions.length}</span>
        </button>
      </div>

      {/* ── QUESTION LIST ── */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '14px 20px', background: '#f8fafc' }}>
        {displayQs.length === 0 ? (
          <div style={{
            textAlign: 'center', padding: '60px 20px',
            color: '#94a3b8', fontSize: '15px'
          }}>
            <div style={{ fontSize: '32px', marginBottom: '12px' }}>⚑</div>
            No flagged questions in this set.
          </div>
        ) : (
          displayQs.map((q, idx) => {
            const answered = answers[q.id];
            const isFlagged = flags.includes(q.id);
            const hasComment = Boolean(comments[q.id]?.trim());
            const isCorrect = answered !== undefined && answered === q.correctAnswer;
            const qNum = activeTab === 'all'
              ? startNum + idx
              : startNum + questions.indexOf(q);

            return (
              <div
                key={q.id}
                className={`review-question-item ${answered !== undefined ? (isCorrect ? 'correct' : 'incorrect') : ''}`}
              >
                <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
                  {/* Number badge */}
                  <div style={{
                    width: '32px', height: '32px', flexShrink: 0,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    background: answered === undefined ? '#e2e8f0'
                      : isCorrect ? '#dcfce7' : '#fee2e2',
                    color: answered === undefined ? '#64748b'
                      : isCorrect ? '#15803d' : '#dc2626',
                    fontWeight: 700, fontSize: '13px', borderRadius: '2px',
                  }}>
                    {qNum}
                  </div>

                  {/* Content */}
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <p style={{
                      margin: '0 0 5px 0', fontSize: '13.5px',
                      color: '#1e293b', lineHeight: '1.55',
                      display: '-webkit-box', WebkitLineClamp: 2,
                      WebkitBoxOrient: 'vertical', overflow: 'hidden'
                    }}>
                      {q.question}
                    </p>
                    {answered !== undefined ? (
                      <div style={{ fontSize: '12px', color: '#64748b', display: 'flex', gap: '12px' }}>
                        <span>Your answer: <strong>{String.fromCharCode(65 + answered)}</strong></span>
                        {!isCorrect && (
                          <span style={{ color: '#dc2626' }}>
                            Correct: <strong>{String.fromCharCode(65 + q.correctAnswer)}</strong>
                          </span>
                        )}
                      </div>
                    ) : (
                      <span style={{ fontSize: '12px', color: '#f97316', fontWeight: 600 }}>
                        Not answered
                      </span>
                    )}
                  </div>

                  {/* Indicators */}
                  <div style={{ display: 'flex', gap: '6px', flexShrink: 0, alignItems: 'center' }}>
                    {isFlagged && (
                      <span style={{ fontSize: '13px', color: '#f59e0b' }} title="Flagged">⚑</span>
                    )}
                    {hasComment && (
                      <span style={{ fontSize: '13px', color: '#3b82f6' }} title="Has note">✎</span>
                    )}
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* ── FOOTER ── */}
      <div style={{
        height: '54px', background: '#fff',
        borderTop: '1px solid #e2e8f0',
        display: 'flex', alignItems: 'center',
        padding: '0 20px', gap: '10px', flexShrink: 0
      }}>
        <button className="nav-btn" onClick={onBack}>
          ← Back to Exam
        </button>
        <div style={{ flex: 1 }} />
        {unanswered > 0 && (
          <span style={{ fontSize: '12.5px', color: '#fca5a5' }}>
            {unanswered} question{unanswered > 1 ? 's' : ''} unanswered
          </span>
        )}
        <button className="submit-btn danger" onClick={() => setShowConfirm(true)}>
          Submit Set {currentSet + 1}
        </button>
      </div>

      {/* ── QUIT CONFIRM ── */}
      {showQuitConfirm && (
        <div className="modal-overlay" onClick={() => setShowQuitConfirm(false)}>
          <div className="modal-box modal-box-sm" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <span className="modal-title">Quit Simulation?</span>
              <button className="modal-close" onClick={() => setShowQuitConfirm(false)}>✕</button>
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
                onClick={() => setShowQuitConfirm(false)}
              >
                Cancel
              </button>
              <button className="submit-btn danger" onClick={onQuit}>
                Yes, Quit
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ── CONFIRM DIALOG ── */}
      {showConfirm && (
        <div className="modal-overlay" onClick={() => setShowConfirm(false)}>
          <div className="modal-box modal-box-sm" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <span className="modal-title">Confirm Submission</span>
              <button className="modal-close" onClick={() => setShowConfirm(false)}>✕</button>
            </div>
            <div className="modal-body">
              <p style={{ margin: '0 0 10px', fontSize: '14.5px', color: '#1e293b', fontWeight: 600 }}>
                Submit Set {currentSet + 1}?
              </p>
              <p style={{ margin: 0, fontSize: '13.5px', color: '#475569', lineHeight: '1.6' }}>
                {isLastSet
                  ? 'This will finalise your exam and display your results. This action cannot be undone.'
                  : 'Once submitted, you cannot return to this set. You will proceed to your break or the next set.'}
              </p>
              {unanswered > 0 && (
                <div style={{
                  marginTop: '12px', padding: '10px 12px',
                  background: '#fff7ed', border: '1px solid #fed7aa',
                  borderLeft: '3px solid #f97316', borderRadius: '2px',
                  fontSize: '13px', color: '#7c2d12'
                }}>
                  ⚠ You have {unanswered} unanswered question{unanswered > 1 ? 's' : ''}.
                </div>
              )}
            </div>
            <div className="modal-footer">
              <button
                className="nav-btn"
                style={{ color: '#374151', background: '#f1f5f9', border: '1px solid #d1d5db' }}
                onClick={() => setShowConfirm(false)}
              >
                Cancel
              </button>
              <button
                className="submit-btn danger"
                onClick={() => { setShowConfirm(false); onSubmit(); }}
              >
                Yes, Submit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
