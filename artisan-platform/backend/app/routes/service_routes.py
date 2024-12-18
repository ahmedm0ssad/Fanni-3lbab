from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.service_schema import ServiceCreate
from app.services.service_service import get_service, get_services, create_service
from app.config.database import SessionLocal

# Define Blueprint for services
service_bp = Blueprint('service_bp', __name__)

# Database session management
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new service
@service_bp.route('/services', methods=['POST'])
def create_new_service():
    service_data = request.get_json()
    service = ServiceCreate(**service_data)
    with SessionLocal() as db:
        new_service = create_service(db=db, service=service)
    return jsonify(new_service.to_dict()), 201  

# Get a list of services
@service_bp.route('/services', methods=['GET'])
def read_services():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        services = get_services(db, skip=skip, limit=limit)
    return jsonify([service.to_dict() for service in services]), 200 
# Get a specific service by ID
@service_bp.route('/services/<int:service_id>', methods=['GET'])
def read_service(service_id):
    with SessionLocal() as db:
        db_service = get_service(db, service_id=service_id)
        if db_service is None:
            return jsonify({"detail": "Service not found"}), 404
    return jsonify(db_service.to_dict()), 200 