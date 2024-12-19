from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class Notification(Base):
    """
    Notification class represents a notification sent to a user.

    Attributes:
        notification_id (int): The primary key for the notification.
        user_id (int): The foreign key referencing the user who receives the notification.
        message (str): The content of the notification.
        is_read (bool): The read status of the notification.
        created_at (datetime): The date and time when the notification was created.
    """

    __tablename__ = 'notifications'

    # Define columns
    notification_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Define relationships
    user = relationship("User", back_populates="notifications")
    def to_dict(self):
        return {
            "notification_id": self.notification_id,
            "user_id": self.user_id,
            "message": self.message,
            "is_read":self.is_read,
            "created_at": self.created_at,
  
            
        }