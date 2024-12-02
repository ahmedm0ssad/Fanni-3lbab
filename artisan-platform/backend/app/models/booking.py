from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class Booking(Base):
    """
    Booking class represents a booking made by a customer for a service provided by an artisan.

    Attributes:
        booking_id (int): The primary key for the booking.
        customer_id (int): The foreign key referencing the user who made the booking.
        service_id (int): The foreign key referencing the service being booked.
        artisan_id (int): The foreign key referencing the artisan providing the service.
        booking_date (datetime): The date and time when the booking is scheduled.
        status (str): The status of the booking (e.g., pending, confirmed, completed, canceled).
        created_at (datetime): The date and time when the booking was created.
    """

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