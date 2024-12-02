from pydantic import BaseModel
from datetime import datetime

class BookingBase(BaseModel):
    customer_id: int
    service_id: int
    artisan_id: int
    booking_date: datetime
    status: str = 'pending'

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    booking_id: int
    created_at: datetime

    class Config:
        from_attributes = True