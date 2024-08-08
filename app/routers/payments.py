from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.payment import Payment, PaymentCreate, PaymentUpdate
from app.crud.payment import get_payment, get_payments, create_payment, update_payment, delete_payment
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Payment)
def create_new_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db, payment)

@router.get("/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.get("/", response_model=list[Payment])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    payments = get_payments(db, skip=skip, limit=limit)
    return payments

@router.put("/{payment_id}", response_model=Payment)
def update_existing_payment(payment_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    db_payment = update_payment(db, payment_id, payment)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.delete("/{payment_id}", response_model=Payment)
def delete_existing_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = delete_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
