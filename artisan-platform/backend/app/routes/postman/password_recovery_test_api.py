from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
password_recovery_bp = Blueprint('password_recovery_bp', __name__)

# Mock Schema and Database Session
class PasswordRecoveryCreate:
    def __init__(self, user_id, reset_token, expires_at):
        self.user_id = user_id
        self.reset_token = reset_token
        self.expires_at = expires_at

# Mock Functions
def create_password_recovery(db, password_recovery):
    return {
        "recovery_id": 1,
        "user_id": password_recovery.user_id,
        "reset_token": password_recovery.reset_token,
        "expires_at": password_recovery.expires_at,
        "created_at": "2024-12-01T15:30:00",
    }

def get_password_recoveries(db, skip, limit):
    return [
        {
            "recovery_id": 1,
            "user_id": 1,
            "reset_token": "test_token",
            "expires_at": "2024-12-01T15:30:00",
            "created_at": "2024-12-01T15:30:00",
        }
    ]

def get_password_recovery(db, recovery_id):
    if recovery_id == 1:
        return {
            "recovery_id": 1,
            "user_id": 1,
            "reset_token": "test_token",
            "expires_at": "2024-12-01T15:30:00",
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
@password_recovery_bp.route('/password_recoveries', methods=['POST'])
def create_new_password_recovery():
    db = next(get_db())
    password_recovery_data = request.get_json()
    password_recovery = PasswordRecoveryCreate(**password_recovery_data)
    new_password_recovery = create_password_recovery(db=db, password_recovery=password_recovery)
    return jsonify(new_password_recovery), 201

@password_recovery_bp.route('/password_recoveries', methods=['GET'])
def read_password_recoveries():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    password_recoveries = get_password_recoveries(db, skip=skip, limit=limit)
    return jsonify(password_recoveries), 200

@password_recovery_bp.route('/password_recoveries/<int:recovery_id>', methods=['GET'])
def read_password_recovery(recovery_id):
    db = next(get_db())
    db_password_recovery = get_password_recovery(db, recovery_id=recovery_id)
    if db_password_recovery is None:
        return jsonify({"detail": "Password recovery not found"}), 404
    return jsonify(db_password_recovery), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(password_recovery_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)