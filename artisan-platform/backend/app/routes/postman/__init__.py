from flask import Flask

app = Flask(__name__)

# Import and register blueprints
from .user_test_api import user_bp
from .service_test_api import service_bp
from .rating_test_api import rating_bp
from .portfolio_test_api import portfolio_bp
from .password_recovery_test_api import password_recovery_bp
from .order_history_test_api import order_history_bp
from .notification_test_api import notification_bp
from .favorite_test_api import favorite_bp
from .booking_test_api import booking_bp

app.register_blueprint(service_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(password_recovery_bp)
app.register_blueprint(order_history_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(favorite_bp)
app.register_blueprint(user_bp)
app.register_blueprint(booking_bp)

if __name__ == '__main__':
    app.run(debug=True)