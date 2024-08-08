from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    billing_id = Column(Integer, ForeignKey("billings.billing_id"), nullable=False)
    advance_paid = Column(DECIMAL(10, 2), nullable=False)
    balance_amount = Column(DECIMAL(10, 2), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    discount = Column(DECIMAL(10, 2), nullable=False)
    fitting_charges = Column(DECIMAL(10, 2), nullable=False)
    grand_total = Column(DECIMAL(10, 2), nullable=False)
    payment_type = Column(String(45), nullable=False)

    billing = relationship("Billing", back_populates="payments")
