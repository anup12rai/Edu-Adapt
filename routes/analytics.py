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