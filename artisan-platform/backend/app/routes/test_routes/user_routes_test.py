import sys
import os
import pytest
from flask import Flask
import warnings

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='pydantic')

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.routes.user_routes import user_bp
from app.config.database import SessionLocal, Base, engine
from app.models.user import User

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register the user blueprint
    app.register_blueprint(user_bp, url_prefix='/api')

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

def test_create_user(test_client):
    # Test creating a new user
    response = test_client.post('/api/users', json={
        'email': 'test@example.com',
        'password': 'password123',
        'name': 'Test User',
        'address': '123 Test St',
        'phone': '1234567890',
        'user_type': 'regular',
        'created_at': '2023-10-01T00:00:00Z',
        'updated_at': '2023-10-01T00:00:00Z',
        'password_hash': 'hashed_password'
    })
    assert response.status_code == 201
    assert response.json['email'] == 'test@example.com'

def test_read_users(test_client):
    # Test reading users
    response = test_client.get('/api/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_read_user(test_client):
    # Test reading a specific user
    response = test_client.get('/api/users/1')
    assert response.status_code in [200, 404]  # User may or may not exist