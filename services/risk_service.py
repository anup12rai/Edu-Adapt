from utils.db import execute_query
from utils.helper import success_response


def calculate_task_risk(task):

    score = 0

    remaining_days = task.get(
        "remaining_days",
        999
    )

    difficulty = task.get(
        "difficulty",
        1
    )

    priority = task.get(
        "priority",
        1
    )

    status = task.get(
        "status",
        "pending"
    )

    estimated_hours = task.get(
        "estimated_hours",
        1
    )

    # Deadline risk
    if remaining_days <= 0:
        score += 50

    elif remaining_days <= 2:
        score += 35

    elif remaining_days <= 5:
        score += 20

    # Difficulty risk
    score += difficulty * 5

    # Priority risk
    score += priority * 5

    # Workload risk
    score += min(
        float(estimated_hours) * 2,
        20
    )

    # Incomplete task
    if status != "completed":
        score += 10

    if score >= 70:
        level = "High"

    elif score >= 40:
        level = "Medium"

    else:
        level = "Low"

    return {
        "risk_score": min(score, 100),
        "risk_level": level
    }


def get_user_risks(user_id):

    tasks = execute_query(
        """
        SELECT
            id,
            title,
            difficulty,
            priority,
            estimated_hours,
            status,
            DATEDIFF(
                deadline,
                CURDATE()
            ) AS remaining_days
        FROM tasks
        WHERE user_id = %s
        AND status != 'completed'
        """,
        (user_id,),
        fetch=True
    )

    results = []

    for task in tasks or []:

        risk = calculate_task_risk(task)

        results.append({
            **task,
            **risk
        })

    results.sort(
        key=lambda x: x["risk_score"],
        reverse=True
    )

    return success_response(
        "Risk analysis completed.",
        results
    )