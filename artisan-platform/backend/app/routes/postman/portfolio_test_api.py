import mysql.connector
from flask import Blueprint, Flask, request, jsonify
from datetime import datetime

# Create a blueprint
portfolio_bp = Blueprint('portfolio_bp', __name__)

# Update with your MySQL database configuration
db_config = {
    'user': 'Rana',
    'password': 'Rana-555',
    'host': 'localhost',
    'database': 'Fanni_3lbab'
}

# Define Routes
@portfolio_bp.route('/portfolios', methods=['POST'])
def create_new_portfolio():
    portfolio_data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
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
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM portfolios LIMIT %s OFFSET %s", (limit, skip))
        portfolios = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(portfolios), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@portfolio_bp.route('/portfolios/<int:portfolio_id>', methods=['GET'])
def read_portfolio(portfolio_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM portfolios WHERE portfolio_id = %s", (portfolio_id,))
        portfolio = cursor.fetchone()
        cursor.close()
        connection.close()
        if portfolio is None:
            return jsonify({"detail": "Portfolio not found"}), 404
        return jsonify(portfolio), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(portfolio_bp)

if __name__ == '__main__':
    app.run(debug=True)