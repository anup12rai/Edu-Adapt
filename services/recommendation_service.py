from utils.helper import success_response


def generate_recommendations(
    task_risks,
    available_hours=2
):

    recommendations = []

    high_risk = [
        task for task in task_risks
        if task["risk_level"] == "High"
    ]

    medium_risk = [
        task for task in task_risks
        if task["risk_level"] == "Medium"
    ]

    if high_risk:

        recommendations.append({
            "type": "urgent",
            "message":
                "Prioritize your high-risk tasks "
                "before working on lower-priority topics."
        })

    if medium_risk:

        recommendations.append({
            "type": "planning",
            "message":
                "Allocate additional study time "
                "to medium-risk subjects."
        })

    if available_hours < 2:

        recommendations.append({
            "type": "time",
            "message":
                "Your available study time is low. "
                "Focus on the highest-priority tasks."
        })

    elif available_hours >= 4:

        recommendations.append({
            "type": "productivity",
            "message":
                "You have enough study time today. "
                "Consider completing an additional topic."
        })

    if not recommendations:

        recommendations.append({
            "type": "general",
            "message":
                "Your current workload looks manageable. "
                "Maintain your study consistency."
        })

    return success_response(
        "Recommendations generated.",
        recommendations
    )