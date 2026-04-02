import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { dashboardService } from '../services/api';
import { logout } from '../services/auth';

const Dashboard = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      setLoading(true);
      setError(null);
      console.log('🚀 Starting dashboard fetch...');
      
      const dashboardData = await dashboardService.getData();
      console.log('✅ Dashboard data received:', dashboardData);
      
      setData(dashboardData);
    } catch (error) {
      console.error('❌ Dashboard fetch error:', error);
      setError(error.message || 'Failed to load dashboard data');
    } finally {
      setLoading(false);
    }
  };

  const formatCurrency = (amount) => {
    if (typeof amount !== 'number') return '$0.00';
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  console.log('🎨 Dashboard render state:', { loading, error, hasData: !!data });

  // Loading State
  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 p-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center">
            <h1 className="text-3xl font-bold text-gray-900 mb-4">Loading Dashboard...</h1>
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
          </div>
        </div>
      </div>
    );
  }

  // Error State
  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 p-6 flex items-center justify-center">
        <div className="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full text-center">
          <div className="text-6xl mb-4">😞</div>
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Error</h2>
          <p className="text-gray-600 mb-6">{error}</p>
          <button 
            onClick={fetchDashboardData}
            className="px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl"
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  // No Data State
  if (!data) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 p-6 flex items-center justify-center">
        <div className="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full text-center">
          <div className="text-6xl mb-4">📊</div>
          <h2 className="text-2xl font-bold text-gray-900 mb-4">No Data Available</h2>
          <p className="text-gray-600 mb-6">Start by adding your first transaction to see your financial dashboard.</p>
          <button 
            onClick={() => window.location.href = '/add-transaction'}
            className="px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl"
          >
            Add Transaction
          </button>
        </div>
      </div>
    );
  }

  // Main Dashboard
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50">
      {/* Header */}
      <div className="bg-white/90 backdrop-blur-md border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">Financial Dashboard</h1>
              <p className="text-gray-600 mt-1">Track your money, grow your wealth</p>
            </div>
            <div className="flex items-center space-x-4">
              <button 
                onClick={() => navigate('/add-transaction')}
                className="px-4 py-2 bg-emerald-600 text-white font-semibold rounded-xl shadow-md hover:shadow-lg hover:bg-emerald-700"
              >
                Add Transaction
              </button>
              <button 
                onClick={() => navigate('/history')}
                className="px-4 py-2 bg-blue-600 text-white font-semibold rounded-xl shadow-md hover:shadow-lg hover:bg-blue-700"
              >
                History
              </button>
              <button 
                onClick={fetchDashboardData}
                className="px-4 py-2 bg-white/80 backdrop-blur-md text-gray-700 font-semibold rounded-xl shadow-md hover:shadow-lg border border-gray-200"
              >
                Refresh
              </button>
              <button 
                onClick={handleLogout}
                className="px-4 py-2 bg-red-600 text-white font-semibold rounded-xl shadow-md hover:shadow-lg hover:bg-red-700"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto p-6">
        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div className="bg-white rounded-2xl shadow-xl p-6">
            <h3 className="text-sm font-semibold text-gray-600 mb-2">Total Income</h3>
            <div className="text-3xl font-bold text-emerald-600">{formatCurrency(data.total_income)}</div>
          </div>
          
          <div className="bg-white rounded-2xl shadow-xl p-6">
            <h3 className="text-sm font-semibold text-gray-600 mb-2">Total Expenses</h3>
            <div className="text-3xl font-bold text-red-600">{formatCurrency(data.total_expenses)}</div>
          </div>
          
          <div className="bg-white rounded-2xl shadow-xl p-6">
            <h3 className="text-sm font-semibold text-gray-600 mb-2">Savings</h3>
            <div className="text-3xl font-bold text-blue-600">{formatCurrency(data.savings || 0)}</div>
          </div>
          
          <div className="bg-white rounded-2xl shadow-xl p-6">
            <h3 className="text-sm font-semibold text-gray-600 mb-2">Savings Rate</h3>
            <div className="text-3xl font-bold text-purple-600">{data.savings_rate?.toFixed(1) || 0}%</div>
          </div>
        </div>

        {/* Debug Info */}
        <div className="bg-white rounded-2xl shadow-xl p-6">
          <h3 className="text-lg font-bold text-gray-900 mb-4">Debug Information</h3>
          <div className="space-y-2 text-sm">
            <div><strong>Total Income:</strong> {data.total_income}</div>
            <div><strong>Total Expenses:</strong> {data.total_expenses}</div>
            <div><strong>Savings:</strong> {data.savings}</div>
            <div><strong>Savings Rate:</strong> {data.savings_rate}</div>
            <div><strong>Expenses Categories:</strong> {data.expenses_by_category?.length || 0}</div>
            <div><strong>Monthly Trend:</strong> {data.monthly_trend?.length || 0}</div>
            <div><strong>Recent Transactions:</strong> {data.recent_transactions?.length || 0}</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
