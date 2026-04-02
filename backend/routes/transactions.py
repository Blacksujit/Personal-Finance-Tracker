from fastapi import APIRouter, HTTPException, status, Depends, Query
from fastapi.responses import StreamingResponse
from models.transaction import TransactionCreate, TransactionResponse, TransactionFilter
from middleware.auth import verify_token
from controllers.transaction_controller import (
    create_transaction, 
    get_user_transactions, 
    delete_transaction,
    export_transactions_csv,
    get_dashboard_data
)
from typing import List, Optional

transactions_router = APIRouter()

@transactions_router.post("/transactions", response_model=TransactionResponse)
async def create_new_transaction(
    transaction: TransactionCreate,
    user_id: int = Depends(verify_token)
):
    result, error = create_transaction(transaction, user_id)
    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )
    return result

@transactions_router.get("/transactions", response_model=List[TransactionResponse])
async def get_transactions(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    user_id: int = Depends(verify_token)
):
    filters = TransactionFilter(
        start_date=start_date,
        end_date=end_date,
        category=category,
        type=type
    )
    result, error = get_user_transactions(user_id, filters)
    if error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error
        )
    return result

@transactions_router.delete("/transactions/{transaction_id}")
async def delete_transaction_endpoint(
    transaction_id: int,
    user_id: int = Depends(verify_token)
):
    if delete_transaction(transaction_id, user_id):
        return {"message": "Transaction deleted successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

@transactions_router.get("/transactions/export")
async def export_transactions(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    user_id: int = Depends(verify_token)
):
    filters = TransactionFilter(
        start_date=start_date,
        end_date=end_date,
        category=category,
        type=type
    )
    
    csv_data, error = export_transactions_csv(user_id, filters)
    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )
    
    return StreamingResponse(
        iter([csv_data]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=transactions.csv"}
    )

@transactions_router.get("/dashboard")
async def get_dashboard(
    user_id: int = Depends(verify_token)
):
    data, error = get_dashboard_data(user_id)
    if error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error
        )
    return data
