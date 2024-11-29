from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service_schema import ServiceCreate, Service

def get_service(db: Session, service_id: int):
    return db.query(Service).filter(Service.service_id == service_id).first()

def get_services(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Service).offset(skip).limit(limit).all()

def create_service(db: Session, service: ServiceCreate):
    db_service = Service(
        artisan_id=service.artisan_id,
        service_name=service.service_name,
        description=service.description,
        price=service.price,
        category=service.category
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service