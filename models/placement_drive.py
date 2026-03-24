from flask_login import UserMixin
from extensions import db

class PlacementDrive(UserMixin, db.Model):
    __tablename__ = 'placement_drive'
    id = db.Column(db.Integer, primary_key = True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable = False)
    job_title = db.Column(db.String(100), nullable = False)
    job_description = db.Column(db.String(255), nullable = False)
    eligibility = db.Column(db.String(255), nullable = False)
    skills = db.Column(db.String(255), nullable = True)
    deadline = db.Column(db.DateTime, nullable = False)
    status = db.Column(db.String(50), nullable = False, default = "pending")

    applications = db.relationship('Application', backref = 'placement_drive')
