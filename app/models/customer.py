# app/models/customer.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    customer_id = Column(Integer, primary_key=True, index=True)
    contact_no = Column(String(45))
    branch_id = Column(Integer, ForeignKey("branches.branch_id"))
    full_name = Column(String(255))
    gender = Column(String(45))
    address = Column(String(255))
    
    branch = relationship("Branch", back_populates="customers")
    prescriptions = relationship("Prescription", back_populates="customer")
    billings = relationship("Billing", back_populates="customer")
