from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
service_bp = Blueprint('service_bp', __name__)

# Mock Schema and Database Session
class ServiceCreate:
    def __init__(self, artisan_id, service_name, description, price, category):
        self.artisan_id = artisan_id
        self.service_name = service_name
        self.description = description
        self.price = price
        self.category = category

# Mock Functions
def create_service(db, service):
    return {
        "service_id": 1,
        "artisan_id": service.artisan_id,
        "service_name": service.service_name,
        "description": service.description,
        "price": service.price,
        "category": service.category,
        "created_at": "2024-12-01T15:30:00",
        "updated_at": "2024-12-01T15:30:00",
    }

def get_services(db, skip, limit):
    return [
        {
            "service_id": 1,
            "artisan_id": 1,
            "service_name": "Sample Service",
            "description": "This is a sample service",
            "price": 100.0,
            "category": "Sample Category",
            "created_at": "2024-12-01T15:30:00",
            "updated_at": "2024-12-01T15:30:00",
        }
    ]

def get_service(db, service_id):
    if service_id == 1:
        return {
            "service_id": 1,
            "artisan_id": 1,
            "service_name": "Sample Service",
            "description": "This is a sample service",
            "price": 100.0,
            "category": "Sample Category",
            "created_at": "2024-12-01T15:30:00",
            "updated_at": "2024-12-01T15:30:00",
        }
    return None

# Mock Database Session
class MockDB:
    pass

def get_db():
    db = MockDB()
    yield db

# Define Routes
@service_bp.route('/services', methods=['POST'])
def create_new_service():
    db = next(get_db())
    service_data = request.get_json()
    service = ServiceCreate(**service_data)
    new_service = create_service(db=db, service=service)
    return jsonify(new_service), 201

@service_bp.route('/services', methods=['GET'])
def read_services():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    services = get_services(db, skip=skip, limit=limit)
    return jsonify(services), 200

@service_bp.route('/services/<int:service_id>', methods=['GET'])
def read_service(service_id):
    db = next(get_db())
    db_service = get_service(db, service_id=service_id)
    if db_service is None:
        return jsonify({"detail": "Service not found"}), 404
    return jsonify(db_service), 200

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(service_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)