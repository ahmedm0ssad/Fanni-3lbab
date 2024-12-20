import sys
import os
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime
import mysql.connector

# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
portfolio_bp = Blueprint('portfolio_bp', __name__)

# Define Routes
@portfolio_bp.route('/portfolios', methods=['POST'])
def create_new_portfolio():
    portfolio_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO portfolios (artisan_id, image_url, description, created_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                portfolio_data['artisan_id'],
                portfolio_data['image_url'],
                portfolio_data['description'],
                datetime.utcnow()  # Use current timestamp for created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Portfolio created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@portfolio_bp.route('/portfolios', methods=['GET'])
def read_portfolios():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM portfolios LIMIT %s OFFSET %s", (limit, skip))
        portfolios = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(portfolios), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(portfolio_bp)

if __name__ == '__main__':
    app.run(debug=True)