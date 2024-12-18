import sys
import os

# Set the PYTHONPATH to the root of your project directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.append(project_root)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.user import UserCreate, create_user, get_user_by_email, get_users, get_user_by_id
from app.routes.user_routes import user_bp

app = Flask(__name__)

# Update with your MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Session = sessionmaker(bind=db.engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Define Routes
@user_bp.route('/users', methods=['POST'])
def create_new_user():
    db = next(get_db())
    user_data = request.get_json()
    user = UserCreate(**user_data)
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        return jsonify({"detail": "Email already registered"}), 400
    new_user = create_user(db=db, user=user)
    return jsonify(new_user), 201

@user_bp.route('/users', methods=['GET'])
def read_users():
    db = next(get_db())
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    users = get_users(db, skip=skip, limit=limit)
    return jsonify(users), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    db = next(get_db())
    user = get_user_by_id(db, user_id=user_id)
    if user is None:
        return jsonify({"detail": "User not found"}), 404
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)