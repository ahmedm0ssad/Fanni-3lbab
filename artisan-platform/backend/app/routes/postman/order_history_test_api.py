import mysql.connector
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime

# Create a blueprint
order_history_bp = Blueprint('order_history_bp', __name__)

# Update with your MySQL database configuration
db_config = {
    'user': 'Rana',
    'password': 'Rana-555',
    'host': 'localhost',
    'database': 'Fanni_3lbab'
}

# Define Routes
@order_history_bp.route('/order_history', methods=['POST'])
def create_order_history():
    order_history_data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO order_history (booking_id, customer_id, artisan_id, amount_paid, payment_status, transaction_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                order_history_data['booking_id'],
                order_history_data['customer_id'],
                order_history_data['artisan_id'],
                order_history_data['amount_paid'],
                order_history_data['payment_status'],
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Order history created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@order_history_bp.route('/order_history', methods=['GET'])
def read_order_histories():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM order_history LIMIT %s OFFSET %s", (limit, skip))
        order_histories = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(order_histories), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@order_history_bp.route('/order_history/<int:order_history_id>', methods=['GET'])
def read_order_history(order_history_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM order_history WHERE order_history_id = %s", (order_history_id,))
        order_history = cursor.fetchone()
        cursor.close()
        connection.close()
        if order_history is None:
            return jsonify({"detail": "Order history not found"}), 404
        return jsonify(order_history), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(order_history_bp)

if __name__ == '__main__':
    app.run(debug=True)