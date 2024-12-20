import sys
import os
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime
import mysql.connector

# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
favorite_bp = Blueprint('favorite_bp', __name__)

# Define Routes
@favorite_bp.route('/favorites', methods=['POST'])
def create_favorite():
    favorite_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO favorites (customer_id, artisan_id, created_at)
            VALUES (%s, %s, %s)
            """,
            (
                favorite_data['customer_id'],
                favorite_data['artisan_id'],
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Favorite created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@favorite_bp.route('/favorites', methods=['GET'])
def read_favorites():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM favorites LIMIT %s OFFSET %s", (limit, skip))
        favorites = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(favorites), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(favorite_bp)

if __name__ == '__main__':
    app.run(debug=True)