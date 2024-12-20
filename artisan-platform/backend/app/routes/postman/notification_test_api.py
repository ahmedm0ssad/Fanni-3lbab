import sys
import os
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime
import mysql.connector


# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
notification_bp = Blueprint('notification_bp', __name__)

# Define Routes
@notification_bp.route('/notifications', methods=['POST'])
def create_notification():
    notification_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO notifications (user_id, message, is_read, created_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                notification_data['user_id'],
                notification_data['message'],
                notification_data.get('is_read', False),
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Notification created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@notification_bp.route('/notifications', methods=['GET'])
def read_notifications():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notifications LIMIT %s OFFSET %s", (limit, skip))
        notifications = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(notifications), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(notification_bp)

if __name__ == '__main__':
    app.run(debug=True)