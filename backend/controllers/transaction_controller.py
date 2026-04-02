import sqlite3
import re
import csv
from io import StringIO
from datetime import datetime, timedelta
from models.database import get_db_connection
from models.transaction import TransactionCreate, TransactionResponse, TransactionFilter

def suggest_category(description: str) -> str:
    """Auto-suggest category based on description keywords"""
    if not description:
        return "Other"
    
    description_lower = description.lower()
    
    # Enhanced keyword mappings for better categorization
    category_keywords = {
        "Transport": [
            "uber", "taxi", "lyft", "bus", "train", "metro", "subway", "gas", "petrol", 
            "parking", "toll", "car", "vehicle", "auto", "cab", "ride", "transport"
        ],
        "Food": [
            "zomato", "swiggy", "restaurant", "pizza", "burger", "cafe", "coffee", 
            "grocery", "supermarket", "food", "meal", "dining", "eat", "drink", 
            "bar", "pub", "bakery", "deli"
        ],
        "Shopping": [
            "amazon", "flipkart", "walmart", "target", "mall", "clothing", "shoes", 
            "fashion", "electronics", "gadgets", "purchase", "buy", "store", "shop", 
            "retail", "online shopping"
        ],
        "Entertainment": [
            "netflix", "spotify", "movie", "cinema", "concert", "game", "gaming", 
            "streaming", "subscription", "entertainment", "fun", "leisure", "hobby"
        ],
        "Bills": [
            "electricity", "water", "internet", "phone", "rent", "insurance", 
            "mortgage", "loan", "emi", "bill", "utility", "tax", "cable"
        ],
        "Healthcare": [
            "hospital", "doctor", "pharmacy", "medicine", "clinic", "health", 
            "medical", "dental", "vision", "fitness", "gym", "wellness"
        ],
        "Education": [
            "course", "book", "tuition", "school", "college", "university", 
            "education", "learning", "training", "certification", "study"
        ],
        "Travel": [
            "flight", "hotel", "booking", "travel", "vacation", "trip", "holiday", 
            "airbnb", "expedia", "booking.com", "airline", "airport"
        ]
    }
    
    # Calculate category scores
    category_scores = {}
    for category, keywords in category_keywords.items():
        score = 0
        for keyword in keywords:
            if keyword in description_lower:
                score += 1
        if score > 0:
            category_scores[category] = score
    
    # Return category with highest score
    if category_scores:
        return max(category_scores, key=category_scores.get)
    
    return "Other"

def validate_transaction_data(transaction: TransactionCreate) -> tuple[bool, str]:
    """Validate transaction data"""
    if not transaction.amount or transaction.amount <= 0:
        return False, "Amount must be greater than 0"
    
    if transaction.amount > 999999999:
        return False, "Amount seems too large"
    
    if transaction.type not in ['income', 'expense']:
        return False, "Type must be either 'income' or 'expense'"
    
    # Validate date format
    try:
        datetime.strptime(transaction.date, '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"
    
    # Check if date is not too far in future
    transaction_date = datetime.strptime(transaction.date, '%Y-%m-%d').date()
    if transaction_date > datetime.now().date() + timedelta(days=30):
        return False, "Date cannot be more than 30 days in the future"
    
    if transaction_date < datetime.now().date() - timedelta(days=365 * 5):
        return False, "Date cannot be more than 5 years in the past"
    
    return True, ""

def create_transaction(transaction: TransactionCreate, user_id: int) -> tuple[TransactionResponse | None, str]:
    """Create a new transaction with validation"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Validate transaction data
        is_valid, error_message = validate_transaction_data(transaction)
        if not is_valid:
            return None, error_message
        
        # Auto-suggest category if not provided or if it's "Other"
        category = transaction.category
        if not category or category.lower() == "other":
            category = suggest_category(transaction.description or "")
        
        # Insert transaction
        cursor.execute(
            """
            INSERT INTO transactions (user_id, amount, category, type, date, description)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (user_id, transaction.amount, category, transaction.type, transaction.date, transaction.description)
        )
        conn.commit()
        
        # Get created transaction
        cursor.execute(
            """
            SELECT id, user_id, amount, category, type, date, description, created_at
            FROM transactions WHERE id = ?
            """,
            (cursor.lastrowid,)
        )
        transaction_data = cursor.fetchone()
        
        if transaction_data:
            return TransactionResponse(**transaction_data), None
        return None, "Failed to create transaction"
        
    except sqlite3.Error as e:
        conn.rollback()
        return None, f"Database error: {str(e)}"
    except Exception as e:
        conn.rollback()
        return None, f"Unexpected error: {str(e)}"
    finally:
        conn.close()

