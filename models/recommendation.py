<<<<<<< HEAD
from . import db
from datetime import datetime

class Recommendation(db.Model):
    __tablename__ = "recommendations"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    recommendation = db.Column(db.Text)

    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)
=======
from dataclasses import dataclass
@dataclass
class Recommendation: id: int; user_id: int; recommendation: str
>>>>>>> 1650dd9 (eduadapt project)
