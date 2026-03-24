from extensions import db

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    company_name = db.Column(db.String(100), nullable = False)
    approval_status = db.Column(db.String(50), nullable = False, default = "pending")
    
    user = db.relationship('User')
    placement_drives = db.relationship('PlacementDrive', backref = 'company')