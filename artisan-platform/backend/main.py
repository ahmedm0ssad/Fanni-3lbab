# main.py

from flask import Flask
from app.routes import create_app
from app.config.database import Base, engine

app = create_app()

# Initialize the database
with app.app_context():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(debug=True)