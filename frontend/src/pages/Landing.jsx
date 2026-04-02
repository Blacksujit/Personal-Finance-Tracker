import React from 'react';
import { Link } from 'react-router-dom';

const Landing = () => {
  const features = [
    {
      icon: '🧠',
      title: 'Smart Insights',
      description: 'AI-powered analysis helps you understand spending patterns and save money intelligently'
    },
    {
      icon: '📊',
      title: 'Real-time Analytics',
      description: 'Track your finances with beautiful charts and up-to-the-minute data visualization'
    },
    {
      icon: '🔒',
      title: 'Secure Tracking',
      description: 'Bank-level security keeps your financial data safe and private with end-to-end encryption'
    }
  ];

  const howItWorks = [
    {
      step: '1',
      title: 'Add Transactions',
      description: 'Easily log income and expenses with smart categorization'
    },
    {
      step: '2',
      title: 'Track Spending',
      description: 'Visualize your financial habits with interactive charts'
    },
    {
      step: '3',
      title: 'Improve Savings',
      description: 'Get personalized insights to optimize your financial future'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse-slow" />
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-indigo-300 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse-slow" />
      </div>

      {/* Navigation */}
      <nav className="relative z-10 flex justify-between items-center px-6 py-4 bg-white/80 backdrop-blur-md border-b border-gray-200">
        <div className="flex items-center space-x-2">
          <div className="w-10 h-10 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl flex items-center justify-center">
            <span className="text-white font-bold text-lg">💰</span>
          </div>
          <span className="text-xl font-bold text-gray-900">FinanceTracker</span>
        </div>
        <div className="flex items-center space-x-4">
          <Link to="/login" className="text-gray-700 hover:text-indigo-600 font-medium transition-colors">
            Sign In
          </Link>
          <Link to="/signup" className="btn-primary">
            Get Started
          </Link>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative z-10 px-6 pt-20 pb-32 text-center">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            <span className="text-gradient">Take Control of</span>
            <br />
            <span className="text-gray-900">Your Money</span>
          </h1>
          
          <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Track, analyze, and grow your finances intelligently with our modern personal finance dashboard
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <Link to="/signup" className="btn-primary text-lg px-8 py-4 shadow-glow">
              Get Started Free
            </Link>
            <Link 
              to="/demo" 
              className="btn-secondary text-lg px-8 py-4"
            >
              View Demo
            </Link>
          </div>

          <div className="mt-8 flex items-center justify-center space-x-8 text-sm text-gray-500">
            <div className="flex items-center">
              <span className="text-green-500 mr-2">✓</span>
              No credit card required
            </div>
            <div className="flex items-center">
              <span className="text-green-500 mr-2">✓</span>
              14-day free trial
            </div>
            <div className="flex items-center">
              <span className="text-green-500 mr-2">✓</span>
              Cancel anytime
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="relative z-10 py-20 px-6 bg-white/60 backdrop-blur-sm">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Everything You Need to Master Your Finances
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Powerful features designed to help you save money, reduce expenses, and achieve your financial goals
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="card-glass text-center hover-lift"
              >
                <div className="text-5xl mb-4">{feature.icon}</div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="relative z-10 py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              How It Works
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Get started in minutes and start seeing results immediately
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {howItWorks.map((item, index) => (
              <div
                key={index}
                className="relative"
              >
                <div className="card p-8 text-center hover-lift">
                  <div className="w-16 h-16 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-full flex items-center justify-center text-white text-2xl font-bold mx-auto mb-4">
                    {item.step}
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 mb-3">{item.title}</h3>
                  <p className="text-gray-600">{item.description}</p>
                </div>
                
                {index < howItWorks.length - 1 && (
                  <div className="hidden md:block absolute top-1/2 -right-4 transform -translate-y-1/2 text-indigo-400">
                    <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Visual Preview */}
      <section className="relative z-10 py-20 px-6 bg-white/60 backdrop-blur-sm">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Beautiful Dashboard, Powerful Insights
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              See your financial data come to life with our intuitive dashboard
            </p>
          </div>

          <div className="glass-card p-8 rounded-3xl">
            <div className="bg-gray-900 rounded-2xl p-6 shadow-2xl">
              {/* Mock Dashboard */}
              <div className="grid grid-cols-3 gap-4 mb-6">
                <div className="bg-gray-800 p-4 rounded-xl">
                  <div className="text-green-400 text-sm mb-1">Total Income</div>
                  <div className="text-white text-2xl font-bold">$12,450</div>
                </div>
                <div className="bg-gray-800 p-4 rounded-xl">
                  <div className="text-red-400 text-sm mb-1">Total Expenses</div>
                  <div className="text-white text-2xl font-bold">$8,320</div>
                </div>
                <div className="bg-gray-800 p-4 rounded-xl">
                  <div className="text-blue-400 text-sm mb-1">Savings Rate</div>
                  <div className="text-white text-2xl font-bold">33.1%</div>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-gray-800 p-4 rounded-xl">
                  <div className="text-gray-400 text-sm mb-3">Expenses by Category</div>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <div className="w-3 h-3 bg-blue-500 rounded-full mr-2"></div>
                        <span className="text-gray-300 text-sm">Food</span>
                      </div>
                      <span className="text-gray-400 text-sm">$2,100</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <div className="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
                        <span className="text-gray-300 text-sm">Transport</span>
                      </div>
                      <span className="text-gray-400 text-sm">$1,800</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <div className="w-3 h-3 bg-purple-500 rounded-full mr-2"></div>
                        <span className="text-gray-300 text-sm">Shopping</span>
                      </div>
                      <span className="text-gray-400 text-sm">$1,200</span>
                    </div>
                  </div>
                </div>
                <div className="bg-gray-800 p-4 rounded-xl">
                  <div className="text-gray-400 text-sm mb-3">Monthly Trend</div>
                  <div className="h-32 flex items-end justify-between space-x-1">
                    <div className="w-full bg-blue-500 rounded-t" style={{height: '60%'}}></div>
                    <div className="w-full bg-blue-500 rounded-t" style={{height: '80%'}}></div>
                    <div className="w-full bg-blue-500 rounded-t" style={{height: '70%'}}></div>
                    <div className="w-full bg-blue-500 rounded-t" style={{height: '90%'}}></div>
                    <div className="w-full bg-green-500 rounded-t" style={{height: '85%'}}></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative z-10 py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <div className="card-glass p-12 text-center">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Ready to Transform Your Financial Future?
            </h2>
            <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
              Join thousands of users who have already taken control of their finances with our smart tracking tools
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Link to="/signup" className="btn-primary text-lg px-8 py-4 shadow-glow">
                Start Free Trial
              </Link>
              <Link to="/login" className="btn-secondary text-lg px-8 py-4">
                Sign In
              </Link>
            </div>

            <div className="mt-8 flex items-center justify-center space-x-6 text-sm text-gray-500">
              <div className="flex items-center">
                <span className="text-yellow-500 mr-1">⭐</span>
                4.9/5 rating
              </div>
              <div className="flex items-center">
                <span className="text-green-500 mr-1">👥</span>
                10,000+ users
              </div>
              <div className="flex items-center">
                <span className="text-blue-500 mr-1">🔒</span>
                Bank-level security
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="relative z-10 bg-gray-900 text-white py-12 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <div className="w-8 h-8 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold">💰</span>
                </div>
                <span className="text-lg font-bold">FinanceTracker</span>
              </div>
              <p className="text-gray-400">
                Your trusted partner in personal finance management
              </p>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Product</h4>
              <ul className="space-y-2 text-gray-400">
                <li><Link to="/features" className="hover:text-white transition-colors">Features</Link></li>
                <li><Link to="/pricing" className="hover:text-white transition-colors">Pricing</Link></li>
                <li><Link to="/security" className="hover:text-white transition-colors">Security</Link></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Company</h4>
              <ul className="space-y-2 text-gray-400">
                <li><Link to="/about" className="hover:text-white transition-colors">About</Link></li>
                <li><Link to="/blog" className="hover:text-white transition-colors">Blog</Link></li>
                <li><Link to="/careers" className="hover:text-white transition-colors">Careers</Link></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-4">Support</h4>
              <ul className="space-y-2 text-gray-400">
                <li><Link to="/help" className="hover:text-white transition-colors">Help Center</Link></li>
                <li><Link to="/contact" className="hover:text-white transition-colors">Contact</Link></li>
                <li><Link to="/privacy" className="hover:text-white transition-colors">Privacy</Link></li>
              </ul>
            </div>
          </div>
          
          <div className="border-t border-gray-800 pt-8 text-center text-gray-400">
            <p>&copy; 2024 FinanceTracker. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Landing;
