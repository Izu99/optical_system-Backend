# app/models/prescription.py

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Prescription(Base):
    __tablename__ = "prescriptions"
    
    prescription_id = Column(Integer, primary_key=True, index=True)
    left_pd = Column(Float, nullable=False)
    right_pd = Column(Float, nullable=False)
    right_add = Column(Float, nullable=True)
    left_add = Column(Float, nullable=True)
    left_axis = Column(Float, nullable=True)
    left_sph = Column(Float, nullable=True)
    right_axis = Column(Float, nullable=True)
    right_cyl = Column(Float, nullable=True)
    right_sph = Column(Float, nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    
    customer = relationship("Customer", back_populates="prescriptions")
