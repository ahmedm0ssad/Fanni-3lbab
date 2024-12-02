from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class RatingAndReview(Base):
    """
    RatingAndReview class represents a rating and review given by a customer to an artisan.

    Attributes:
        review_id (int): The primary key for the rating and review.
        customer_id (int): The foreign key referencing the customer who gave the rating and review.
        artisan_id (int): The foreign key referencing the artisan who received the rating and review.
        rating (int): The rating given by the customer.
        review (str): The review text provided by the customer.
        created_at (datetime): The date and time when the rating and review were created.
    """

    __tablename__ = 'ratings_and_reviews'

    # Define columns
    review_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Define relationships
    customer = relationship("User", back_populates="reviews", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])
