from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    owner = "owner"
    manager = "manager"
    optician = "optician"
    fitter = "fitter"

class UserBase(BaseModel):
    role: UserRole
    branch_id: int
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    role: UserRole = None
    branch_id: int = None
    email: EmailStr = None
    password: str = None

class UserResponse(BaseModel):
    user_id: int
    role: UserRole
    branch_id: int
    email: EmailStr

    class Config:
        orm_mode = True
