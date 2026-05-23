import { Link } from 'react-router-dom';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardTitle } from './ui/card';
import { BookOpen, FileText, Zap, Target, Youtube, LogOut, User, GraduationCap, ScrollText } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';

export default function Landing() {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-[#f8fafc] p-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-end mb-4">
          <div className="bg-white rounded-lg shadow-md px-3 py-2 flex items-center gap-3 max-w-full">
            <div className="flex items-center gap-2 min-w-0">
              <User className="size-4 sm:size-5 text-indigo-600 flex-shrink-0" />
              <span className="font-medium text-gray-900 text-sm sm:text-base truncate max-w-[120px] sm:max-w-none">{user?.name}</span>
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={logout}
              className="text-red-600 border-red-300 hover:bg-red-50 flex-shrink-0"
            >
              <LogOut className="size-4 mr-1 sm:mr-2" />
              <span className="hidden sm:inline">Logout</span>
              <span className="sm:hidden">Out</span>
            </Button>
          </div>
        </div>

        <div className="text-center mb-6 mt-2 sm:mb-8 sm:mt-4">
          <div className="flex items-center justify-center gap-2.5 mb-2">
            <BookOpen className="size-6 text-indigo-600" />
            <h1 className="text-xl sm:text-2xl font-semibold text-gray-900">Practice Exam System</h1>
          </div>
          <p className="text-sm text-gray-500">
            Project Management MCQ Questions
          </p>
        </div>

        {/* PMP Simulation Mode */}
        <div className="mb-8">
          <Card className="bg-gradient-to-r from-indigo-900 to-indigo-800 text-white border-2 border-indigo-500 hover:shadow-2xl hover:shadow-indigo-500/30 transition-all">
            <CardContent className="p-6 sm:p-8">
              <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                {/* Left: icon + title */}
                <div className="flex items-center gap-4">
                  <div className="bg-indigo-500/30 p-3 rounded-full flex-shrink-0">
                    <GraduationCap className="size-10 text-indigo-200" />
                  </div>
                  <div>
                    <CardTitle className="text-2xl sm:text-3xl mb-1">PMP Exam Simulation</CardTitle>
                    <CardDescription className="text-indigo-200 text-base sm:text-lg">
                      Full exam simulation with timer, breaks, and review
                    </CardDescription>
                  </div>
                </div>
                {/* Right: stats + button */}
                <div className="flex flex-col sm:flex-row sm:items-center gap-4">
                  <div className="flex items-center gap-4">
                    <div>
                      <p className="text-sm text-indigo-200">180 questions</p>
                      <p className="text-sm text-indigo-200">240 minutes</p>
                    </div>
                    <div className="h-8 w-px bg-indigo-500/50" />
                    <div>
                      <p className="text-sm text-indigo-200">60 questions</p>
                      <p className="text-sm text-indigo-200">80 minutes</p>
                    </div>
                  </div>
                  <Link to="/pmp-simulation" className="w-full sm:w-auto">
                    <Button className="w-full sm:w-auto bg-white text-indigo-900 hover:bg-indigo-50 text-base sm:text-lg px-6 sm:px-8 py-5 sm:py-6 font-semibold">
                      <GraduationCap className="size-5 mr-2" />
                      Start Simulation
                    </Button>
                  </Link>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="mb-8">
          <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-3">Practice Sets</h2>
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm divide-y divide-gray-100">
            {[
              { to: '/sets-50', icon: FileText, color: 'text-indigo-600', bg: 'bg-indigo-50', badge: 'bg-indigo-100 text-indigo-700', label: 'DumpsGate Standard', sub: '34 sets · 50 questions each', tag: '1,650 Qs' },
              { to: '/sets-25', icon: Zap, color: 'text-purple-600', bg: 'bg-purple-50', badge: 'bg-purple-100 text-purple-700', label: 'DumpsGate Quick', sub: '67 sets · 25 questions each', tag: '1,675 Qs' },
              { to: '/sets-ramd', icon: Target, color: 'text-green-600', bg: 'bg-green-50', badge: 'bg-green-100 text-green-700', label: 'RamD Practice', sub: 'Sets of 15 questions', tag: 'Focused' },
              { to: '/sets-davidyt', icon: Youtube, color: 'text-orange-600', bg: 'bg-orange-50', badge: 'bg-orange-100 text-orange-700', label: 'David YT Practice', sub: 'Sets of 10 questions', tag: 'Daily' },
            ].map(item => (
              <Link key={item.to} to={item.to} className="flex items-center gap-4 px-5 py-4 hover:bg-gray-50 transition-colors group first:rounded-t-xl last:rounded-b-xl">
                <div className={`${item.bg} p-2.5 rounded-lg flex-shrink-0`}>
                  <item.icon className={`size-5 ${item.color}`} />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="font-semibold text-gray-900 text-sm">{item.label}</div>
                  <div className="text-xs text-gray-400 mt-0.5">{item.sub}</div>
                </div>
                <span className={`text-xs font-semibold px-2.5 py-1 rounded-full ${item.badge} flex-shrink-0`}>{item.tag}</span>
                <svg className="size-4 text-gray-300 group-hover:text-gray-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" /></svg>
              </Link>
            ))}
          </div>
        </div>

        {/* Footer */}
        <div className="mt-10 flex flex-col sm:flex-row items-center justify-between gap-3 text-sm text-gray-400 border-t border-gray-200 pt-6">
          <div>
            Developed by{' '}
            <a
              href="https://www.linkedin.com/in/abdulhadimohamad/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-indigo-600 font-semibold hover:underline"
            >
              Max
            </a>
          </div>
          <Link
            to="/release-notes"
            className="flex items-center gap-1.5 text-indigo-500 hover:text-indigo-700 font-medium transition-colors"
          >
            <ScrollText className="size-4" />
            Release Notes
          </Link>
        </div>
      </div>
    </div>
  );
}
