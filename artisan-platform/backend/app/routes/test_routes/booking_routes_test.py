import sys
import os
import pytest
from flask import Flask
import warnings

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='pydantic')

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.routes.booking_routes import booking_bp
from app.config.database import SessionLocal, Base, engine
from app.models.booking import Booking

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register the booking blueprint
    app.register_blueprint(booking_bp, url_prefix='/api')

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

def test_create_booking(test_client):
    print("Running test_create_booking")
    # Test creating a new booking
    response = test_client.post('/api/bookings', json={
        'customer_id': 1,
        'service_id': 2,
        'artisan_id': 3,
        'status': 'pending',
       
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 201
    assert response.json['status'] == 'pending'

def test_read_bookings(test_client):
    print("Running test_read_bookings")
    # Test reading bookings
    response = test_client.get('/api/bookings')
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_read_booking(test_client):
    print("Running test_read_booking")
    # Test reading a specific booking
    response = test_client.get('/api/bookings/1')
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code in [200, 404]  # Booking may or may not exist