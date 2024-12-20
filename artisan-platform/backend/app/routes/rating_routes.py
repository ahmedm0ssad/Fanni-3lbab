from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.rating_schema import RatingCreate
from app.services.rating_service import get_rating, get_ratings, create_rating
from app.config.database import SessionLocal

rating_bp = Blueprint('rating_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rating_bp.route('/ratings', methods=['POST'])
def create_new_rating():
    db = next(get_db())
    rating_data = request.get_json()
    rating = RatingCreate(**rating_data)
    new_rating = create_rating(db=db, rating=rating)
    return jsonify(new_rating), 201

@rating_bp.route('/ratings', methods=['GET'])
def read_ratings():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    ratings = get_ratings(db, skip=skip, limit=limit)
    return jsonify(ratings), 200

@rating_bp.route('/ratings/<int:review_id>', methods=['GET'])
def read_rating(review_id):
    db = next(get_db())
    db_rating = get_rating(db, review_id=review_id)
    if db_rating is None:
        return jsonify({"detail": "Rating not found"}), 404
    return jsonify(db_rating), 200