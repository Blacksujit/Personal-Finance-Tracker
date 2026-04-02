# Personal Finance Tracker

A full-stack personal finance tracking application with React frontend and FastAPI backend.


# Video Demo :

> ⚠️ Note: GitHub may disable direct `<video>` playback in README previews for security/sanitization reasons. Use the link below to open the video in your browser.

- [Open demo video](./video-demo/Recording%202026-04-02%20153948.mp4)
- [Download demo video](./video-demo/Recording%202026-04-02%20153948.mp4)

If you want inline playback locally (not on GitHub.com), keep this block in your local markdown viewer:
<!-- 
```html
<video controls>
  <source src="./video-demo/20260402-0928-59.7778076.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
``` -->

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

- Node.js 18+ and npm
- Python 3.11+ (tested)
- Git
- (Optional) SQLite browser if you want to inspect the local DB

## Setup Instructions

### 1. Clone and Navigate
```bash
git clone https://github.com/Blacksujit/Personal-Finance-Tracker.git
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

# Start the backend server
python main.py
```

The backend will start on:

- `http://localhost:8003`
- API base URL used by the frontend: `http://localhost:8003/api`

#### Backend Environment Variables

The backend will run without env vars, but for a real setup you should set:

- `JWT_SECRET` (recommended): used to sign JWTs

Windows (PowerShell):
```powershell
$env:JWT_SECRET="replace-with-a-long-random-string"
```

macOS/Linux (bash/zsh):
```bash
export JWT_SECRET="replace-with-a-long-random-string"
```

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

#### Frontend Environment Variables

The frontend reads the API base URL from `VITE_API_URL`.

- If `VITE_API_URL` is not set, it defaults to `http://localhost:8003/api`.

To override locally, create `frontend/.env.local`:
```bash
VITE_API_URL=http://localhost:8003/api
```

## Database Setup

The SQLite database is created automatically when you start the backend server. No manual database setup is required.

## Environment Variables

Required environment variable for the backend:

- `JWT_SECRET`: Secret key for JWT token signing (recommended to set a secure random string)

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

## Default Ports

- **Backend**: `8003`
- **Frontend**: `5173` (Vite may pick another free port if 5173 is already in use)

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
- If auth tokens are invalid after restart, set `JWT_SECRET` to a fixed value (otherwise the default secret will be used)
- If you see a port error like `address already in use`, stop the other process using port `8003` or change the port in `backend/main.py`

**Frontend Issues:**
- Ensure Node.js 16+ is installed
- Reinstall deps if needed: delete `frontend/node_modules` and run `npm install`
- Check that backend is running on `http://localhost:8003`
- If Vite uses a different port (e.g. 5174), the backend CORS list in `backend/main.py` must include that port

**Database Issues:**
- SQLite database file is created automatically
- If corrupted, delete `finance_tracker.db` and restart backend

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
