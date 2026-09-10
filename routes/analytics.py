<<<<<<< HEAD
from flask import Blueprint, jsonify
from models.study_session import StudySession

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/api/analytics"
)


@analytics_bp.route("/<int:user_id>", methods=["GET"])
def get_analytics(user_id):

    sessions = StudySession.query.filter_by(
        user_id=user_id
    ).all()

    total_minutes = sum(
        session.duration for session in sessions
    )

    return jsonify({
        "success": True,
        "analytics": {
            "total_sessions": len(sessions),
            "total_minutes": total_minutes,
            "total_hours": round(total_minutes / 60, 2)
        }
    })
=======
from flask import Blueprint, render_template, session
from services.analytics_service import analytics
from services.dashboard_service import summary
from utils.helper import login_required
bp=Blueprint('analytics',__name__,url_prefix='/analytics')
@bp.route('/')
@login_required
def index(): return render_template('analytics/analytics.html',data=analytics(session['user_id']),summary=summary(session['user_id']))
>>>>>>> 1650dd9 (eduadapt project)
