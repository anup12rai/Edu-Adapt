from . import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"),
                        nullable=False)

    title = db.Column(db.String(150))
    description = db.Column(db.Text)

    due_date = db.Column(db.Date)

    priority = db.Column(db.String(20))
    status = db.Column(db.String(20), default="Pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)