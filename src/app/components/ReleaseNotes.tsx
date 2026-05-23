import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../utils/supabase/client';
import { ArrowLeft, Sparkles, Wrench, Shield, TrendingUp } from 'lucide-react';

interface ReleaseNote {
  id: string;
  version: string;
  release_date: string;
  display_title: string;
  display_summary: string;
  display_items: string[];
  category: 'feature' | 'improvement' | 'fix' | 'security';
}

const CATEGORY_CONFIG = {
  feature: {
    label: 'New Feature',
    icon: Sparkles,
    bg: '#eff6ff',
    border: '#bfdbfe',
    color: '#1d4ed8',
    dot: '#3b82f6',
  },
  improvement: {
    label: 'Improvement',
    icon: TrendingUp,
    bg: '#f0fdf4',
    border: '#bbf7d0',
    color: '#15803d',
    dot: '#22c55e',
  },
  fix: {
    label: 'Bug Fix',
    icon: Wrench,
    bg: '#fff7ed',
    border: '#fed7aa',
    color: '#c2410c',
    dot: '#f97316',
  },
  security: {
    label: 'Security',
    icon: Shield,
    bg: '#fdf4ff',
    border: '#e9d5ff',
    color: '#7e22ce',
    dot: '#a855f7',
  },
};

function formatDate(iso: string) {
  return new Date(iso).toLocaleDateString('en-US', {
    year: 'numeric', month: 'long', day: 'numeric',
  });
}

export default function ReleaseNotes() {
  const [notes, setNotes] = useState<ReleaseNote[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    supabase
      .from('release_notes')
      .select('id, version, release_date, display_title, display_summary, display_items, category')
      .eq('is_published', true)
      .order('sort_order', { ascending: true })
      .then(({ data }) => {
        setNotes((data as ReleaseNote[]) || []);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #f0f4ff 0%, #faf5ff 50%, #fff0f6 100%)',
      fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif",
    }}>
      {/* Header */}
      <div style={{
        background: '#fff',
        borderBottom: '1px solid #e2e8f0',
        padding: '0 24px',
        display: 'flex',
        alignItems: 'center',
        height: '56px',
        gap: '16px',
        position: 'sticky',
        top: 0,
        zIndex: 10,
        boxShadow: '0 1px 4px rgba(0,0,0,0.06)',
      }}>
        <Link
          to="/"
          style={{
            display: 'flex', alignItems: 'center', gap: '6px',
            color: '#64748b', fontSize: '13.5px', fontWeight: 500,
            textDecoration: 'none', padding: '5px 10px',
            border: '1px solid #e2e8f0', borderRadius: '5px',
            background: '#f8fafc', whiteSpace: 'nowrap',
          }}
        >
          <ArrowLeft size={14} />
          Back
        </Link>
        <div style={{ flex: 1, minWidth: 0 }}>
          <span style={{ fontSize: '15px', fontWeight: 700, color: '#111827' }}>
            Release Notes
          </span>
        </div>
        <span style={{ fontSize: '12px', color: '#94a3b8', whiteSpace: 'nowrap' }}>
          Practice Exam System
        </span>
      </div>

      {/* Content */}
      <div style={{ maxWidth: '680px', margin: '0 auto', padding: '40px 20px 80px' }}>

        {/* Hero */}
        <div style={{ textAlign: 'center', marginBottom: '48px' }}>
          <h1 style={{ fontSize: '32px', fontWeight: 800, color: '#111827', margin: '0 0 10px' }}>
            What's New
          </h1>
          <p style={{ fontSize: '15px', color: '#64748b', margin: 0, lineHeight: '1.6' }}>
            Updates, improvements and new features added to the Practice Exam System.
          </p>
        </div>

        {/* Notes list */}
        {loading ? (
          <div style={{ textAlign: 'center', padding: '60px 0', color: '#94a3b8', fontSize: '14px' }}>
            Loading release notes…
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0' }}>
            {notes.map((note, i) => {
              const cfg = CATEGORY_CONFIG[note.category] || CATEGORY_CONFIG.improvement;
              const Icon = cfg.icon;
              const isLast = i === notes.length - 1;

              return (
                <div key={note.id} style={{ display: 'flex', gap: '0' }}>
                  {/* Timeline spine */}
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginRight: '20px', flexShrink: 0 }}>
                    <div style={{
                      width: '36px', height: '36px', borderRadius: '50%',
                      background: cfg.bg, border: `2px solid ${cfg.border}`,
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                      flexShrink: 0,
                    }}>
                      <Icon size={16} color={cfg.color} />
                    </div>
                    {!isLast && (
                      <div style={{ width: '2px', flex: 1, background: '#e2e8f0', minHeight: '24px', marginTop: '4px' }} />
                    )}
                  </div>

                  {/* Card */}
                  <div style={{
                    flex: 1, paddingBottom: isLast ? '0' : '32px',
                  }}>
                    <div style={{
                      background: '#fff',
                      border: '1px solid #e2e8f0',
                      borderRadius: '10px',
                      padding: '20px 22px',
                      boxShadow: '0 1px 6px rgba(0,0,0,0.05)',
                    }}>
                      {/* Top row */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap', marginBottom: '10px' }}>
                        <span style={{
                          fontSize: '11px', fontWeight: 800, letterSpacing: '0.08em',
                          background: '#1d4ed8', color: '#fff',
                          padding: '2px 8px', borderRadius: '3px',
                        }}>
                          {note.version}
                        </span>
                        <span style={{
                          fontSize: '11px', fontWeight: 600, letterSpacing: '0.04em',
                          background: cfg.bg, color: cfg.color,
                          border: `1px solid ${cfg.border}`,
                          padding: '2px 8px', borderRadius: '3px',
                        }}>
                          {cfg.label}
                        </span>
                        <span style={{ fontSize: '12px', color: '#94a3b8', marginLeft: 'auto' }}>
                          {formatDate(note.release_date)}
                        </span>
                      </div>

                      {/* Title */}
                      <h2 style={{ fontSize: '17px', fontWeight: 700, color: '#111827', margin: '0 0 6px' }}>
                        {note.display_title}
                      </h2>

                      {/* Summary */}
                      <p style={{ fontSize: '13.5px', color: '#64748b', margin: '0 0 14px', lineHeight: '1.65' }}>
                        {note.display_summary}
                      </p>

                      {/* Bullet items */}
                      {note.display_items && note.display_items.length > 0 && (
                        <ul style={{ margin: 0, padding: 0, listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '7px' }}>
                          {note.display_items.map((item, idx) => (
                            <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '8px', fontSize: '13.5px', color: '#374151', lineHeight: '1.55' }}>
                              <span style={{
                                width: '6px', height: '6px', borderRadius: '50%',
                                background: cfg.dot, flexShrink: 0, marginTop: '6px',
                              }} />
                              {item}
                            </li>
                          ))}
                        </ul>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* Footer credit */}
        <div style={{
          textAlign: 'center', marginTop: '56px',
          paddingTop: '24px', borderTop: '1px solid #e2e8f0',
          fontSize: '13px', color: '#94a3b8',
        }}>
          Developed by{' '}
          <a
            href="https://www.linkedin.com/in/abdulhadimohamad/"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: '#1d4ed8', fontWeight: 600, textDecoration: 'none' }}
          >
            Max
          </a>
          {' '}· Practice Exam System
        </div>
      </div>
    </div>
  );
}
