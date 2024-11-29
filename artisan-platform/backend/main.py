# main.py

from flask import Flask
from app.routes import create_app
from app.config.database import Base, engine
from app.utils.email import init_mail

app = create_app()

# Initialize the database
with app.app_context():
    Base.metadata.create_all(bind=engine)

# Initialize mail
init_mail(app)

if __name__ == "__main__":
    app.run(debug=True)