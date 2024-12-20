import sys
import os
from flask import Blueprint, Flask, request, jsonify
import mysql.connector

# Add the root directory of your project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../')

from app.config.database import get_db_connection

# Create a blueprint
service_bp = Blueprint('service_bp', __name__)

# Define Routes
@service_bp.route('/services', methods=['POST'])
def create_service():
    service_data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO services (name, description, price)
            VALUES (%s, %s, %s)
            """,
            (
                service_data['name'],
                service_data['description'],
                service_data['price']
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"detail": "Service created successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@service_bp.route('/services', methods=['GET'])
def read_services():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services")
        services = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(services), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(service_bp)

if __name__ == '__main__':
    app.run(debug=True)