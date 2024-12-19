from flask import Blueprint, request, jsonify
from app.schemas.password_recovery_schema import PasswordRecoveryCreate
from app.services.password_recovery_service import (
    get_password_recovery, 
    get_password_recoveries, 
    create_password_recovery
)
from app.config.database import SessionLocal

password_recovery_bp = Blueprint('password_recovery_bp', __name__)

def get_db():
    """
    Provides a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@password_recovery_bp.route('/password_recoveries', methods=['POST'])
def create_new_password_recovery():
    """
    Create a new password recovery entry.
    """
    password_recovery_data = request.get_json()
    password_recovery = PasswordRecoveryCreate(**password_recovery_data)
    with SessionLocal() as db:
        new_password_recovery = create_password_recovery(db=db, password_recovery=password_recovery)
    return jsonify(new_password_recovery.to_dict()), 201  
@password_recovery_bp.route('/password_recoveries', methods=['GET'])
def read_password_recoveries():
    """
    Retrieve all password recoveries with optional pagination.
    """
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        password_recoveries = get_password_recoveries(db, skip=skip, limit=limit)
    return jsonify([recovery.to_dict() for recovery in password_recoveries]), 200  

@password_recovery_bp.route('/password_recoveries/<int:recovery_id>', methods=['GET'])
def read_password_recovery(recovery_id):
    """
    Retrieve a single password recovery entry by its ID.
    """
    with SessionLocal() as db:
        db_password_recovery = get_password_recovery(db, recovery_id=recovery_id)
        if db_password_recovery is None:
            return jsonify({"detail": "Password recovery not found"}), 404
    return jsonify(db_password_recovery.to_dict()), 200  