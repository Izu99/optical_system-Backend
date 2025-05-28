from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    contact_no: Optional[str] = None
    branch_id: Optional[int] = None
    full_name: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    full_name: str  # Required for create

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True
