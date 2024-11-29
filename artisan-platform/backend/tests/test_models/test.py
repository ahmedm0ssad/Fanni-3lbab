from flask import Flask
from flask_mail import Mail, Message
from app.config.settings import settings

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = settings.mail_server
app.config['MAIL_PORT'] = settings.mail_port
app.config['MAIL_USE_TLS'] = settings.mail_tls
app.config['MAIL_USE_SSL'] = settings.mail_ssl
app.config['MAIL_USERNAME'] = settings.mail_username
app.config['MAIL_PASSWORD'] = settings.mail_password
app.config['MAIL_DEFAULT_SENDER'] = settings.mail_from

mail = Mail(app)

def send_email(subject: str, email_to: str, body: str):
    with app.app_context():
        msg = Message(subject=subject, recipients=[email_to], html=body)
        mail.send(msg)

