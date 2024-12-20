import sys
import os
from flask import Blueprint, Flask, request, jsonify
import mysql.connector

# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
user_bp = Blueprint('user_bp', __name__)

# Define Routes
@user_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
            """,
            (
                user_data['username'],
                user_data['email'],
                user_data['password']
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "User created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@user_bp.route('/users', methods=['GET'])
def read_users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)