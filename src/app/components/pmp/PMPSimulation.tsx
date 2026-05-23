import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import './pmp-exam.css';

export default function PMPSimulation() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();
  const [showDisclaimer, setShowDisclaimer] = useState<'full' | 'quick' | null>(null);

  const handleUnderstand = () => {
    const mode = showDisclaimer;
    setShowDisclaimer(null);
    navigate(`/pmp-exam/${mode}`);
  };

  const MODES = [
    {
      key: 'full' as const,
      label: 'Full Simulation',
      tag: 'RECOMMENDED',
      questions: 180,
      minutes: 240,
      features: [
        '3 sets × 60 questions',
        '10-minute break between sets',
        'Flag, highlight & annotate',
        'Mirrors actual PMP structure',
      ],
    },
    {
      key: 'quick' as const,
      label: 'Quick Practice',
      tag: null,
      questions: 60,
      minutes: 80,
      features: [
        '3 sets × 20 questions',
        '10-minute break between sets',
        'Same tools as Full Exam',
        'Great for focused practice',
      ],
    },
  ];

  return (
    <div style={{
      width: '100%', minHeight: '100vh', background: '#f8fafc',
      display: 'flex', flexDirection: 'column',
      fontFamily: "'Segoe UI', system-ui, sans-serif",
    }}>

      {/* ── HEADER ── */}
      <div className="pmp-sim-header">
        <span style={{
          background: 'rgba(255,255,255,0.2)', color: '#fff',
          fontSize: '10.5px', fontWeight: 800,
          padding: '3px 9px', borderRadius: '3px', letterSpacing: '0.12em',
          flexShrink: 0,
        }}>PMP</span>
        <span style={{ color: '#fff', fontSize: '13.5px', fontWeight: 600, flex: 1, minWidth: 0, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          EXAM SIMULATION CENTRE
        </span>
        <span style={{ color: 'rgba(255,255,255,0.75)', fontSize: '13px', flexShrink: 0 }} className="exam-header-candidate">{user?.name}</span>
        <button
          onClick={() => navigate('/')}
          style={{
            height: '30px', padding: '0 14px',
            background: 'rgba(255,255,255,0.12)',
            border: '1px solid rgba(255,255,255,0.25)', borderRadius: '4px',
            color: 'rgba(255,255,255,0.85)', fontSize: '12.5px', cursor: 'pointer', fontFamily: 'inherit',
            fontWeight: 500, flexShrink: 0, whiteSpace: 'nowrap',
          }}
        >
          ← Main Page
        </button>
        <button
          onClick={logout}
          style={{
            height: '30px', padding: '0 14px',
            background: 'rgba(255,255,255,0.15)',
            border: '1px solid rgba(255,255,255,0.25)', borderRadius: '4px',
            color: '#fff', fontSize: '12.5px', cursor: 'pointer', fontFamily: 'inherit',
            flexShrink: 0, whiteSpace: 'nowrap',
          }}
        >
          Sign out
        </button>
      </div>

      {/* ── CONTENT ── */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '40px 24px' }}>
        <div style={{ maxWidth: '820px', margin: '0 auto' }}>

          {/* Heading */}
          <div style={{ textAlign: 'center', marginBottom: '36px' }}>
            <h2 style={{ color: '#111827', fontSize: '24px', fontWeight: 700, margin: '0 0 8px 0' }}>
              Choose Your Exam Mode
            </h2>
            <p style={{ color: '#64748b', fontSize: '14px', margin: 0 }}>
              A realistic PMP certification simulation with timed sections, review tools, and break management.
            </p>
          </div>

          {/* Mode cards */}
          <div className="pmp-mode-grid">
            {MODES.map(mode => (
              <div
                key={mode.key}
                style={{
                  background: '#fff', border: '1px solid #e2e8f0',
                  borderRadius: '8px', padding: '28px',
                  boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
                  position: 'relative', overflow: 'hidden', cursor: 'pointer',
                  transition: 'border-color 0.15s, box-shadow 0.15s',
                }}
                onMouseEnter={e => {
                  (e.currentTarget as HTMLDivElement).style.borderColor = '#93c5fd';
                  (e.currentTarget as HTMLDivElement).style.boxShadow = '0 4px 16px rgba(29,78,216,0.1)';
                }}
                onMouseLeave={e => {
                  (e.currentTarget as HTMLDivElement).style.borderColor = '#e2e8f0';
                  (e.currentTarget as HTMLDivElement).style.boxShadow = '0 2px 8px rgba(0,0,0,0.05)';
                }}
                onClick={() => setShowDisclaimer(mode.key)}
              >
                {mode.tag && (
                  <div style={{
                    position: 'absolute', top: '14px', right: '14px',
                    background: '#1d4ed8', color: '#fff',
                    fontSize: '10px', fontWeight: 800, letterSpacing: '0.08em',
                    padding: '3px 8px', borderRadius: '3px',
                  }}>
                    {mode.tag}
                  </div>
                )}

                <h3 style={{ color: '#111827', fontSize: '18px', fontWeight: 700, margin: '0 0 4px 0' }}>
                  {mode.label}
                </h3>
                <p style={{ color: '#1d4ed8', fontSize: '13.5px', fontWeight: 600, margin: '0 0 20px 0' }}>
                  {mode.questions} questions &nbsp;·&nbsp; {mode.minutes} minutes
                </p>

                <ul style={{
                  padding: '0 0 0 16px', margin: '0 0 24px 0',
                  color: '#64748b', fontSize: '13.5px', lineHeight: '1.9',
                }}>
                  {mode.features.map(f => <li key={f}>{f}</li>)}
                </ul>

                <button
                  className="submit-btn"
                  style={{ width: '100%', height: '40px', borderRadius: '6px' }}
                  onClick={e => { e.stopPropagation(); setShowDisclaimer(mode.key); }}
                >
                  Start {mode.label}
                </button>
              </div>
            ))}
          </div>

          {/* Feature strip */}
          <div className="pmp-feature-strip">
            {[
              { icon: '⏱', text: 'Countdown timer with low-time warning' },
              { icon: '⚑', text: 'Flag questions for review' },
              { icon: '✎', text: 'Highlight & strikethrough text' },
              { icon: '⊞', text: 'Full question navigator' },
            ].map(item => (
              <div key={item.text} className="pmp-feature-item">
                <span style={{ fontSize: '16px', flexShrink: 0 }}>{item.icon}</span>
                <span style={{ fontSize: '12.5px', color: '#64748b' }}>{item.text}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── DISCLAIMER MODAL ── */}
      {showDisclaimer && (
        <div className="modal-overlay" onClick={() => setShowDisclaimer(null)}>
          <div className="modal-box" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <span className="modal-title">Important Disclaimer</span>
              <button className="modal-close" onClick={() => setShowDisclaimer(null)}>✕</button>
            </div>
            <div className="modal-body">
              <p style={{ fontSize: '14px', color: '#374151', marginBottom: '12px', lineHeight: '1.7' }}>
                This is a <strong>practice simulation tool</strong> and is not affiliated with,
                endorsed by, or associated with PMI (Project Management Institute).
              </p>
              <p style={{ fontSize: '14px', color: '#374151', marginBottom: '12px', lineHeight: '1.7' }}>
                Questions in this simulation are for practice purposes only and may not reflect
                the exact style, difficulty, or content of the actual PMP certification examination.
              </p>
              <div style={{
                padding: '12px 14px', background: '#fffbeb',
                border: '1px solid #fde68a', borderLeft: '3px solid #f59e0b',
                borderRadius: '4px', fontSize: '13.5px', color: '#78350f', lineHeight: '1.6',
              }}>
                Results from this simulation should not be considered a guarantee of performance
                on the actual PMP exam. Use at your own discretion.
              </div>
            </div>
            <div className="modal-footer">
              <button
                className="nav-btn"
                onClick={() => setShowDisclaimer(null)}
              >
                Cancel
              </button>
              <button className="submit-btn" onClick={handleUnderstand}>
                I Understand — Begin
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
