from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'))
    service_id = Column(Integer, ForeignKey('services.service_id'))
    artisan_id = Column(Integer, ForeignKey('users.user_id'))
    booking_date = Column(DateTime)
    status = Column(String(20))
    created_at = Column(DateTime)

    customer = relationship("User", foreign_keys=[customer_id])
    service = relationship("Service", back_populates="bookings")
    artisan = relationship("User", foreign_keys=[artisan_id])
    order_histories = relationship("OrderHistory", back_populates="booking")