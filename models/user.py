from extensions import db
import uuid

class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable = False)
    token = db.Column(db.String(255),unique=True, nullable = True)

    def generate_token(self):
        self.token = str(uuid.uuid4())