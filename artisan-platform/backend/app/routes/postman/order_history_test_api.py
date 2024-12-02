from flask import Blueprint, Flask, request, jsonify

# Create a blueprint
order_history_bp = Blueprint('order_history_bp', __name__)

# Mock Schema and Database Session
class OrderHistoryCreate:
    def __init__(self, booking_id, customer_id, artisan_id, amount_paid, payment_status):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.artisan_id = artisan_id
        self.amount_paid = amount_paid
        self.payment_status = payment_status

# Mock Functions
def create_order_history(db, order_history):
    return {
        "order_id": 1,
        "booking_id": order_history.booking_id,
        "customer_id": order_history.customer_id,
        "artisan_id": order_history.artisan_id,
        "amount_paid": order_history.amount_paid,
        "payment_status": order_history.payment_status,
        "transaction_date": "2024-12-01T15:30:00",
    }

def get_order_histories(db, skip, limit):
    return [
        {
            "order_id": 1,
            "booking_id": 1,
            "customer_id": 1,
            "artisan_id": 2,
            "amount_paid": 100.0,
            "payment_status": "completed",
            "transaction_date": "2024-12-01T15:30:00",
        }
    ]

def get_order_history(db, order_id):
    if order_id == 1:
        return {
            "order_id": 1,
            "booking_id": 1,
            "customer_id": 1,
            "artisan_id": 2,
            "amount_paid": 100.0,
            "payment_status": "completed",
            "transaction_date": "2024-12-01T15:30:00",
        }
    return None

# Mock Database Session
class MockDB:
    pass

def get_db():
    db = MockDB()
    yield db

# Define Routes
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

# Create a standalone test app
def create_test_app():
    app = Flask(__name__)
    app.register_blueprint(order_history_bp)
    return app

if __name__ == '__main__':
    app = create_test_app()
    app.run(debug=True)