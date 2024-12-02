from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
booking_bp = Blueprint('booking_bp', __name__)

# Mock Schema and Database Session
class BookingCreate:
    def __init__(self, customer_id, service_id, artisan_id, booking_date):
        self.customer_id = customer_id
        self.service_id = service_id
        self.artisan_id = artisan_id
        self.booking_date = booking_date

# Mock Functions
def create_booking(db, booking):
    return {
        "booking_id": 1,
        "customer_id": booking.customer_id,
        "service_id": booking.service_id,
        "artisan_id": booking.artisan_id,
        "booking_date": booking.booking_date,
        "status": "pending",
    }

def get_bookings(db, skip, limit):
    return [
        {
            "booking_id": 1,
            "customer_id": 1,
            "service_id": 2,
            "artisan_id": 3,
            "booking_date": "2024-12-01T15:30:00",
            "status": "confirmed",
        }
    ]

def get_booking(db, booking_id):
    if booking_id == 1:
        return {
            "booking_id": 1,
            "customer_id": 1,
            "service_id": 2,
            "artisan_id": 3,
            "booking_date": "2024-12-01T15:30:00",
            "status": "confirmed",
        }
    return None

# Mock Database Session
class MockDB:
    pass

def get_db():
    db = MockDB()
    yield db

# Define Routes
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

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(booking_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)
