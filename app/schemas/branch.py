from pydantic import BaseModel

class BranchBase(BaseModel):
    contact_number: str
    branch_code: str
    branch_name: str
    shop_id: int

class BranchCreate(BranchBase):
    pass

class Branch(BranchBase):
    branch_id: int

    class Config:
        orm_mode = True
