from pydantic import BaseModel
from datetime import datetime

class PasswordRecoveryBase(BaseModel):
    user_id: int
    reset_token: str
    expires_at: datetime

class PasswordRecoveryCreate(PasswordRecoveryBase):
    pass

class PasswordRecovery(PasswordRecoveryBase):
    recovery_id: int
    created_at: datetime

    class Config:
        orm_mode = True