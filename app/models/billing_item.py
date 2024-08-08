# app/models/billing_item.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class BillingItem(Base):
    __tablename__ = "billing_items"
    billing_item_id = Column(Integer, primary_key=True, index=True)
    billing_id = Column(Integer, ForeignKey(
        "billings.billing_id"), nullable=False)
    frame_id = Column(Integer, ForeignKey("frames.frame_id"), nullable=True)
    lens_id = Column(Integer, ForeignKey("lenses.lens_id"), nullable=True)
    lens_quantity = Column(Integer, nullable=False)
    frame_quantity = Column(Integer, nullable=False)

    billing = relationship("Billing", back_populates="billing_items")
    frame = relationship("Frame", back_populates="billing_items")
    lens = relationship("Lens", back_populates="billing_items")
