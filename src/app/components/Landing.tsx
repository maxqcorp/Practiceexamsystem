import { Link } from 'react-router-dom';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { BookOpen, FileText, Zap, Target, Youtube, LogOut, User, GraduationCap } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';

export default function Landing() {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-end mb-4">
          <div className="bg-white rounded-lg shadow-md px-4 py-2 flex items-center gap-4">
            <div className="flex items-center gap-2">
              <User className="size-5 text-indigo-600" />
              <span className="font-medium text-gray-900">{user?.name}</span>
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={logout}
              className="text-red-600 border-red-300 hover:bg-red-50"
            >
              <LogOut className="size-4 mr-2" />
              Logout
            </Button>
          </div>
        </div>

        <div className="text-center mb-12 mt-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <BookOpen className="size-16 text-indigo-600" />
            <h1 className="text-5xl font-bold text-gray-900">Practice Exam System</h1>
          </div>
          <p className="text-xl text-gray-600 mb-2">
            Project Management MCQ Questions
          </p>
          <p className="text-sm text-gray-500">
            Choose your practice mode and start learning
          </p>
        </div>

        {/* PMP Simulation Mode */}
        <div className="mb-8">
          <Card className="bg-gradient-to-r from-indigo-900 to-indigo-800 text-white border-2 border-indigo-500 hover:shadow-2xl hover:shadow-indigo-500/30 transition-all">
            <CardContent className="p-8">
              <div className="flex items-center justify-between flex-wrap gap-4">
                <div className="flex items-center gap-4">
                  <div className="bg-indigo-500/30 p-3 rounded-full">
                    <GraduationCap className="size-10 text-indigo-200" />
                  </div>
                  <div>
                    <CardTitle className="text-3xl mb-1">PMP Exam Simulation</CardTitle>
                    <CardDescription className="text-indigo-200 text-lg">
                      Full exam simulation with timer, breaks, and review
                    </CardDescription>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <div className="text-right">
                    <p className="text-sm text-indigo-200">180 questions</p>
                    <p className="text-sm text-indigo-200">240 minutes</p>
                  </div>
                  <div className="h-10 w-px bg-indigo-500/50" />
                  <div className="text-right">
                    <p className="text-sm text-indigo-200">60 questions</p>
                    <p className="text-sm text-indigo-200">80 minutes</p>
                  </div>
                  <Link to="/pmp-simulation">
                    <Button className="bg-white text-indigo-900 hover:bg-indigo-50 text-lg px-8 py-6 font-semibold">
                      <GraduationCap className="size-5 mr-2" />
                      Start Simulation
                    </Button>
                  </Link>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          <Card className="hover:shadow-xl transition-all border-2 border-indigo-200 hover:border-indigo-400">
            <CardHeader>
              <div className="flex items-center gap-2 mb-3">
                <FileText className="size-8 text-indigo-600" />
                <CardTitle className="text-2xl">DumpsGate Standard Practice</CardTitle>
              </div>
              <CardDescription className="text-base">
                34 sets with 50 questions each
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <ul className="space-y-2 text-sm text-gray-700">
                  <li className="flex items-start gap-2">
                    <span className="text-indigo-600 font-bold">•</span>
                    <span>Comprehensive practice sessions</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-indigo-600 font-bold">•</span>
                    <span>Better for focused study time</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-indigo-600 font-bold">•</span>
                    <span>1650 questions total</span>
                  </li>
                </ul>
                <Link to="/sets-50">
                  <Button className="w-full bg-indigo-600 hover:bg-indigo-700 text-lg py-6">
                    <FileText className="size-5 mr-2" />
                    50 Questions per Set
                  </Button>
                </Link>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-xl transition-all border-2 border-purple-200 hover:border-purple-400">
            <CardHeader>
              <div className="flex items-center gap-2 mb-3">
                <Zap className="size-8 text-purple-600" />
                <CardTitle className="text-2xl">DumpsGate Quick Practice</CardTitle>
              </div>
              <CardDescription className="text-base">
                67 sets with 25 questions each
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <ul className="space-y-2 text-sm text-gray-700">
                  <li className="flex items-start gap-2">
                    <span className="text-purple-600 font-bold">•</span>
                    <span>Shorter, focused practice sessions</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-purple-600 font-bold">•</span>
                    <span>Perfect for limited time</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-purple-600 font-bold">•</span>
                    <span>1675 questions total</span>
                  </li>
                </ul>
                <Link to="/sets-25">
                  <Button className="w-full bg-purple-600 hover:bg-purple-700 text-lg py-6">
                    <Zap className="size-5 mr-2" />
                    25 Questions per Set
                  </Button>
                </Link>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-xl transition-all border-2 border-green-200 hover:border-green-400">
            <CardHeader>
              <div className="flex items-center gap-2 mb-3">
                <Target className="size-8 text-green-600" />
                <CardTitle className="text-2xl">RamD Practice</CardTitle>
              </div>
              <CardDescription className="text-base">
                Sets with 15 questions each
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <ul className="space-y-2 text-sm text-gray-700">
                  <li className="flex items-start gap-2">
                    <span className="text-green-600 font-bold">•</span>
                    <span>Compact, focused learning sessions</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-green-600 font-bold">•</span>
                    <span>Ideal for quick review sessions</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-green-600 font-bold">•</span>
                    <span>Perfect balance of depth and speed</span>
                  </li>
                </ul>
                <Link to="/sets-ramd">
                  <Button className="w-full bg-green-600 hover:bg-green-700 text-lg py-6">
                    <Target className="size-5 mr-2" />
                    15 Questions per Set
                  </Button>
                </Link>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-xl transition-all border-2 border-orange-200 hover:border-orange-400">
            <CardHeader>
              <div className="flex items-center gap-2 mb-3">
                <Youtube className="size-8 text-orange-600" />
                <CardTitle className="text-2xl">David YT Practice</CardTitle>
              </div>
              <CardDescription className="text-base">
                Sets with 10 questions each
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <ul className="space-y-2 text-sm text-gray-700">
                  <li className="flex items-start gap-2">
                    <span className="text-orange-600 font-bold">•</span>
                    <span>Quick, bite-sized practice sessions</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-orange-600 font-bold">•</span>
                    <span>Perfect for daily study habits</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-orange-600 font-bold">•</span>
                    <span>Easy to fit into busy schedules</span>
                  </li>
                </ul>
                <Link to="/sets-davidyt">
                  <Button className="w-full bg-orange-600 hover:bg-orange-700 text-lg py-6">
                    <Youtube className="size-5 mr-2" />
                    10 Questions per Set
                  </Button>
                </Link>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="bg-white rounded-lg p-6 shadow-md">
          <h2 className="text-xl font-semibold mb-3 text-gray-900">How it works</h2>
          <ul className="space-y-2 text-gray-700">
            <li className="flex items-start gap-2">
              <span className="text-indigo-600 font-bold">1.</span>
              <span>Choose your preferred practice mode (50, 25, 15, or 10 questions per set)</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-indigo-600 font-bold">2.</span>
              <span>Select a practice set to begin</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-indigo-600 font-bold">3.</span>
              <span>Click on your answer choice for each question</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-indigo-600 font-bold">4.</span>
              <span>Get instant feedback with explanations</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-indigo-600 font-bold">5.</span>
              <span>Your progress is automatically saved across sessions</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}
