from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime


class RatingAndReview(Base):
    __tablename__ = 'ratings_and_reviews'

    review_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    customer = relationship("User", back_populates="reviews", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])
