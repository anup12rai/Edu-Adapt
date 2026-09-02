from flask import Blueprint, jsonify
from models.task import Task

calendar_bp = Blueprint(
    "calendar",
    __name__,
    url_prefix="/api/calendar"
)


@calendar_bp.route("/<int:user_id>", methods=["GET"])
def get_calendar(user_id):

    tasks = Task.query.filter_by(user_id=user_id).all()

    events = []

    for task in tasks:
        events.append({
            "id": task.id,
            "title": task.title,
            "date": str(task.due_date) if task.due_date else None,
            "priority": task.priority,
            "status": task.status
        })

    return jsonify({
        "success": True,
        "events": events
    })