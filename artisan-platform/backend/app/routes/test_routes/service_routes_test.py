import sys
import os
import pytest
from flask import Flask
import warnings

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='pydantic')

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.routes.service_routes import service_bp
from app.config.database import SessionLocal, Base, engine
from app.models.service import Service

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register the service blueprint
    app.register_blueprint(service_bp, url_prefix='/api')

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

def test_create_service(test_client):
    # Test creating a new service
    response = test_client.post('/api/services', json={
        'artisan_id': 1,
        'service_name': 'Test Service',
        'description': 'This is a test service',
        'price': 100.0,
        'category': 'Test Category',
        'created_at': '2023-10-01T00:00:00Z',
        'updated_at': '2023-10-01T00:00:00Z'
    })
    assert response.status_code == 201
    assert response.json['service_name'] == 'Test Service'

def test_read_services(test_client):
    # Test reading services
    response = test_client.get('/api/services')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_read_service(test_client):
    # Test reading a specific service
    response = test_client.get('/api/services/1')
    assert response.status_code in [200, 404]  # Service may or may not exist