from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.config.database import Base

class OrderHistory(Base):
    __tablename__ = 'order_histories'

    order_id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'))
    customer_id = Column(Integer, ForeignKey('users.user_id'))
    artisan_id = Column(Integer, ForeignKey('users.user_id'))
    amount_paid = Column(DECIMAL)
    payment_status = Column(String(50))  # Specify length for VARCHAR column
    transaction_date = Column(DateTime)

    booking = relationship("Booking", back_populates="order_histories")
    customer = relationship("User", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])