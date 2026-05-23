import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { BookOpen, LogIn, UserPlus } from 'lucide-react';

const SIGNUP_RATE_LIMIT_KEY = 'signup-rate-limit';
const SIGNUP_COOLDOWN_MS = 60000; // 60 seconds

export default function Login() {
  const [isSignup, setIsSignup] = useState(false);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { login, signup } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isSubmitting) return;
    setError('');

    // Rate limit for signup
    if (isSignup) {
      const lastAttempt = localStorage.getItem(SIGNUP_RATE_LIMIT_KEY);
      if (lastAttempt) {
        const elapsed = Date.now() - parseInt(lastAttempt, 10);
        if (elapsed < SIGNUP_COOLDOWN_MS) {
          const remaining = Math.ceil((SIGNUP_COOLDOWN_MS - elapsed) / 1000);
          setError(`Please wait ${remaining} seconds before trying again.`);
          return;
        }
      }
    }

    setIsSubmitting(true);

    if (isSignup) {
      if (!name.trim()) {
        setError('Please enter your name');
        setIsSubmitting(false);
        return;
      }
      localStorage.setItem(SIGNUP_RATE_LIMIT_KEY, Date.now().toString());
      const result = await signup(name, email, password);
      if (result.success) {
        navigate('/');
      } else {
        setError(result.error || 'Signup failed. Please try again.');
      }
    } else {
      const result = await login(email, password);
      if (result.success) {
        navigate('/');
      } else {
        setError(result.error || 'Invalid email or password');
      }
    }

    setIsSubmitting(false);
  };

  return (
    <div className="min-h-screen bg-[#f8fafc] p-6 flex items-center justify-center">
      <div className="max-w-md w-full">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <BookOpen className="size-8 text-indigo-600" />
            <h1 className="text-2xl font-bold text-gray-900">Practice Exam System</h1>
          </div>
          <p className="text-sm text-gray-500">
            Sign in to access your personalized practice sessions
          </p>
        </div>

        <Card>
          <CardHeader>
            <CardTitle className="text-2xl">
              {isSignup ? 'Create Account' : 'Welcome Back'}
            </CardTitle>
            <CardDescription>
              {isSignup
                ? 'Create an account to track your progress'
                : 'Login to continue your practice sessions'
              }
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              {isSignup && (
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
                    Full Name
                  </label>
                  <input
                    id="name"
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required={isSignup}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none"
                    placeholder="John Doe"
                  />
                </div>
              )}

              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                  Email
                </label>
                <input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none"
                  placeholder="you@example.com"
                />
              </div>

              <div>
                <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">
                  Password
                </label>
                <input
                  id="password"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none"
                  placeholder="••••••••"
                />
              </div>

              {error && (
                <div className="p-3 bg-red-50 border border-red-200 rounded-lg text-red-600 text-sm">
                  {error}
                </div>
              )}

              <Button
                type="submit"
                disabled={isSubmitting}
                className="w-full bg-indigo-600 hover:bg-indigo-700 py-6 text-lg disabled:opacity-60 disabled:cursor-not-allowed"
              >
                {isSubmitting ? (
                  <span className="flex items-center justify-center">
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    {isSignup ? 'Creating Account...' : 'Logging in...'}
                  </span>
                ) : isSignup ? (
                  <>
                    <UserPlus className="size-5 mr-2" />
                    Create Account
                  </>
                ) : (
                  <>
                    <LogIn className="size-5 mr-2" />
                    Login
                  </>
                )}
              </Button>
            </form>

            <div className="mt-6 text-center">
              <button
                type="button"
                onClick={() => {
                  setIsSignup(!isSignup);
                  setError('');
                  setIsSubmitting(false);
                }}
                className="text-indigo-600 hover:text-indigo-700 font-medium"
              >
                {isSignup
                  ? 'Already have an account? Login'
                  : "Don't have an account? Sign up"
                }
              </button>
            </div>
          </CardContent>
        </Card>

      </div>
    </div>
  );
}
