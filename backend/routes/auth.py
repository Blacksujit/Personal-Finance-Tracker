from fastapi import APIRouter, HTTPException, status
from models.user import UserCreate, UserLogin, Token, UserResponse
from controllers.auth_controller import create_user, authenticate_user

auth_router = APIRouter()

@auth_router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    created_user, error = create_user(user)
    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )
    return created_user

@auth_router.post("/login", response_model=dict)
async def login(user_credentials: UserLogin):
    result = authenticate_user(user_credentials.email, user_credentials.password)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return result
