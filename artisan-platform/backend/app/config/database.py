from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
import mysql.connector
import sys
import os

# Ensure the backend directory is in the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

# Import settings after adjusting the sys.path
from app.config.settings import settings

# Use root user credentials to create the database
INITIAL_SQLALCHEMY_DATABASE_URL = settings.initial_database_url

# Connection to create the database if it doesn't exist
initial_engine = create_engine(INITIAL_SQLALCHEMY_DATABASE_URL)

# Define the final database URL
SQLALCHEMY_DATABASE_URL = settings.database_url

# Create the final engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_connection():
    return mysql.connector.connect(
        user=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        database=settings.db_name
    )

def init_db():
    # Check if the database exists
    inspector = inspect(engine)
    if not inspector.get_table_names():
        # Import models to register them
        from app.models.booking import Booking
        from app.models.favorite import Favorite
        from app.models.notification import Notification
        from app.models.order_history import OrderHistory
        from app.models.password_recovery import PasswordRecovery
        from app.models.portfolio import Portfolio
        from app.models.rating import RatingAndReview
        from app.models.service import Service
        from app.models.user import User, Admin

        # Create all tables
        try:
            Base.metadata.create_all(bind=engine)
            print("All tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")
    else:
        print("Database and tables already exist.")

def close_connection():
    try:
        initial_engine.dispose()
        engine.dispose()
        print("Connections closed successfully!")
    except Exception as e:
        print(f"Error closing the connections: {e}")