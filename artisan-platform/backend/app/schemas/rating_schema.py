from pydantic import BaseModel
from datetime import datetime

class RatingBase(BaseModel):
    customer_id: int
    artisan_id: int
    rating: int
    review: str = None

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    review_id: int
    created_at: datetime

    class Config:
        from_attributes = True