import mysql.connector
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime

# Create a blueprint
booking_bp = Blueprint('booking_bp', __name__)

# Update with your MySQL database configuration
db_config = {
    'user': 'Rana',
    'password': 'Rana-555',
    'host': 'localhost',
    'database': 'Fanni_3lbab'
}

# Define Routes
@booking_bp.route('/bookings', methods=['POST'])
def create_booking():
    booking_data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO bookings (customer_id, service_id, artisan_id, booking_date, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                booking_data['customer_id'],
                booking_data['service_id'],
                booking_data['artisan_id'],
                booking_data['booking_date'],
                booking_data.get('status', 'pending'),
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Booking created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@booking_bp.route('/bookings', methods=['GET'])
def read_bookings():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bookings LIMIT %s OFFSET %s", (limit, skip))
        bookings = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(bookings), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@booking_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def read_booking(booking_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bookings WHERE booking_id = %s", (booking_id,))
        booking = cursor.fetchone()
        cursor.close()
        connection.close()
        if booking is None:
            return jsonify({"detail": "Booking not found"}), 404
        return jsonify(booking), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(booking_bp)

if __name__ == '__main__':
    app.run(debug=True)