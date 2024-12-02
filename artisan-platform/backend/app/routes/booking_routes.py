# Import necessary modules and functions from Flask, SQLAlchemy, and the application
from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.booking_schema import BookingCreate
from app.services.booking_service import get_booking, get_bookings, create_booking
from app.config.database import SessionLocal

# Create a Blueprint for booking routes, which allows us to organize the routes for this module
booking_bp = Blueprint('booking_bp', __name__)

# Dependency to get the database session
# This function provides a database session and ensures it is properly closed after use
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new booking
# This endpoint handles POST requests to create a new booking
@booking_bp.route('/bookings', methods=['POST'])
def create_new_booking():
    # Get a database session
    db = next(get_db())
    # Parse the JSON request data into a BookingCreate schema object
    booking_data = request.get_json()
    booking = BookingCreate(**booking_data)
    # Call the service layer to create a new booking in the database
    new_booking = create_booking(db=db, booking=booking)
    # Return the newly created booking as a JSON response with a 201 status code
    return jsonify(new_booking), 201

# Route to read all bookings with pagination
# This endpoint handles GET requests to retrieve a list of bookings with optional pagination
@booking_bp.route('/bookings', methods=['GET'])
def read_bookings():
    # Get a database session
    db = next(get_db())
    # Get the 'skip' and 'limit' query parameters for pagination, with default values
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    # Call the service layer to get a list of bookings from the database
    bookings = get_bookings(db, skip=skip, limit=limit)
    # Return the list of bookings as a JSON response with a 200 status code
    return jsonify(bookings), 200

# Route to read a specific booking by ID
# This endpoint handles GET requests to retrieve a specific booking by its ID
@booking_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def read_booking(booking_id):
    # Get a database session
    db = next(get_db())
    # Call the service layer to get the booking from the database by its ID
    db_booking = get_booking(db, booking_id=booking_id)
    # If the booking is not found, return a 404 error with a message
    if db_booking is None:
        return jsonify({"detail": "Booking not found"}), 404
    # Return the booking as a JSON response with a 200 status code
    return jsonify(db_booking), 200