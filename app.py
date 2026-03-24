from flask import Flask, request, jsonify
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


@app.route('/api/register/student/', methods = ['POST'])
def register_student():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({"status":"error", "message": "Email already exists"}), 400
    
    user = User(email=email, password_hash=generate_password_hash(password), role='student')
    db.session.add(user)
    db.session.flush()

    student = Student(user_id = user.id,
                      name = data.get('name'),
                      cgpa = data.get('cgpa'),
                      branch = data.get('branch'),
                      skills = data.get('skills'),
                      status='active'
                    )
    db.session.add(student)
    db.session.commit()

    return jsonify({"status": "success", "message": "Student registered"})


@app.route('/api/register/company/', methods = ["POST"])
def register_company():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email):
        return jsonify({"status": "error", "message" : "Email already exists"}), 400

    user = User(email=email, password_hash = generate_password_hash(password), role='company')

    db.session.add(user)
    db.session.flush()

    company = Company(
        user_id =user.id,
        company_name = data.get('company_name'),
        approval_status = 'pending'
    )

    db.session.add(company)
    db.session.commit()

    return jsonify({"status": "success", "message":"Company registered"})