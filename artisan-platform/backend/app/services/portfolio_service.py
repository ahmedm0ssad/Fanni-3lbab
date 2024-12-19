from sqlalchemy.orm import Session
from app.models.portfolio import Portfolio
from app.schemas.portfolio_schema import PortfolioCreate

def get_portfolio(db: Session, portfolio_id: int):
    """
    Retrieve a specific portfolio entry by its ID.
    """
    return db.query(Portfolio).filter(Portfolio.portfolio_id == portfolio_id).first()

def get_portfolios(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of portfolio entries with optional pagination.
    """
    return db.query(Portfolio).offset(skip).limit(limit).all()

def create_portfolio(db: Session, portfolio: PortfolioCreate):
    """
    Create a new portfolio entry for an artisan.
    """
    db_portfolio = Portfolio(
        artisan_id=portfolio.artisan_id,
        image_url=portfolio.image_url,
        description=portfolio.description
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio
