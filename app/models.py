from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Inf(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    duration = db.Column(db.String(50), nullable=False)

class Tickets(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    time_start = db.Column(db.String(50), nullable=False)
    place = db.Column(db.String(50), nullable=False)
    
def create_models(app):
    with app.app_context():
        db.create_all()