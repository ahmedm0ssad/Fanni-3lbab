import sys
import os
import pytest
from flask import Flask
import warnings

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='pydantic')

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.routes.favorite_routes import favorite_bp
from app.config.database import SessionLocal, Base, engine
from app.models.favorite import Favorite

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register the favorite blueprint
    app.register_blueprint(favorite_bp, url_prefix='/api')

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

def test_create_favorite(test_client):
    print("Running test_create_favorite")
    # Test creating a new favorite
    response = test_client.post('/api/favorites', json={
        'customer_id': 1,
        'artisan_id': 2,
        'created_at': '2023-10-01T00:00:00Z'
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 201
    assert response.json['customer_id'] == 1

def test_read_favorites(test_client):
    print("Running test_read_favorites")
    # Test reading favorites
    response = test_client.get('/api/favorites')
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_read_favorite(test_client):
    print("Running test_read_favorite")
    # Test reading a specific favorite
    response = test_client.get('/api/favorites/1')
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code in [200, 404]  # Favorite may or may not exist