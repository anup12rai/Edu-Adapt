from . import db
from datetime import datetime

class StudySession(db.Model):
    __tablename__ = "study_sessions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    subject_id = db.Column(db.Integer,
                           db.ForeignKey("subjects.id"))

    duration = db.Column(db.Integer)

    session_date = db.Column(db.DateTime,
                             default=datetime.utcnow)