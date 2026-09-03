from utils.scheduler import generate_study_plan
from utils.helper import success_response


def simulate_plan(
    tasks,
    available_hours,
    simulated_hours=None
):

    if simulated_hours is None:
        simulated_hours = available_hours

    current_plan = generate_study_plan(
        tasks,
        available_hours
    )

    simulated_plan = generate_study_plan(
        tasks,
        simulated_hours
    )

    current_total = sum(
        item["allocated_hours"]
        for item in current_plan
    )

    simulated_total = sum(
        item["allocated_hours"]
        for item in simulated_plan
    )

    return success_response(
        "Simulation completed.",
        {
            "current": {
                "available_hours": available_hours,
                "allocated_hours": current_total,
                "plan": current_plan
            },
            "simulated": {
                "available_hours": simulated_hours,
                "allocated_hours": simulated_total,
                "plan": simulated_plan
            }
        }
    )


def calculate_readiness(tasks, available_hours):

    total_hours = sum(
        float(task.get("estimated_hours", 0))
        for task in tasks
        if task.get("status") != "completed"
    )

    if total_hours == 0:
        readiness = 100

    else:

        readiness = min(
            round(
                (available_hours / total_hours) * 100,
                2
            ),
            100
        )

    if readiness >= 80:
        level = "Excellent"

    elif readiness >= 60:
        level = "Good"

    elif readiness >= 40:
        level = "Moderate"

    else:
        level = "Low"

    return {
        "readiness_percentage": readiness,
        "readiness_level": level
    }