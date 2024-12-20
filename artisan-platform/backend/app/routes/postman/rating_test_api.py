import sys
import os
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime
import mysql.connector

# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
rating_bp = Blueprint('rating_bp', __name__)

# Define Routes
@rating_bp.route('/ratings', methods=['POST'])
def create_new_rating():
    rating_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO ratings_and_reviews (customer_id, artisan_id, rating, review, created_at)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                rating_data['customer_id'],
                rating_data['artisan_id'],
                rating_data['rating'],
                rating_data['review'],
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Rating created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@rating_bp.route('/ratings', methods=['GET'])
def read_ratings():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ratings_and_reviews LIMIT %s OFFSET %s", (limit, skip))
        ratings = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(ratings), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(rating_bp)

if __name__ == '__main__':
    app.run(debug=True)