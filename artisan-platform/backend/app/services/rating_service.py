from sqlalchemy.orm import Session
from app.models.rating import Rating
from app.schemas.rating_schema import RatingCreate, Rating

def get_rating(db: Session, review_id: int):
    return db.query(Rating).filter(Rating.review_id == review_id).first()

def get_ratings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Rating).offset(skip).limit(limit).all()

def create_rating(db: Session, rating: RatingCreate):
    db_rating = Rating(
        customer_id=rating.customer_id,
        artisan_id=rating.artisan_id,
        rating=rating.rating,
        review=rating.review
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating