from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification_schema import NotificationCreate, Notification

def get_notification(db: Session, notification_id: int):
    return db.query(Notification).filter(Notification.notification_id == notification_id).first()

def get_notifications(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Notification).offset(skip).limit(limit).all()

def create_notification(db: Session, notification: NotificationCreate):
    db_notification = Notification(
        user_id=notification.user_id,
        message=notification.message,
        is_read=notification.is_read
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification