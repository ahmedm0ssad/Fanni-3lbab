from sqlalchemy.orm import Session
from app.models.password_recovery import PasswordRecovery
from app.schemas.password_recovery_schema import PasswordRecoveryCreate, PasswordRecovery

def get_password_recovery(db: Session, recovery_id: int):
    return db.query(PasswordRecovery).filter(PasswordRecovery.recovery_id == recovery_id).first()

def get_password_recoveries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PasswordRecovery).offset(skip).limit(limit).all()

def create_password_recovery(db: Session, password_recovery: PasswordRecoveryCreate):
    db_password_recovery = PasswordRecovery(
        user_id=password_recovery.user_id,
        reset_token=password_recovery.reset_token,
        expires_at=password_recovery.expires_at
    )
    db.add(db_password_recovery)
    db.commit()
    db.refresh(db_password_recovery)
    return db_password_recovery