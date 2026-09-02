from flask import Blueprint, request, jsonify
from models import db
from models.subject import Subject

subjects_bp = Blueprint(
    "subjects",
    __name__,
    url_prefix="/api/subjects"
)


@subjects_bp.route("/<int:user_id>", methods=["GET"])
def get_subjects(user_id):

    subjects = Subject.query.filter_by(user_id=user_id).all()

    result = []

    for subject in subjects:
        result.append({
            "id": subject.id,
            "subject_name": subject.subject_name,
            "credits": subject.credits,
            "priority": subject.priority
        })

    return jsonify({
        "success": True,
        "subjects": result
    })


@subjects_bp.route("/", methods=["POST"])
def add_subject():

    data = request.get_json()

    user_id = data.get("user_id")
    subject_name = data.get("subject_name")
    credits = data.get("credits", 0)
    priority = data.get("priority", "Medium")

    if not user_id or not subject_name:
        return jsonify({
            "success": False,
            "message": "User ID and subject name are required"
        }), 400

    subject = Subject(
        user_id=user_id,
        subject_name=subject_name,
        credits=credits,
        priority=priority
    )

    db.session.add(subject)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Subject added successfully",
        "subject_id": subject.id
    }), 201


@subjects_bp.route("/<int:subject_id>", methods=["DELETE"])
def delete_subject(subject_id):

    subject = Subject.query.get(subject_id)

    if not subject:
        return jsonify({
            "success": False,
            "message": "Subject not found"
        }), 404

    db.session.delete(subject)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Subject deleted successfully"
    })