from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.service_schema import ServiceCreate
from app.services.service_service import get_service, get_services, create_service
from app.config.database import SessionLocal

service_bp = Blueprint('service_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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