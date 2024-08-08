from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    billing_id: int
    advance_paid: float
    balance_amount: float
    total_amount: float
    discount: float
    fitting_charges: float
    grand_total: float
    payment_type: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    pass

class Payment(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True
