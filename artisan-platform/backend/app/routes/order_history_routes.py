from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.schemas.order_history_schema import OrderHistoryCreate
from app.services.order_history_service import get_order_history, get_order_histories, create_order_history
from app.config.database import SessionLocal

order_history_bp = Blueprint('order_history_bp', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@order_history_bp.route('/order_histories', methods=['POST'])
def create_new_order_history():
    db = next(get_db())
    order_history_data = request.get_json()
    order_history = OrderHistoryCreate(**order_history_data)
    new_order_history = create_order_history(db=db, order_history=order_history)
    return jsonify(new_order_history), 201

@order_history_bp.route('/order_histories', methods=['GET'])
def read_order_histories():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    order_histories = get_order_histories(db, skip=skip, limit=limit)
    return jsonify(order_histories), 200

@order_history_bp.route('/order_histories/<int:order_id>', methods=['GET'])
def read_order_history(order_id):
    db = next(get_db())
    db_order_history = get_order_history(db, order_id=order_id)
    if db_order_history is None:
        return jsonify({"detail": "Order history not found"}), 404
    return jsonify(db_order_history), 200