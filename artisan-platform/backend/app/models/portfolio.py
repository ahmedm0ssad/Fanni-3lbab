from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Portfolio(Base):
    """
    Portfolio class represents a portfolio entry created by an artisan.

    Attributes:
        portfolio_id (int): The primary key for the portfolio entry.
        artisan_id (int): The foreign key referencing the artisan who created the portfolio.
        image_url (str): The URL of the image associated with the portfolio entry.
        description (str): The description of the portfolio entry.
        created_at (datetime): The date and time when the portfolio entry was created.
    """

    __tablename__ = 'portfolios'

    # Define columns
    portfolio_id = Column(Integer, primary_key=True, autoincrement=True)
    artisan_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    image_url = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Define relationships
    artisan = relationship("User", back_populates="portfolios")

    def to_dict(self):
        return {
            "portfolio_id": self.portfolio_id,
            "artisan_id": self.artisan_id,
            "image_url": self.image_url,
            "description":self.description,
            "created_at": self.created_at,
            
        }
