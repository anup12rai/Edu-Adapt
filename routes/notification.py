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