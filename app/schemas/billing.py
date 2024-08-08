# app/schemas/billing.py

from datetime import date
from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class BillingBase(BaseModel):
    delivery_date: date
    invoice_date: date
    invoice_time: Optional[time]
    delivery_time: Optional[time]
    sales_person: str
    customer_id: int

class BillingCreate(BillingBase):
    pass

class BillingUpdate(BillingBase):
    pass

class Billing(BillingBase):
    billing_id: int

    class Config:
        orm_mode = True
