from . import db

class Unit(db.Model):
    __tablename__ = "units"

    id = db.Column(db.Integer, primary_key=True)

    subject_id = db.Column(db.Integer,
                           db.ForeignKey("subjects.id"),
                           nullable=False)

    unit_name = db.Column(db.String(100))
    completion = db.Column(db.Float, default=0)

    topics = db.relationship("Topic", backref="unit", lazy=True)