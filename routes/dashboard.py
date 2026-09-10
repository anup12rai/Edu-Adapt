<<<<<<< HEAD
from flask import Blueprint, jsonify
from models.user import User
from models.subject import Subject
from models.task import Task
from models.study_session import StudySession

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/api/dashboard"
)


@dashboard_bp.route("/<int:user_id>", methods=["GET"])
def dashboard(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    subjects = Subject.query.filter_by(user_id=user_id).count()
    tasks = Task.query.filter_by(user_id=user_id).count()
    sessions = StudySession.query.filter_by(user_id=user_id).count()

    return jsonify({
        "success": True,
        "dashboard": {
            "user": user.full_name,
            "total_subjects": subjects,
            "total_tasks": tasks,
            "total_study_sessions": sessions
        }
    })
=======
from flask import Blueprint, render_template, session
from services.dashboard_service import summary
from services.planner_service import plan
from utils.helper import login_required
bp=Blueprint('dashboard',__name__,url_prefix='/dashboard')
@bp.route('/')
@login_required
def index(): return render_template('dashboard/dashboard.html', summary=summary(session['user_id']), plan=plan(session['user_id'])[:3])
>>>>>>> 1650dd9 (eduadapt project)
