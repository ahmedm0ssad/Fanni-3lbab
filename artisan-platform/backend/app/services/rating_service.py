from sqlalchemy.orm import Session
from app.models.rating import RatingAndReview
from app.schemas.rating_schema import RatingCreate

def get_rating(db: Session, review_id: int):
    """
    Retrieve a specific rating and review by its ID.
    """
    return db.query(RatingAndReview).filter(RatingAndReview.review_id == review_id).first()

def get_ratings(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of ratings and reviews with optional pagination.
    """
    return db.query(RatingAndReview).offset(skip).limit(limit).all()

def create_rating(db: Session, rating: RatingCreate):
    """
    Create a new rating and review entry.
    """
    db_rating = RatingAndReview(
        customer_id=rating.customer_id,
        artisan_id=rating.artisan_id,
        rating=rating.rating,
        review=rating.review
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
