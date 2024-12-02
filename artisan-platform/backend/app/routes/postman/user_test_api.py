from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
user_bp = Blueprint('user_bp', __name__)

# Mock Schema and Database Session
class UserCreate:
    def __init__(self, name, email, password_hash, phone=None, address=None, user_type=None):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.phone = phone
        self.address = address
        self.user_type = user_type

# Mock Functions
def create_user(db, user):
    return {
        "user_id": 1,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "address": user.address,
        "user_type": user.user_type,
        "created_at": "2024-12-01T15:30:00",
        "updated_at": "2024-12-01T15:30:00",
    }

def get_users(db, skip, limit):
    return [
        {
            "user_id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "user_type": "customer",
            "created_at": "2024-12-01T15:30:00",
            "updated_at": "2024-12-01T15:30:00",
        }
    ]

def get_user(db, user_id):
    if user_id == 1:
        return {
            "user_id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "user_type": "customer",
            "created_at": "2024-12-01T15:30:00",
            "updated_at": "2024-12-01T15:30:00",
        }
    return None

def get_user_by_email(db, email):
    if email == "john.doe@example.com":
        return {
            "user_id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "user_type": "customer",
            "created_at": "2024-12-01T15:30:00",
            "updated_at": "2024-12-01T15:30:00",
        }
    return None

# Mock Database Session
class MockDB:
    pass

def get_db():
    db = MockDB()
    yield db

# Define Routes
@user_bp.route('/users', methods=['POST'])
def create_new_user():
    db = next(get_db())
    user_data = request.get_json()
    user = UserCreate(**user_data)
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        return jsonify({"detail": "Email already registered"}), 400
    new_user = create_user(db=db, user=user)
    return jsonify(new_user), 201

@user_bp.route('/users', methods=['GET'])
def read_users():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    users = get_users(db, skip=skip, limit=limit)
    return jsonify(users), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    db = next(get_db())
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        return jsonify({"detail": "User not found"}), 404
    return jsonify(db_user), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)