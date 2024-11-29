from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime


class Portfolio(Base):
    __tablename__ = 'portfolios'

    portfolio_id = Column(Integer, primary_key=True, autoincrement=True)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    image_url = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    artisan = relationship("User", back_populates="portfolios")
