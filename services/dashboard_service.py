from services.analytics_service import (
    get_task_statistics,
    get_study_hours
)

from services.risk_service import get_user_risks

from services.recommendation_service import (
    generate_recommendations
)

from utils.helper import success_response


def get_dashboard_data(user_id):

    task_stats = get_task_statistics(
        user_id
    )

    study_hours = get_study_hours(
        user_id
    )

    risk_result = get_user_risks(
        user_id
    )

    risks = risk_result.get(
        "data",
        []
    )

    recommendation_result = generate_recommendations(
        risks,
        study_hours
    )

    return success_response(
        "Dashboard data retrieved.",
        {
            "tasks": task_stats,
            "study_hours": study_hours,
            "risks": risks[:5],
            "recommendations":
                recommendation_result.get(
                    "data",
                    []
                )
        }
    )