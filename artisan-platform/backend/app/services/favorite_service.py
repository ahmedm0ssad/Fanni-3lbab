from sqlalchemy.orm import Session
from app.models.favorite import Favorite
from app.schemas.favorite_schema import FavoriteCreate

def get_favorite(db: Session, favorite_id: int):
    """
    Retrieve a favorite record by its ID.
    """
    return db.query(Favorite).filter(Favorite.favorite_id == favorite_id).first()

def get_favorites(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of favorite records with optional pagination.
    """
    return db.query(Favorite).offset(skip).limit(limit).all()

def create_favorite(db: Session, favorite: FavoriteCreate):
    """
    Create a new favorite record.
    """
    db_favorite = Favorite(
        customer_id=favorite.customer_id,
        artisan_id=favorite.artisan_id
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite
