from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class User(Base):
    """
    User class represents a user in the system.

    Attributes:
        user_id (int): The primary key for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        password_hash (str): The hashed password of the user.
        phone (str): The phone number of the user.
        address (str): The address of the user.
        user_type (str): The type of the user (e.g., customer, artisan, admin).
        created_at (datetime): The date and time when the user was created.
        updated_at (datetime): The date and time when the user was last updated.
    """

    __tablename__ = 'users'

    # Define columns
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    user_type = Column(String, nullable=False)  # 'customer', 'artisan', 'admin'
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define relationships
    services = relationship("Service", back_populates="artisan")
    bookings = relationship("Booking", back_populates="customer", foreign_keys="Booking.customer_id")
    reviews = relationship("RatingAndReview", back_populates="customer", foreign_keys="RatingAndReview.customer_id")
    notifications = relationship("Notification", back_populates="user")
    password_recovery = relationship("PasswordRecovery", back_populates="user")

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password_hash":self.password_hash,
            "phone": self.phone,
            "address": self.address,
            "user_type": self.user_type,
            "created_at":self.created_at,
            "updated_at":self.updated_at,

        }


    

class Admin(User):
    """
    Admin class represents an admin user in the system.

    Attributes:
        admin_id (int): The primary key for the admin, referencing the user ID.
    """

    __tablename__ = 'admins'

    admin_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    # Inherits other fields from User

    def to_dict(self):
            return {
                "admin_id": self.admin_id,
            
            }

