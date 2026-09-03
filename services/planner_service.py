from utils.db import execute_query
from utils.scheduler import generate_study_plan
from utils.helper import success_response, error_response


def get_pending_tasks(user_id):

    tasks = execute_query(
        """
        SELECT
            t.id,
            t.title,
            t.description,
            t.estimated_hours,
            t.priority,
            t.difficulty,
            t.deadline,
            DATEDIFF(t.deadline, CURDATE())
                AS remaining_days
        FROM tasks t
        WHERE t.user_id = %s
        AND t.status != 'completed'
        ORDER BY t.deadline ASC
        """,
        (user_id,),
        fetch=True
    )

    return tasks or []


def generate_daily_plan(user_id, available_hours):

    tasks = get_pending_tasks(user_id)

    if not tasks:
        return error_response(
            "No pending tasks available."
        )

    plan = generate_study_plan(
        tasks,
        available_hours
    )

    return success_response(
        "Daily study plan generated.",
        plan
    )


def save_plan(user_id, plan_date, plan):

    for item in plan:

        execute_query(
            """
            INSERT INTO tasks
            (
                user_id,
                title,
                estimated_hours,
                priority,
                status,
                planned_date
            )
            VALUES (%s, %s, %s, %s, 'pending', %s)
            """,
            (
                user_id,
                item["title"],
                item["allocated_hours"],
                item["priority"],
                plan_date
            )
        )

    return success_response(
        "Study plan saved."
    )


def get_daily_plan(user_id, plan_date):

    tasks = execute_query(
        """
        SELECT *
        FROM tasks
        WHERE user_id = %s
        AND planned_date = %s
        ORDER BY priority DESC
        """,
        (
            user_id,
            plan_date
        ),
        fetch=True
    )

    return success_response(
        "Daily plan retrieved.",
        tasks or []
    )


def reschedule_task(task_id, new_date):

    result = execute_query(
        """
        UPDATE tasks
        SET planned_date = %s
        WHERE id = %s
        """,
        (
            new_date,
            task_id
        )
    )

    if not result:
        return error_response(
            "Unable to reschedule task."
        )

    return success_response(
        "Task rescheduled successfully."
    )