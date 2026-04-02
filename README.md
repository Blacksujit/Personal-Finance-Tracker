# Personal Finance Tracker

A full-stack personal finance tracking application with React frontend and FastAPI backend.

## Tech Stack

**Frontend:**
- React 18 with Vite
- Tailwind CSS for styling
- Recharts for data visualization
- React Router for navigation
- Axios for API calls

**Backend:**
- FastAPI (Python)
- SQLite database
- JWT authentication
- bcrypt for password hashing
- CORS support

## Features

- **Authentication:** Secure signup/login with JWT tokens
- **Transaction Management:** Add, view, and delete transactions
- **Smart Insights:** Automated financial insights and warnings
- **Auto-Categorization:** Intelligent category suggestions based on descriptions
- **Dashboard:** Visual charts showing income vs expenses and spending patterns
- **Filtering:** Filter transactions by date, category, and type
- **CSV Export:** Download transaction data as CSV
- **Responsive Design:** Works on desktop and mobile devices

## Prerequisites

- Node.js 16+ and npm
- Python 3.8+
- pip (Python package manager)

## Setup Instructions

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd Personal-Finance-Tracker
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variable for JWT secret
# On Windows:
set JWT_SECRET=your-super-secret-jwt-key-here
# On macOS/Linux:
export JWT_SECRET=your-super-secret-jwt-key-here

# Start the backend server
python main.py
```

The backend will start on `http://localhost:8000`

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will start on `http://localhost:5173`

## Database Setup

The SQLite database is created automatically when you start the backend server. No manual database setup is required.

## Environment Variables

Required environment variable for the backend:

- `JWT_SECRET`: Secret key for JWT token signing (set this to a secure random string)

Example:
```bash
# Windows
set JWT_SECRET=my-super-secret-key-12345

# macOS/Linux
export JWT_SECRET=my-super-secret-key-12345
```

## Running the Application

1. Start the backend server (from `backend/` directory):
   ```bash
   python main.py
   ```

2. Start the frontend server (from `frontend/` directory):
   ```bash
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173`

## How to Use the App

1. **Sign up** for a new account or **login** with existing credentials
2. **Add transactions** from the sidebar menu
3. View your **dashboard** for insights and charts
4. Browse **transaction history** with filtering options
5. **Export** your data as CSV for further analysis

## Smart Features

### Auto-Categorization
The app automatically suggests categories based on transaction descriptions:
- Keywords like "uber", "taxi" → Transport
- Keywords like "zomato", "restaurant" → Food
- Keywords like "amazon", "shopping" → Shopping
- And more...

### Smart Insights
The dashboard provides intelligent insights:
- ⚠️ Spending warnings for high categories
- 💡 Savings rate recommendations
- 📈 Monthly spending trend analysis
- 🎉 Positive reinforcement for good financial habits

## API Endpoints

**Authentication:**
- `POST /api/auth/signup` - Create new user
- `POST /api/auth/login` - User login

**Transactions:**
- `GET /api/transactions` - Get user transactions (with filters)
- `POST /api/transactions` - Add new transaction
- `DELETE /api/transactions/{id}` - Delete transaction
- `GET /api/transactions/export` - Export transactions as CSV

**Dashboard:**
- `GET /api/dashboard` - Get dashboard data and insights

## Project Structure

```
Personal-Finance-Tracker/
├── backend/
│   ├── main.py              # FastAPI application entry point
│   ├── requirements.txt     # Python dependencies
│   ├── models/             # Database models
│   ├── routes/             # API routes
│   ├── controllers/        # Business logic
│   └── middleware/         # Authentication middleware
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── App.jsx         # Main app component
│   ├── package.json        # Node dependencies
│   └── tailwind.config.js  # Tailwind configuration
└── README.md               # This file
```

## Security Features

- JWT-based authentication
- Password hashing with bcrypt
- User data isolation (users can only see their own data)
- CORS configuration for frontend access
- Input validation and sanitization

## Troubleshooting

**Backend Issues:**
- Ensure Python 3.8+ is installed
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify JWT_SECRET environment variable is set

**Frontend Issues:**
- Ensure Node.js 16+ is installed
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Check that backend is running on port 8000

**Database Issues:**
- SQLite database file is created automatically
- If corrupted, delete `finance_tracker.db` and restart backend

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
