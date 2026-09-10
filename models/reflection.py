<<<<<<< HEAD
from . import db
from datetime import datetime

class Reflection(db.Model):
    __tablename__ = "reflections"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    notes = db.Column(db.Text)

    mood = db.Column(db.String(50))

    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)
=======
from dataclasses import dataclass
@dataclass
class Reflection: id: int; user_id: int; notes: str = None; mood: str = None
>>>>>>> 1650dd9 (eduadapt project)
