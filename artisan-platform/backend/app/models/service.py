from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class Service(Base):
    """
    Service class represents a service provided by an artisan.

    Attributes:
        service_id (int): The primary key for the service.
        artisan_id (int): The foreign key referencing the artisan providing the service.
        service_name (str): The name of the service.
        description (str): The description of the service.
        price (float): The price of the service.
        category (str): The category of the service.
        created_at (datetime): The date and time when the service was created.
        updated_at (datetime): The date and time when the service was last updated.
    """

    __tablename__ = 'services'

    # Define columns
    service_id = Column(Integer, primary_key=True, autoincrement=True)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    service_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define relationships
    artisan = relationship("User", back_populates="services")
    bookings = relationship("Booking", back_populates="service")
