import bcrypt
import re
from models.database import get_db_connection
from models.user import UserCreate, UserResponse
from datetime import datetime, timedelta
from middleware.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

# Password validation
def validate_password(password: str) -> tuple[bool, str]:
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if len(password) > 72:
        return False, "Password must be less than 72 characters long"
    if not re.search(r"[A-Za-z]", password):
        return False, "Password must contain at least one letter"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, ""

def validate_email(email: str) -> tuple[bool, str]:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Invalid email format"
    return True, ""

def hash_password(password: str) -> str:
    """Hash password using bcrypt directly"""
    # Convert to bytes and ensure it's not longer than 72 bytes
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    try:
        plain_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_bytes, hashed_bytes)
    except Exception:
        return False

def create_user(user: UserCreate) -> tuple[UserResponse | None, str]:
    """Create a new user with proper validation"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Validate email
        is_valid_email, email_error = validate_email(user.email)
        if not is_valid_email:
            return None, email_error
        
        # Validate password
        is_valid_password, password_error = validate_password(user.password)
        if not is_valid_password:
            return None, password_error
        
        # Check if user already exists
        cursor.execute("SELECT id FROM users WHERE email = ?", (user.email.lower(),))
        if cursor.fetchone():
            return None, "User with this email already exists"
        
        # Create new user
        hashed_password = hash_password(user.password)
        cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (user.email.lower(), hashed_password)
        )
        conn.commit()
        
        # Get created user
        cursor.execute("SELECT id, email FROM users WHERE email = ?", (user.email.lower(),))
        user_data = cursor.fetchone()
        
        if user_data:
            return UserResponse(id=user_data["id"], email=user_data["email"]), None
        return None, "Failed to create user"
        
    except Exception as e:
        conn.rollback()
        return None, f"Database error: {str(e)}"
    finally:
        conn.close()

def authenticate_user(email: str, password: str) -> dict | None:
    """Authenticate user with credentials"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Validate email format
        is_valid_email, email_error = validate_email(email)
        if not is_valid_email:
            return None
        
        cursor.execute(
            "SELECT id, email, password_hash FROM users WHERE email = ?", 
            (email.lower(),)
        )
        user_data = cursor.fetchone()
        
        if not user_data:
            return None
        
        if not verify_password(password, user_data["password_hash"]):
            return None
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user_data["id"])}, 
            expires_delta=access_token_expires
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": UserResponse(id=user_data["id"], email=user_data["email"])
        }
        
    except Exception as e:
        return None
    finally:
        conn.close()
