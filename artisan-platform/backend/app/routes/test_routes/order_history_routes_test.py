import sys
import os
import pytest
from flask import Flask
import warnings

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='pydantic')

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.routes.order_history_routes import order_history_bp
from app.config.database import SessionLocal, Base, engine
from app.models.order_history import OrderHistory

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register the order history blueprint
    app.register_blueprint(order_history_bp, url_prefix='/api')

    # Create the database tables
    with app.app_context():
        Base.metadata.create_all(bind=engine)

    # Create a test client
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

    # Drop the database tables
    with app.app_context():
        Base.metadata.drop_all(bind=engine)

def test_create_order_history(test_client):
    print("Running test_create_order_history")
    # Test creating a new order history
    response = test_client.post('/api/order_histories', json={
        'booking_id': 1,
        'customer_id': 1,
        'artisan_id': 2,
        'amount_paid': 100.0,
        'payment_status': 'Paid',
        'created_at': '2023-10-01T00:00:00Z'
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 201
    assert response.json['amount_paid'] == 100.0

def test_read_order_histories(test_client):
    print("Running test_read_order_histories")
    # Test reading order histories
    response = test_client.get('/api/order_histories')
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_read_order_history(test_client):
    print("Running test_read_order_history")
    # Test reading a specific order history
    response = test_client.get('/api/order_histories/1')
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code in [200, 404]  # Order history may or may not exist