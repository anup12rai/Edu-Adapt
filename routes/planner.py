<<<<<<< HEAD
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
=======
from flask import Blueprint, flash, redirect, render_template, session, url_for
from services.planner_service import completed_today, generate_today, has_today_plan, plan
from utils.helper import login_required
bp=Blueprint('planner',__name__,url_prefix='/planner')
@bp.route('/')
@login_required
def index(): return render_template('planner/planner.html', plan=plan(session['user_id']), done=completed_today(session['user_id']), generated=has_today_plan(session['user_id']))
@bp.post('/generate')
@login_required
def generate():
    created = generate_today(session['user_id'])
    flash(f'{created} study tasks added to today\'s plan.' if created else 'Complete today\'s plan before generating another one.', 'success' if created else 'warning')
    return redirect(url_for('planner.index'))
>>>>>>> 1650dd9 (eduadapt project)
