<<<<<<< HEAD
from . import db

class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"),
                        nullable=False)

    subject_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer)
    priority = db.Column(db.String(20))

    units = db.relationship("Unit", backref="subject", lazy=True)
=======
from dataclasses import dataclass
@dataclass
class Subject: id: int; user_id: int; subject_name: str; credits: int = 0; priority: str = 'Medium'
>>>>>>> 1650dd9 (eduadapt project)
