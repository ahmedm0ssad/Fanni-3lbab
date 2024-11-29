from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime


class PasswordRecovery(Base):
    __tablename__ = 'password_recovery'

    recovery_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    reset_token = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    # Relationship
    user = relationship("User", back_populates="password_recovery")
