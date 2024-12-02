from pydantic import BaseModel
from datetime import datetime

class ServiceBase(BaseModel):
    artisan_id: int
    service_name: str
    description: str = None
    price: float
    category: str

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    service_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True