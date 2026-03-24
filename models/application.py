from extensions import db

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable = False)
    placement_drive_id = db.Column(db.Integer, db.ForeignKey('placement_drive.id'), nullable = False)
    applied_date = db.Column(db.DateTime, default = db.func.now(), nullable = False) 
    status = db.Column(db.String(50), nullable = False, default = 'applied')

    __table_args__ = (db.UniqueConstraint('student_id', 'placement_drive_id', name='unique_student_drive_application'),)
