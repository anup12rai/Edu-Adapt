<<<<<<< HEAD
from flask import Blueprint, jsonify
from models import db
from models.notification import Notification

notification_bp = Blueprint(
    "notification",
    __name__,
    url_prefix="/api/notifications"
)


@notification_bp.route("/<int:user_id>", methods=["GET"])
def get_notifications(user_id):

    notifications = Notification.query.filter_by(
        user_id=user_id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    result = []

    for notification in notifications:
        result.append({
            "id": notification.id,
            "message": notification.message,
            "is_read": notification.is_read,
            "created_at": str(notification.created_at)
        })

    return jsonify({
        "success": True,
        "notifications": result
    })


@notification_bp.route("/<int:notification_id>/read", methods=["PUT"])
def mark_as_read(notification_id):

    notification = Notification.query.get(notification_id)

    if not notification:
        return jsonify({
            "success": False,
            "message": "Notification not found"
        }), 404

    notification.is_read = True
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Notification marked as read"
    })
=======
from flask import Blueprint, redirect, render_template, session, url_for
from services.notification_service import all_for, mark_read
from utils.helper import login_required
bp=Blueprint('notification',__name__,url_prefix='/notifications')
@bp.route('/')
@login_required
def index(): return render_template('notifications/notifications.html',items=all_for(session['user_id']))
@bp.post('/read-all')
@login_required
def read_all(): mark_read(session['user_id']); return redirect(url_for('notification.index'))
>>>>>>> 1650dd9 (eduadapt project)
