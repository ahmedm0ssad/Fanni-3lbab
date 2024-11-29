from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.booking_schema import BookingCreate
from app.services.booking_service import get_booking, get_bookings, create_booking
from app.config.database import SessionLocal

booking_bp = Blueprint('booking_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@booking_bp.route('/bookings', methods=['POST'])
def create_new_booking():
    db = next(get_db())
    booking_data = request.get_json()
    booking = BookingCreate(**booking_data)
    new_booking = create_booking(db=db, booking=booking)
    return jsonify(new_booking), 201

@booking_bp.route('/bookings', methods=['GET'])
def read_bookings():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    bookings = get_bookings(db, skip=skip, limit=limit)
    return jsonify(bookings), 200

@booking_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def read_booking(booking_id):
    db = next(get_db())
    db_booking = get_booking(db, booking_id=booking_id)
    if db_booking is None:
        return jsonify({"detail": "Booking not found"}), 404
    return jsonify(db_booking), 200