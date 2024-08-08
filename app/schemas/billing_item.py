# app/schemas/billing_item.py
from pydantic import BaseModel
from typing import Optional

class BillingItemBase(BaseModel):
    billing_id: int
    frame_id: Optional[int] = None
    lens_id: Optional[int] = None
    lens_quantity: int
    frame_quantity: int

class BillingItemCreate(BillingItemBase):
    pass

class BillingItemUpdate(BillingItemBase):
    pass

class BillingItem(BillingItemBase):
    billing_item_id: int

    class Config:
        orm_mode = True
