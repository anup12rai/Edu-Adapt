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