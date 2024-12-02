from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
rating_bp = Blueprint('rating_bp', __name__)

# Mock Schema and Database Session
class RatingCreate:
    def __init__(self, customer_id, artisan_id, rating, review=None):
        self.customer_id = customer_id
        self.artisan_id = artisan_id
        self.rating = rating
        self.review = review

# Mock Functions
def create_rating(db, rating):
    return {
        "review_id": 1,
        "customer_id": rating.customer_id,
        "artisan_id": rating.artisan_id,
        "rating": rating.rating,
        "review": rating.review,
        "created_at": "2024-12-01T15:30:00",
    }

def get_ratings(db, skip, limit):
    return [
        {
            "review_id": 1,
            "customer_id": 1,
            "artisan_id": 2,
            "rating": 5,
            "review": "Excellent service!",
            "created_at": "2024-12-01T15:30:00",
        }
    ]

def get_rating(db, review_id):
    if review_id == 1:
        return {
            "review_id": 1,
            "customer_id": 1,
            "artisan_id": 2,
            "rating": 5,
            "review": "Excellent service!",
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
@rating_bp.route('/ratings', methods=['POST'])
def create_new_rating():
    db = next(get_db())
    rating_data = request.get_json()
    rating = RatingCreate(**rating_data)
    new_rating = create_rating(db=db, rating=rating)
    return jsonify(new_rating), 201

@rating_bp.route('/ratings', methods=['GET'])
def read_ratings():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    ratings = get_ratings(db, skip=skip, limit=limit)
    return jsonify(ratings), 200

@rating_bp.route('/ratings/<int:review_id>', methods=['GET'])
def read_rating(review_id):
    db = next(get_db())
    db_rating = get_rating(db, review_id=review_id)
    if db_rating is None:
        return jsonify({"detail": "Rating not found"}), 404
    return jsonify(db_rating), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(rating_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)