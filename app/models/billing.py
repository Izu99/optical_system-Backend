from sqlalchemy import Column, Integer, DateTime, Time, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime, time
from app.database import Base

class Billing(Base):
    __tablename__ = 'billings'

    billing_id = Column(Integer, primary_key=True, index=True)
    delivery_date = Column(DateTime, default=datetime.utcnow)
    invoice_date = Column(DateTime, default=datetime.utcnow)
    invoice_time = Column(Time, nullable=True)
    delivery_time = Column(Time, nullable=True)
    sales_person = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))

    # Relationships
    customer = relationship("Customer", back_populates="billings")
    billing_items = relationship("BillingItem", back_populates="billing")
    payments = relationship("Payment", back_populates="billing")
