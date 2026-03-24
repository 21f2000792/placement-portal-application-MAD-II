from flask import Flask, request
from extensions import db
from models import *
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    admin_exists = User.query.filter_by(role='admin').first()

    if not admin_exists:
        admin = User(email='admin@gmail.com', password_hash = generate_password_hash('admin123'), role='admin')
        db.session.add(admin)
        db.session.commit()
