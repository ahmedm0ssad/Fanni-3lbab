from flask import Blueprint, request, jsonify
from app.schemas.portfolio_schema import PortfolioCreate
from app.services.portfolio_service import get_portfolio, get_portfolios, create_portfolio
from app.config.database import SessionLocal

portfolio_bp = Blueprint('portfolio_bp', __name__)

def get_db():
    """
    Provides a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@portfolio_bp.route('/portfolios', methods=['POST'])
def create_new_portfolio():
    """
    Create a new portfolio.
    """
    portfolio_data = request.get_json()
    portfolio = PortfolioCreate(**portfolio_data)
    with SessionLocal() as db:
        new_portfolio = create_portfolio(db=db, portfolio=portfolio)
    return jsonify(new_portfolio.to_dict()), 201  

@portfolio_bp.route('/portfolios', methods=['GET'])
def read_portfolios():
    """
    Retrieve all portfolios with optional pagination.
    """
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        portfolios = get_portfolios(db, skip=skip, limit=limit)
    return jsonify([portfolio.to_dict() for portfolio in portfolios]), 200  

@portfolio_bp.route('/portfolios/<int:portfolio_id>', methods=['GET'])
def read_portfolio(portfolio_id):
    """
    Retrieve a single portfolio by its ID.
    """
    with SessionLocal() as db:
        db_portfolio = get_portfolio(db, portfolio_id=portfolio_id)
        if db_portfolio is None:
            return jsonify({"detail": "Portfolio not found"}), 404
    return jsonify(db_portfolio.to_dict()), 200 