def get_user_transactions(user_id: int, filters: TransactionFilter = None) -> tuple[list[TransactionResponse], str]:
    """Get user transactions with filtering"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = "SELECT * FROM transactions WHERE user_id = ?"
        params = [user_id]
        
        if filters:
            if filters.start_date:
                query += " AND date >= ?"
                params.append(filters.start_date)
            if filters.end_date:
                query += " AND date <= ?"
                params.append(filters.end_date)
            if filters.category:
                query += " AND category = ?"
                params.append(filters.category)
            if filters.type:
                query += " AND type = ?"
                params.append(filters.type)
        
        query += " ORDER BY date DESC, created_at DESC"
        
        cursor.execute(query, params)
        transactions = cursor.fetchall()
        
        return [TransactionResponse(**transaction) for transaction in transactions], ""
        
    except sqlite3.Error as e:
        return [], f"Database error: {str(e)}"
    except Exception as e:
        return [], f"Unexpected error: {str(e)}"
    finally:
        conn.close()

def delete_transaction(transaction_id: int, user_id: int) -> tuple[bool, str]:
    """Delete a transaction with validation"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check if transaction exists and belongs to user
        cursor.execute(
            "SELECT id FROM transactions WHERE id = ? AND user_id = ?",
            (transaction_id, user_id)
        )
        if not cursor.fetchone():
            return False, "Transaction not found or access denied"
        
        # Delete transaction
        cursor.execute(
            "DELETE FROM transactions WHERE id = ? AND user_id = ?",
            (transaction_id, user_id)
        )
        conn.commit()
        
        return cursor.rowcount > 0, ""
        
    except sqlite3.Error as e:
        conn.rollback()
        return False, f"Database error: {str(e)}"
    except Exception as e:
        conn.rollback()
        return False, f"Unexpected error: {str(e)}"
    finally:
        conn.close()

def export_transactions_csv(user_id: int, filters: TransactionFilter = None) -> tuple[str, str]:
    """Export transactions to CSV"""
    try:
        transactions, error = get_user_transactions(user_id, filters)
        if error:
            return "", error
        
        if not transactions:
            return "", "No transactions found"
        
        output = StringIO()
        writer = csv.writer(output)
        
        # Write header
        writer.writerow(['Date', 'Description', 'Category', 'Type', 'Amount'])
        
        # Write transactions
        for transaction in transactions:
            writer.writerow([
                transaction.date,
                transaction.description or '',
                transaction.category,
                transaction.type,
                transaction.amount
            ])
        
        output.seek(0)
        return output.getvalue(), ""
        
    except Exception as e:
        return "", f"Export error: {str(e)}"

def get_dashboard_data(user_id: int) -> tuple[dict, str]:
    """Get comprehensive dashboard data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Get total income and expenses
        cursor.execute(
            """
            SELECT type, SUM(amount) as total
            FROM transactions 
            WHERE user_id = ?
            GROUP BY type
            """,
            (user_id,)
        )
        totals = cursor.fetchall()
        
        total_income = 0.0
        total_expenses = 0.0
        
        for row in totals:
            if row['type'] == 'income':
                total_income = row['total']
            elif row['type'] == 'expense':
                total_expenses = row['total']
        
        savings = total_income - total_expenses
        savings_rate = (savings / total_income * 100) if total_income > 0 else 0
        
        # Get expenses by category
        cursor.execute(
            """
            SELECT category, SUM(amount) as total
            FROM transactions 
            WHERE user_id = ? AND type = 'expense'
            GROUP BY category
            ORDER BY total DESC
            """,
            (user_id,)
        )
        expenses_by_category = [dict(row) for row in cursor.fetchall()]
        
        # Get monthly trend (last 12 months)
        cursor.execute(
            """
            SELECT 
                substr(date, 1, 7) as month,
                SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) as income,
                SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as expenses
            FROM transactions 
            WHERE user_id = ? AND date >= date('now', '-12 months')
            GROUP BY substr(date, 1, 7)
            ORDER BY month
            """,
            (user_id,)
        )
        monthly_trend = [dict(row) for row in cursor.fetchall()]
        
        # Get recent transactions (last 5)
        cursor.execute(
            """
            SELECT * FROM transactions 
            WHERE user_id = ? 
            ORDER BY date DESC, created_at DESC 
            LIMIT 5
            """,
            (user_id,)
        )
        recent_transactions = [TransactionResponse(**row) for row in cursor.fetchall()]
        
        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'savings': savings,
            'savings_rate': round(savings_rate, 2),
            'expenses_by_category': expenses_by_category,
            'monthly_trend': monthly_trend,
            'recent_transactions': recent_transactions,
            'total_transactions': len(recent_transactions)
        }, ""
        
    except sqlite3.Error as e:
        return {}, f"Database error: {str(e)}"
    except Exception as e:
        return {}, f"Unexpected error: {str(e)}"
    finally:
        conn.close()

def get_financial_insights(user_id: int) -> tuple[list[dict], str]:
    """Generate smart financial insights"""
    try:
        dashboard_data, error = get_dashboard_data(user_id)
        if error:
            return [], error
        
        insights = []
        
        # Spending insights
        if dashboard_data['expenses_by_category']:
            top_category = dashboard_data['expenses_by_category'][0]
            if top_category['total'] > dashboard_data['total_expenses'] * 0.4:
                insights.append({
                    'type': 'warning',
                    'title': 'High Spending Alert',
                    'message': f"You spent {round((top_category['total'] / dashboard_data['total_expenses']) * 100)}% of your expenses on {top_category['category']}",
                    'suggestion': f"Consider reviewing your {top_category['category']} spending habits."
                })
        
        # Savings rate insights
        if dashboard_data['savings_rate'] < 10:
            insights.append({
                'type': 'warning',
                'title': 'Low Savings Rate',
                'message': f"Your savings rate is {dashboard_data['savings_rate']}%",
                'suggestion': "Try to reduce expenses or increase income to improve your savings."
            })
        elif dashboard_data['savings_rate'] > 30:
            insights.append({
                'type': 'success',
                'title': 'Excellent Savings',
                'message': f"Great job! Your savings rate is {dashboard_data['savings_rate']}%",
                'suggestion': "Consider investing your savings for better returns."
            })
        
        # Monthly trend insights
        if len(dashboard_data['monthly_trend']) >= 2:
            last_month = dashboard_data['monthly_trend'][-1]
            previous_month = dashboard_data['monthly_trend'][-2]
            
            if last_month['expenses'] > previous_month['expenses'] * 1.2:
                increase_percent = round(((last_month['expenses'] - previous_month['expenses']) / previous_month['expenses']) * 100)
                insights.append({
                    'type': 'warning',
                    'title': 'Spending Increase',
                    'message': f"Your expenses increased by {increase_percent}% this month",
                    'suggestion': "Review your recent transactions to identify areas for cost reduction."
                })
        
        # Income insights
        if dashboard_data['total_income'] == 0:
            insights.append({
                'type': 'info',
                'title': 'No Income Recorded',
                'message': "You haven't recorded any income yet",
                'suggestion': "Start tracking your income to get a complete financial picture."
            })
        
        return insights, ""
        
    except Exception as e:
        return [], f"Insights error: {str(e)}"
