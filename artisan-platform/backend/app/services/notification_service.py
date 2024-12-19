from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification_schema import NotificationCreate

def get_notification(db: Session, notification_id: int):
    """
    Retrieve a notification record by its ID.
    """
    return db.query(Notification).filter(Notification.notification_id == notification_id).first()

def get_notifications(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of notification records with optional pagination.
    """
    return db.query(Notification).offset(skip).limit(limit).all()

def create_notification(db: Session, notification: NotificationCreate):
    """
    Create a new notification record.
    """
    db_notification = Notification(
        user_id=notification.user_id,
        message=notification.message,
        is_read=notification.is_read
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification
