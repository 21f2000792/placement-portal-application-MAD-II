from extensions import db

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    
    cgpa = db.Column(db.Float, nullable = False)
    branch = db.Column(db.String(100), nullable = False)
    skills = db.Column(db.String(255), nullable = True)
    status = db.Column(db.String(50), nullable = False)
    resume_path = db.Column(db.String(255), nullable = True)

    user = db.relationship('User')
    applications = db.relationship('Application', backref = 'student')

