# app/models/branch.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Branch(Base):
    __tablename__ = "branches"

    branch_id = Column(Integer, primary_key=True, index=True)
    contact_number = Column(String, index=True)
    branch_code = Column(String, unique=True, index=True)
    branch_name = Column(String, index=True)
    shop_id = Column(Integer, ForeignKey('shops.shop_id'))

    shop = relationship("Shop", back_populates="branches")
    users = relationship("User", back_populates="branch")
    customers = relationship("Customer", back_populates="branch")
    frames = relationship("Frame", back_populates="branch")
    lenses = relationship("Lens", back_populates="branch")
