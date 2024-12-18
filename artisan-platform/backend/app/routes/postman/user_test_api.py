import sys
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

# Update with your MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

# Define the UserCreate schema
class UserCreate:
    def __init__(self, email, password):
        self.email = email
        self.password = password

# Define the functions to interact with the database
def create_user(db_session, user):
    new_user = User(email=user.email, password=user.password)
    db_session.add(new_user)
    db_session.commit()
    return new_user

def get_user_by_email(db_session, email):
    return db_session.query(User).filter(User.email == email).first()

def get_users(db_session, skip=0, limit=10):
    return db_session.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db_session, user_id):
    return db_session.query(User).filter(User.id == user_id).first()

# Define Routes
@app.route('/users', methods=['POST'])
def create_new_user():
    user_data = request.get_json()
    user = UserCreate(**user_data)
    db_user = get_user_by_email(db.session, email=user.email)
    if db_user:
        return jsonify({"detail": "Email already registered"}), 400
    new_user = create_user(db.session, user=user)
    return jsonify(new_user), 201

@app.route('/users', methods=['GET'])
def read_users():
    skip = int(request.args.get('skip', 0))
    limit = int(request.args.get('limit', 10))
    users = get_users(db.session, skip=skip, limit=limit)
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = get_user_by_id(db.session, user_id=user_id)
    if user is None:
        return jsonify({"detail": "User not found"}), 404
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)