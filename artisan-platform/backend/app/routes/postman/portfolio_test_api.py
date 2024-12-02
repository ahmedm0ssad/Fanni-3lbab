from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
portfolio_bp = Blueprint('portfolio_bp', __name__)

# Mock Schema and Database Session
class PortfolioCreate:
    def __init__(self, artisan_id, image_url, description=None):
        self.artisan_id = artisan_id
        self.image_url = image_url
        self.description = description

# Mock Functions
def create_portfolio(db, portfolio):
    return {
        "portfolio_id": 1,
        "artisan_id": portfolio.artisan_id,
        "image_url": portfolio.image_url,
        "description": portfolio.description,
        "created_at": "2024-12-01T15:30:00",
    }

def get_portfolios(db, skip, limit):
    return [
        {
            "portfolio_id": 1,
            "artisan_id": 1,
            "image_url": "http://example.com/image.jpg",
            "description": "Sample portfolio",
            "created_at": "2024-12-01T15:30:00",
        }
    ]

def get_portfolio(db, portfolio_id):
    if portfolio_id == 1:
        return {
            "portfolio_id": 1,
            "artisan_id": 1,
            "image_url": "http://example.com/image.jpg",
            "description": "Sample portfolio",
            "created_at": "2024-12-01T15:30:00",
        }
    return None

# Mock Database Session
class MockDB:
    pass

def get_db():
    db = MockDB()
    yield db

# Define Routes
@portfolio_bp.route('/portfolios', methods=['POST'])
def create_new_portfolio():
    db = next(get_db())
    portfolio_data = request.get_json()
    portfolio = PortfolioCreate(**portfolio_data)
    new_portfolio = create_portfolio(db=db, portfolio=portfolio)
    return jsonify(new_portfolio), 201

@portfolio_bp.route('/portfolios', methods=['GET'])
def read_portfolios():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    portfolios = get_portfolios(db, skip=skip, limit=limit)
    return jsonify(portfolios), 200

@portfolio_bp.route('/portfolios/<int:portfolio_id>', methods=['GET'])
def read_portfolio(portfolio_id):
    db = next(get_db())
    db_portfolio = get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        return jsonify({"detail": "Portfolio not found"}), 404
    return jsonify(db_portfolio), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(portfolio_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)