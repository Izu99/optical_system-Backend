# app/models/frame.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Frame(Base):
    __tablename__ = "frames"

    frame_id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(255))
    size = Column(String(50))
    whole_sale_price = Column(Float)
    color = Column(String(50))
    model = Column(String(100))
    selling_price = Column(Float)
    stock = Column(Integer)
    branch_id = Column(Integer, ForeignKey("branches.branch_id"))

    branch = relationship("Branch", back_populates="frames")
    billing_items = relationship("BillingItem", back_populates="frame")
