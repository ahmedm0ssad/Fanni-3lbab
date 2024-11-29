from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime


class Favorite(Base):
    __tablename__ = 'favorites'

    favorite_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    customer = relationship("User", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])
