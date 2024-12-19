import mysql.connector
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime

# Create a blueprint
rating_bp = Blueprint('rating_bp', __name__)

# Update with your MySQL database configuration
db_config = {
    'user': 'Rana',
    'password': 'Rana-555',
    'host': 'localhost',
    'database': 'Fanni_3lbab'
}

# Define Routes
@rating_bp.route('/ratings', methods=['POST'])
def create_new_rating():
    rating_data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
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
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ratings_and_reviews LIMIT %s OFFSET %s", (limit, skip))
        ratings = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(ratings), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@rating_bp.route('/ratings/<int:rating_id>', methods=['GET'])
def read_rating(rating_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ratings_and_reviews WHERE rating_id = %s", (rating_id,))
        rating = cursor.fetchone()
        cursor.close()
        connection.close()
        if rating is None:
            return jsonify({"detail": "Rating not found"}), 404
        return jsonify(rating), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(rating_bp)

if __name__ == '__main__':
    app.run(debug=True)