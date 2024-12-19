from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class Favorite(Base):
    """
    Favorite class represents a favorite artisan marked by a customer.

    Attributes:
        favorite_id (int): The primary key for the favorite.
        customer_id (int): The foreign key referencing the user who marked the favorite.
        artisan_id (int): The foreign key referencing the artisan marked as favorite.
        created_at (datetime): The date and time when the favorite was created.
    """

    __tablename__ = 'favorites'  # Name of the table in the database

    favorite_id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)  # Foreign key to the users table
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)  # Foreign key to the users table
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp of when the favorite was created

    # Relationships
    customer = relationship("User", foreign_keys=[customer_id])  # Relationship to the User model for the customer
    artisan = relationship("User", foreign_keys=[artisan_id])  # Relationship to the User model for the artisan
    def to_dict(self):
        return {
            "favorite_id": self.favorite_id,
            "customer_id": self.customer_id,
            "artisan_id": self.artisan_id,
            "created_at":self.created_at,

  
            
        }