from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.favorite_schema import FavoriteCreate
from app.services.favorite_service import get_favorite, get_favorites, create_favorite
from app.config.database import SessionLocal

favorite_bp = Blueprint('favorite_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@favorite_bp.route('/favorites', methods=['POST'])
def create_new_favorite():
    db = next(get_db())
    favorite_data = request.get_json()
    favorite = FavoriteCreate(**favorite_data)
    new_favorite = create_favorite(db=db, favorite=favorite)
    return jsonify(new_favorite), 201

@favorite_bp.route('/favorites', methods=['GET'])
def read_favorites():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    favorites = get_favorites(db, skip=skip, limit=limit)
    return jsonify(favorites), 200

@favorite_bp.route('/favorites/<int:favorite_id>', methods=['GET'])
def read_favorite(favorite_id):
    db = next(get_db())
    db_favorite = get_favorite(db, favorite_id=favorite_id)
    if db_favorite is None:
        return jsonify({"detail": "Favorite not found"}), 404
    return jsonify(db_favorite), 200