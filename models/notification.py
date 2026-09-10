<<<<<<< HEAD
from . import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    message = db.Column(db.Text)

    is_read = db.Column(db.Boolean,
                        default=False)

    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)
=======
from dataclasses import dataclass
@dataclass
class Notification: id: int; user_id: int; message: str; is_read: bool = False
>>>>>>> 1650dd9 (eduadapt project)
