import mysql.connector
from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
service_bp = Blueprint('service_bp', __name__)

# Update with your MySQL database configuration
db_config = {
    'user': 'Rana',
    'password': 'Rana-555',
    'host': 'localhost',
    'database': 'Fanni_3lbab'
}

# Define Routes
@service_bp.route('/services', methods=['POST'])
def create_new_service():
    service_data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO services (artisan_id, service_name, description, price, category, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                service_data['artisan_id'],
                service_data['service_name'],
                service_data['description'],
                service_data['price'],
                service_data['category'],
                service_data['created_at'],
                service_data['updated_at']
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
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services LIMIT %s OFFSET %s", (limit, skip))
        services = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(services), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

@service_bp.route('/services/<int:service_id>', methods=['GET'])
def read_service(service_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM services WHERE service_id = %s", (service_id,))
        service = cursor.fetchone()
        cursor.close()
        connection.close()
        if service is None:
            return jsonify({"detail": "Service not found"}), 404
        return jsonify(service), 200
    except mysql.connector.Error as err:
        return jsonify({"detail": f"Error: {err}"}), 500

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(service_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)