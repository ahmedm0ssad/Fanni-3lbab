from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
favorite_bp = Blueprint('favorite_bp', __name__)

# Mock Schema and Database Session
class FavoriteCreate:
    def __init__(self, customer_id, artisan_id):
        self.customer_id = customer_id
        self.artisan_id = artisan_id

# Mock Functions
def create_favorite(db, favorite):
    return {
        "favorite_id": 1,
        "customer_id": favorite.customer_id,
        "artisan_id": favorite.artisan_id,
        "created_at": "2024-12-01T15:30:00",
    }

def get_favorites(db, skip, limit):
    return [
        {
            "favorite_id": 1,
            "customer_id": 1,
            "artisan_id": 2,
            "created_at": "2024-12-01T15:30:00",
        }
    ]

def get_favorite(db, favorite_id):
    if favorite_id == 1:
        return {
            "favorite_id": 1,
            "customer_id": 1,
            "artisan_id": 2,
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
@favorite_bp.route('/favorites', methods=['POST'])
def create_new_favorite():
    db = next(get_db())
    favorite_data = request.get_json()
    favorite = FavoriteCreate(**favorite_data)
    new_favorite = create_favorite(db=db, favorite=favorite)
    return jsonify(new_favorite), 201

@favorite_bp.route('/favorites', methods=['GET'])
def read_favorites():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    favorites = get_favorites(db, skip=skip, limit=limit)
    return jsonify(favorites), 200

@favorite_bp.route('/favorites/<int:favorite_id>', methods=['GET'])
def read_favorite(favorite_id):
    db = next(get_db())
    db_favorite = get_favorite(db, favorite_id=favorite_id)
    if db_favorite is None:
        return jsonify({"detail": "Favorite not found"}), 404
    return jsonify(db_favorite), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(favorite_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)