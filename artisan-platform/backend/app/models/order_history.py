from sqlalchemy import Column, Integer, Decimal, String, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime


class OrderHistory(Base):
    __tablename__ = 'order_history'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    amount_paid = Column(Decimal, nullable=False)
    payment_status = Column(String, nullable=False)  # paid, pending, failed
    transaction_date = Column(DateTime, default=datetime.utcnow)

    # Relationships
    booking = relationship("Booking")
    customer = relationship("User", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])
