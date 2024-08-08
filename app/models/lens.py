from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Lens(Base):
    __tablename__ = "lenses"

    lens_id = Column(Integer, primary_key=True, index=True)
    power = Column(String, index=True)
    coating = Column(String)
    branch_id = Column(Integer, ForeignKey('branches.branch_id'))
    category = Column(String)
    cost = Column(Float)
    stock = Column(Integer)
    selling_price = Column(Float)

    branch = relationship("Branch", back_populates="lenses")
    billing_items = relationship("BillingItem", back_populates="lens")
