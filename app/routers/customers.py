# app/routers/customers.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from app.crud.customer import get_customer, get_customers, create_customer, update_customer, delete_customer
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=Customer)
def create_new_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.get("/{customer_id}", response_model=Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = get_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.get("/", response_model=list[Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customers = get_customers(db, skip=skip, limit=limit)
    return customers

@router.put("/{customer_id}", response_model=Customer)
def update_existing_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = update_customer(db, customer_id, customer)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.delete("/{customer_id}", response_model=Customer)
def delete_existing_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = delete_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer
