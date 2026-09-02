from . import db
from datetime import datetime

class Simulation(db.Model):
    __tablename__ = "simulations"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    expected_gpa = db.Column(db.Float)

    predicted_score = db.Column(db.Float)

    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)