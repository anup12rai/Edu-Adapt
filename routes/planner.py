from flask import Blueprint, request, jsonify
from models import db
from models.task import Task

planner_bp = Blueprint(
    "planner",
    __name__,
    url_prefix="/api/planner"
)


@planner_bp.route("/<int:user_id>", methods=["GET"])
def get_tasks(user_id):

    tasks = Task.query.filter_by(user_id=user_id).all()

    result = []

    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "due_date": str(task.due_date) if task.due_date else None,
            "priority": task.priority,
            "status": task.status
        })

    return jsonify({
        "success": True,
        "tasks": result
    })


@planner_bp.route("/", methods=["POST"])
def add_task():

    data = request.get_json()

    task = Task(
        user_id=data.get("user_id"),
        title=data.get("title"),
        description=data.get("description"),
        due_date=data.get("due_date"),
        priority=data.get("priority", "Medium"),
        status=data.get("status", "Pending")
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Task added successfully",
        "task_id": task.id
    }), 201


@planner_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({
            "success": False,
            "message": "Task not found"
        }), 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.priority = data.get("priority", task.priority)
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Task updated successfully"
    })


@planner_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({
            "success": False,
            "message": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Task deleted successfully"
    })