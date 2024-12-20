import sys
import os
import pytest
from flask import Flask
import warnings

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='pydantic')

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.routes.rating_routes import rating_bp
from app.config.database import SessionLocal, Base, engine
from app.models.rating import RatingAndReview

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register the rating blueprint
    app.register_blueprint(rating_bp, url_prefix='/api')

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

def test_create_rating(test_client):
    # Test creating a new rating
    response = test_client.post('/api/ratings', json={
        'customer_id': 1,
        'artisan_id': 1,
        'rating': 5,
        'review': 'Excellent service!',
        'created_at': '2023-10-01T00:00:00Z'
    })
    assert response.status_code == 201
    assert response.json['rating'] == 5

def test_read_ratings(test_client):
    # Test reading ratings
    response = test_client.get('/api/ratings')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_read_rating(test_client):
    # Test reading a specific rating
    response = test_client.get('/api/ratings/1')
    assert response.status_code in [200, 404]  # Rating may or may not exist