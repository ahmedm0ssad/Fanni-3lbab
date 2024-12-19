from sqlalchemy.orm import Session
from app.models.booking import Booking as BookingModel
from app.schemas.booking_schema import BookingCreate

def get_booking(db: Session, booking_id: int):
    """
    Retrieve a booking record by its ID.
    """
    return db.query(BookingModel).filter(BookingModel.booking_id == booking_id).first()

def get_bookings(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of booking records with optional pagination.
    """
    return db.query(BookingModel).offset(skip).limit(limit).all()

def create_booking(db: Session, booking: BookingCreate):
    """
    Create a new booking record.
    """
    db_booking = BookingModel(
        customer_id=booking.customer_id,
        service_id=booking.service_id,
        artisan_id=booking.artisan_id,
        booking_date=booking.booking_date,
        status=booking.status
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
