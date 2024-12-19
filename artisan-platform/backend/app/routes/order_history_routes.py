from flask import Blueprint, request, jsonify
from app.schemas.order_history_schema import OrderHistoryCreate
from app.services.order_history_service import (
    get_order_history, 
    get_order_histories, 
    create_order_history
)
from app.config.database import SessionLocal

order_history_bp = Blueprint('order_history_bp', __name__)

def get_db():
    """
    Provides a new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@order_history_bp.route('/order_histories', methods=['POST'])
def create_new_order_history():
    """
    Create a new order history entry.
    """
    order_history_data = request.get_json()
    order_history = OrderHistoryCreate(**order_history_data)
    with SessionLocal() as db:
        new_order_history = create_order_history(db=db, order_history=order_history)
    return jsonify(new_order_history.to_dict()), 201  

@order_history_bp.route('/order_histories', methods=['GET'])
def read_order_histories():
    """
    Retrieve all order histories with optional pagination.
    """
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    with SessionLocal() as db:
        order_histories = get_order_histories(db, skip=skip, limit=limit)
    return jsonify([history.to_dict() for history in order_histories]), 200  

@order_history_bp.route('/order_histories/<int:history_id>', methods=['GET'])
def read_order_history(history_id):
    """
    Retrieve a single order history entry by its ID.
    """
    with SessionLocal() as db:
        db_order_history = get_order_history(db, history_id=history_id)
        if db_order_history is None:
            return jsonify({"detail": "Order history not found"}), 404
    return jsonify(db_order_history.to_dict()), 200  