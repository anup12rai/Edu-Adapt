from flask import Blueprint, request, jsonify
from models import db
from models.user import User

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/api/profile"
)


@profile_bp.route("/<int:user_id>", methods=["GET"])
def get_profile(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    return jsonify({
        "success": True,
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "created_at": str(user.created_at)
        }
    })


@profile_bp.route("/<int:user_id>", methods=["PUT"])
def update_profile(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    data = request.get_json()

    user.full_name = data.get(
        "full_name",
        user.full_name
    )

    user.email = data.get(
        "email",
        user.email
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Profile updated successfully"
    })