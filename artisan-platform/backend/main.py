from flask import Flask
from app.config.database import init_db
from app.routes.postman.notification_test_api import notification_bp
from app.routes.postman.user_test_api import user_bp
from app.routes.postman.service_test_api import service_bp
from app.routes.postman.rating_test_api import rating_bp
from app.routes.postman.portfolio_test_api import portfolio_bp
from app.routes.postman.password_recovery_test_api import password_recovery_bp
from app.routes.postman.order_history_test_api import order_history_bp
from app.routes.postman.favorite_test_api import favorite_bp
from app.routes.postman.booking_test_api import booking_bp
# Import other blueprints as needed

app = Flask(__name__)
app.register_blueprint(notification_bp)
app.register_blueprint(user_bp)
app.register_blueprint(service_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(password_recovery_bp)
app.register_blueprint(order_history_bp)
app.register_blueprint(favorite_bp)
app.register_blueprint(booking_bp)
# Register other blueprints as needed

if __name__ == "__main__":
    app.run(debug=True)