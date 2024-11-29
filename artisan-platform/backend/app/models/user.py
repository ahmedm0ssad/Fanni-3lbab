from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    user_type = Column(String, nullable=False)  # 'customer', 'artisan', 'admin'
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    services = relationship("Service", back_populates="artisan")
    bookings = relationship("Booking", back_populates="customer", foreign_keys="Booking.customer_id")
    reviews = relationship("RatingAndReview", back_populates="customer", foreign_keys="RatingAndReview.customer_id")
    notifications = relationship("Notification", back_populates="user")
    password_recovery = relationship("PasswordRecovery", back_populates="user")


class Admin(User):
    __tablename__ = 'admins'

    admin_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    # Inherits other fields from User
