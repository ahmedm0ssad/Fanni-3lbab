from sqlalchemy.orm import Session
from app.models.favorite import Favorite
from app.schemas.favorite_schema import FavoriteCreate, Favorite

def get_favorite(db: Session, favorite_id: int):
    return db.query(Favorite).filter(Favorite.favorite_id == favorite_id).first()

def get_favorites(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Favorite).offset(skip).limit(limit).all()

def create_favorite(db: Session, favorite: FavoriteCreate):
    db_favorite = Favorite(
        customer_id=favorite.customer_id,
        artisan_id=favorite.artisan_id
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite