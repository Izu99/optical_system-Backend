# app/models/shop.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Shop(Base):
    __tablename__ = "shops"

    shop_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_number = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    headoffice_address = Column(String, index=True)

    branches = relationship("Branch", back_populates="shop")
