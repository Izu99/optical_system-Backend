# app/crud/billing.py

from sqlalchemy.orm import Session
from app.models.billing import Billing
from app.schemas.billing import BillingCreate, BillingUpdate

from sqlalchemy.orm import Session
from app.models.billing import Billing
from app.schemas.billing import BillingCreate

def create_billing(db: Session, billing: BillingCreate):
    db_billing = Billing(
        delivery_date=billing.delivery_date,
        invoice_date=billing.invoice_date,
        invoice_time=billing.invoice_time,
        delivery_time=billing.delivery_time,
        sales_person=billing.sales_person,
        customer_id=billing.customer_id,
    )
    db.add(db_billing)
    db.commit()
    db.refresh(db_billing)
    return db_billing

def get_billing(db: Session, billing_id: int):
    return db.query(Billing).filter(Billing.billing_id == billing_id).first()

def get_billings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Billing).offset(skip).limit(limit).all()


def update_billing(db: Session, billing_id: int, billing: BillingUpdate):
    db_billing = db.query(Billing).filter(Billing.billing_id == billing_id).first()
    if db_billing is None:
        return None
    for var, value in vars(billing).items():
        setattr(db_billing, var, value) if value else None
    db.commit()
    db.refresh(db_billing)
    return db_billing

def delete_billing(db: Session, billing_id: int):
    db_billing = db.query(Billing).filter(Billing.billing_id == billing_id).first()
    if db_billing:
        db.delete(db_billing)
        db.commit()
    return db_billing
