from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
notification_bp = Blueprint('notification_bp', __name__)

# Mock Schema and Database Session
class NotificationCreate:
    def __init__(self, user_id, message, is_read=False):
        self.user_id = user_id
        self.message = message
        self.is_read = is_read

# Mock Functions
def create_notification(db, notification):
    return {
        "notification_id": 1,
        "user_id": notification.user_id,
        "message": notification.message,
        "is_read": notification.is_read,
        "created_at": "2024-12-01T15:30:00",
    }

def get_notifications(db, skip, limit):
    return [
        {
            "notification_id": 1,
            "user_id": 1,
            "message": "Test notification",
            "is_read": False,
            "created_at": "2024-12-01T15:30:00",
        }
    ]

def get_notification(db, notification_id):
    if notification_id == 1:
        return {
            "notification_id": 1,
            "user_id": 1,
            "message": "Test notification",
            "is_read": False,
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
@notification_bp.route('/notifications', methods=['POST'])
def create_new_notification():
    db = next(get_db())
    notification_data = request.get_json()
    notification = NotificationCreate(**notification_data)
    new_notification = create_notification(db=db, notification=notification)
    return jsonify(new_notification), 201

@notification_bp.route('/notifications', methods=['GET'])
def read_notifications():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    notifications = get_notifications(db, skip=skip, limit=limit)
    return jsonify(notifications), 200

@notification_bp.route('/notifications/<int:notification_id>', methods=['GET'])
def read_notification(notification_id):
    db = next(get_db())
    db_notification = get_notification(db, notification_id=notification_id)
    if db_notification is None:
        return jsonify({"detail": "Notification not found"}), 404
    return jsonify(db_notification), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(notification_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)