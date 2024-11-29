from pydantic import BaseModel
from datetime import datetime

class PortfolioBase(BaseModel):
    artisan_id: int
    image_url: str
    description: str = None

class PortfolioCreate(PortfolioBase):
    pass

class Portfolio(PortfolioBase):
    portfolio_id: int
    created_at: datetime

    class Config:
        orm_mode = True