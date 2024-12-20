from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class PasswordRecovery(Base):
    """
    PasswordRecovery class represents a password recovery request made by a user.

    Attributes:
        recovery_id (int): The primary key for the password recovery request.
        user_id (int): The foreign key referencing the user who made the request.
        reset_token (str): The token used to reset the password.
        created_at (datetime): The date and time when the request was created.
        expires_at (datetime): The date and time when the request expires.
    """

    __tablename__ = 'password_recovery'

    # Define columns
    recovery_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    reset_token = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    # Define relationships
    user = relationship("User", back_populates="password_recovery")
    def to_dict(self):
        return {
            "recovery_id": self.recovery_id,
            "user_id": self.user_id,
            "reset_token": self.reset_token,
            "created_at":self.created_at,
            "expires_at": self.expires_at,
            
        }
