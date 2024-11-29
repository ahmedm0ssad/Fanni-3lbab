from flask import Flask
from .user_routes import user_bp
from .booking_routes import booking_bp
from .favorite_routes import favorite_bp
from .notification_routes import notification_bp
from .order_history_routes import order_history_bp
from .password_recovery_routes import password_recovery_bp
from .portfolio_routes import portfolio_bp
from .rating_routes import rating_bp
from .service_routes import service_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(booking_bp, url_prefix='/api')
    app.register_blueprint(favorite_bp, url_prefix='/api')
    app.register_blueprint(notification_bp, url_prefix='/api')
    app.register_blueprint(order_history_bp, url_prefix='/api')
    app.register_blueprint(password_recovery_bp, url_prefix='/api')
    app.register_blueprint(portfolio_bp, url_prefix='/api')
    app.register_blueprint(rating_bp, url_prefix='/api')
    app.register_blueprint(service_bp, url_prefix='/api')
    return app