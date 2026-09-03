from flask import Blueprint, jsonify
from models.recommendation import Recommendation

recommendation_bp = Blueprint(
    "recommendation",
    __name__,
    url_prefix="/api/recommendations"
)


@recommendation_bp.route("/<int:user_id>", methods=["GET"])
def get_recommendations(user_id):

    recommendations = Recommendation.query.filter_by(
        user_id=user_id
    ).all()

    result = []

    for recommendation in recommendations:
        result.append({
            "id": recommendation.id,
            "recommendation": recommendation.recommendation,
            "created_at": str(recommendation.created_at)
        })

    return jsonify({
        "success": True,
        "recommendations": result
    })