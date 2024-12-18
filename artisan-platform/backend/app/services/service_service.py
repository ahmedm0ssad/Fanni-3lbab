from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service_schema import ServiceCreate

def get_service(db: Session, service_id: int):
    """
    Retrieve a service by its ID.
    """
    return db.query(Service).filter(Service.id == service_id).first()  

def get_services(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of services with optional pagination.
    """
    return db.query(Service).offset(skip).limit(limit).all()

def create_service(db: Session, service: ServiceCreate):
    """
    Create a new service record.
    """
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
