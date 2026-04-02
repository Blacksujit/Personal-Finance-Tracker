from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionCreate(BaseModel):
    amount: float
    category: str
    type: str  # 'income' or 'expense'
    date: str
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    category: str
    type: str
    date: str
    description: Optional[str]
    created_at: str
    
    class Config:
        from_attributes = True

class TransactionFilter(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    category: Optional[str] = None
    type: Optional[str] = None
