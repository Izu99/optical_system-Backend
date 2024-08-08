# app/schemas/customer.py

from pydantic import BaseModel, Field
from typing import Optional

class CustomerBase(BaseModel):
    contact_no: str
    branch_id: int
    full_name: str
    gender: str
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    contact_no: Optional[str] = None
    branch_id: Optional[int] = None
    full_name: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True
