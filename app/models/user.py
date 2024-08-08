from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from app.database import Base

class UserRole(str, Enum):
    owner = "owner"
    manager = "manager"
    optician = "optician"
    fitter = "fitter"

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True)
    branch_id = Column(Integer, ForeignKey('branches.branch_id'))
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # Define a composite unique constraint for owner and manager roles
    __table_args__ = (
        UniqueConstraint('branch_id', 'role', name='unique_branch_role'),
    )

    branch = relationship("Branch", back_populates="users")
