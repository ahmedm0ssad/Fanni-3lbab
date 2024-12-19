from flask import Blueprint, request, jsonify
from app.schemas.favorite_schema import FavoriteCreate
from app.services.favorite_service import (
    get_favorite,
    get_favorites,
    create_favorite
)
from app.config.database import SessionLocal

favorite_bp = Blueprint('favorite_bp', __name__)

def get_db():
    """
    Provides a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@favorite_bp.route('/favorites', methods=['POST'])
def create_new_favorite():
    """
    Create a new favorite entry.
    """
    favorite_data = request.get_json()
    favorite = FavoriteCreate(**favorite_data)
    with SessionLocal() as db:
        new_favorite = create_favorite(db=db, favorite=favorite)
    return jsonify(new_favorite.to_dict()), 201 
@favorite_bp.route('/favorites', methods=['GET'])
def read_favorites():
    """
    Retrieve all favorite entries with optional pagination.
    """
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        favorites = get_favorites(db, skip=skip, limit=limit)
    return jsonify([favorite.to_dict() for favorite in favorites]), 200  

@favorite_bp.route('/favorites/<int:favorite_id>', methods=['GET'])
def read_favorite(favorite_id):
    """
    Retrieve a single favorite entry by its ID.
    """
    with SessionLocal() as db:
        db_favorite = get_favorite(db, favorite_id=favorite_id)
        if db_favorite is None:
            return jsonify({"detail": "Favorite not found"}), 404
    return jsonify(db_favorite.to_dict()), 200  