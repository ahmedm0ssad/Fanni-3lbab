# Import necessary modules and functions
from flask import Blueprint, request, jsonify
from app.schemas.booking_schema import BookingCreate
from app.services.booking_service import (
    get_booking,
    get_bookings,
    create_booking
)
from app.config.database import SessionLocal

# Create a Blueprint for booking routes
booking_bp = Blueprint('booking_bp', __name__)

# Database session dependency
def get_db():
    """
    Provides a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@booking_bp.route('/bookings', methods=['POST'])
def create_new_booking():
    """
    Create a new booking.
    """
    booking_data = request.get_json()
    booking = BookingCreate(**booking_data)  # Parse request JSON into schema
    with SessionLocal() as db:
        new_booking = create_booking(db=db, booking=booking)  # Call service layer
    return jsonify(new_booking.to_dict()), 201  

@booking_bp.route('/bookings', methods=['GET'])
def read_bookings():
    """
    Retrieve all bookings with optional pagination.
    """
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        bookings = get_bookings(db, skip=skip, limit=limit)  # Fetch bookings
    return jsonify([booking.to_dict() for booking in bookings]), 200  
@booking_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def read_booking(booking_id):
    """
    Retrieve a specific booking by ID.
    """
    with SessionLocal() as db:
        db_booking = get_booking(db, booking_id=booking_id)  # Fetch booking by ID
        if db_booking is None:
            return jsonify({"detail": "Booking not found"}), 404  # Handle not found
    return jsonify(db_booking.to_dict()), 200 
