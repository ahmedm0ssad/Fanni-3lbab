from sqlalchemy.orm import Session
from app.models.order_history import OrderHistory
from app.schemas.order_history_schema import OrderHistoryCreate, OrderHistory

def get_order_history(db: Session, order_id: int):
    return db.query(OrderHistory).filter(OrderHistory.order_id == order_id).first()

def get_order_histories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(OrderHistory).offset(skip).limit(limit).all()

def create_order_history(db: Session, order_history: OrderHistoryCreate):
    db_order_history = OrderHistory(
        booking_id=order_history.booking_id,
        customer_id=order_history.customer_id,
        artisan_id=order_history.artisan_id,
        amount_paid=order_history.amount_paid,
        payment_status=order_history.payment_status
    )
    db.add(db_order_history)
    db.commit()
    db.refresh(db_order_history)
    return db_order_history