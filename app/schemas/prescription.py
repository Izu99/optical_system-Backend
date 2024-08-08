# app/schemas/prescription.py

from pydantic import BaseModel
from typing import Optional

class PrescriptionBase(BaseModel):
    left_pd: float
    right_pd: float
    right_add: Optional[float] = None
    left_add: Optional[float] = None
    left_axis: Optional[float] = None
    left_sph: Optional[float] = None
    right_axis: Optional[float] = None
    right_cyl: Optional[float] = None
    right_sph: Optional[float] = None

class PrescriptionCreate(PrescriptionBase):
    customer_id: int

class PrescriptionUpdate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    prescription_id: int

    class Config:
        orm_mode = True
