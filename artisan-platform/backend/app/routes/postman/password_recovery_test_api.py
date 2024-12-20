import sys
import os
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime
import mysql.connector

# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
password_recovery_bp = Blueprint('password_recovery_bp', __name__)

# Define Routes
@password_recovery_bp.route('/password_recovery', methods=['POST'])
def create_password_recovery():
    password_recovery_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO password_recovery (user_id, reset_token, created_at)
            VALUES (%s, %s, %s)
            """,
            (
                password_recovery_data['user_id'],
                password_recovery_data['reset_token'],
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Password recovery created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@password_recovery_bp.route('/password_recovery', methods=['GET'])
def read_password_recovery():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM password_recovery LIMIT %s OFFSET %s", (limit, skip))
        password_recovery = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(password_recovery), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(password_recovery_bp)

if __name__ == '__main__':
    app.run(debug=True)