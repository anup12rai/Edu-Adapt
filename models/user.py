<<<<<<< HEAD
from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    subjects = db.relationship("Subject", backref="user", lazy=True)
    tasks = db.relationship("Task", backref="user", lazy=True)
=======
from dataclasses import dataclass
@dataclass
class User: id: int; full_name: str; email: str
>>>>>>> 1650dd9 (eduadapt project)
