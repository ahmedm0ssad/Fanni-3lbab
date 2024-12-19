from flask import Blueprint, request, jsonify
from app.schemas.notification_schema import NotificationCreate
from app.services.notification_service import (
    get_notification, 
    get_notifications, 
    create_notification
)
from app.config.database import SessionLocal

notification_bp = Blueprint('notification_bp', __name__)

def get_db():
    """
    Provides a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@notification_bp.route('/notifications', methods=['POST'])
def create_new_notification():
    """
    Create a new notification entry.
    """
    notification_data = request.get_json()
    notification = NotificationCreate(**notification_data)
    with SessionLocal() as db:
        new_notification = create_notification(db=db, notification=notification)
    return jsonify(new_notification.to_dict()), 201  

@notification_bp.route('/notifications', methods=['GET'])
def read_notifications():
    """
    Retrieve all notifications with optional pagination.
    """
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        notifications = get_notifications(db, skip=skip, limit=limit)
    return jsonify([notification.to_dict() for notification in notifications]), 200  
@notification_bp.route('/notifications/<int:notification_id>', methods=['GET'])
def read_notification(notification_id):
    """
    Retrieve a single notification entry by its ID.
    """
    with SessionLocal() as db:
        db_notification = get_notification(db, notification_id=notification_id)
        if db_notification is None:
            return jsonify({"detail": "Notification not found"}), 404
    return jsonify(db_notification.to_dict()), 200  