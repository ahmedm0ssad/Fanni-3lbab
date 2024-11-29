from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.notification_schema import NotificationCreate
from app.services.notification_service import get_notification, get_notifications, create_notification
from app.config.database import SessionLocal

notification_bp = Blueprint('notification_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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