from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime


class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.service_id'), nullable=False)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    booking_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False, default='pending')  # pending, confirmed, completed, canceled
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    customer = relationship("User", back_populates="bookings", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])
    service = relationship("Service", back_populates="bookings")
