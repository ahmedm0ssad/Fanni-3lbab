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
    db = next(get_db())
    user_data = request.get_json()
    user = UserCreate(**user_data)
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        return jsonify({"detail": "Email already registered"}), 400
    new_user = create_user(db=db, user=user)
    return jsonify(new_user), 201

@user_bp.route('/users', methods=['GET'])
def read_users():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    users = get_users(db, skip=skip, limit=limit)
    return jsonify(users), 200