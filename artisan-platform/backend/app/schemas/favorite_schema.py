from pydantic import BaseModel
from datetime import datetime

class FavoriteBase(BaseModel):
    customer_id: int
    artisan_id: int

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    favorite_id: int
    created_at: datetime

    class Config:
        orm_mode = True