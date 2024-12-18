from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.services.user_service import get_user, get_user_by_email, get_users, create_user
from app.config.database import SessionLocal

user_bp = Blueprint('user_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_bp.route('/users', methods=['POST'])
def create_new_user():
    user_data = request.get_json()
    user = UserCreate(**user_data)
    with SessionLocal() as db:
        db_user = get_user_by_email(db, email=user.email)
        if db_user:
            return jsonify({"detail": "Email already registered"}), 400
        new_user = create_user(db=db, user=user)
    return jsonify(new_user.to_dict()), 201  # Serialize the new user

@user_bp.route('/users', methods=['GET'])
def read_users():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        users = get_users(db, skip=skip, limit=limit)
    return jsonify([user.to_dict() for user in users]), 200  # Serialize users list

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    with SessionLocal() as db:
        db_user = get_user(db, user_id=user_id)
        if db_user is None:
            return jsonify({"detail": "User not found"}), 404
    return jsonify(db_user.to_dict()), 200  # Serialize user