from pydantic import BaseModel

class AdminBase(BaseModel):
    user_id: int

class AdminCreate(AdminBase):
    pass

class Admin(AdminBase):
    admin_id: int

    class Config:
        from_attributes = True