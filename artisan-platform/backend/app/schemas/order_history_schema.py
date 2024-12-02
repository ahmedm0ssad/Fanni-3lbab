from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class OrderHistoryBase(BaseModel):
    booking_id: int
    customer_id: int
    artisan_id: int
    amount_paid: Decimal
    payment_status: str

class OrderHistoryCreate(OrderHistoryBase):
    pass

class OrderHistory(OrderHistoryBase):
    order_id: int
    transaction_date: datetime

    class Config:
        from_attributes = True