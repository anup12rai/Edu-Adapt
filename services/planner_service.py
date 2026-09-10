<<<<<<< HEAD
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
=======
from datetime import date
from utils.db import execute, query
from algorithms.study_planner import build_plan

def plan(user_id):
    tasks = query("SELECT * FROM tasks WHERE user_id=%s AND status!='Completed' AND due_date=%s ORDER BY priority='High' DESC, created_at", (user_id, date.today()))
    return build_plan(tasks)

def completed_today(user_id):
    tasks = query("SELECT * FROM tasks WHERE user_id=%s AND status='Completed' AND due_date=%s ORDER BY created_at", (user_id, date.today()))
    return build_plan(tasks)

def has_today_plan(user_id):
    return bool(query('SELECT id FROM tasks WHERE user_id=%s AND due_date=%s LIMIT 1', (user_id, date.today()), one=True))

def can_generate(user_id):
    return not query("SELECT id FROM tasks WHERE user_id=%s AND status!='Completed' AND due_date=%s LIMIT 1", (user_id, date.today()), one=True)

def generate_today(user_id):
    if not can_generate(user_id):
        return 0
    topics = query("""SELECT t.id, t.topic_name, s.subject_name, s.priority
        FROM topics t JOIN units u ON u.id=t.unit_id JOIN subjects s ON s.id=u.subject_id
        WHERE s.user_id=%s AND t.status!='Completed' ORDER BY s.priority='High' DESC, u.completion ASC LIMIT 5""", (user_id,))
    for topic in topics:
        execute('INSERT INTO tasks (user_id,title,due_date,priority) VALUES (%s,%s,%s,%s)',
                (user_id, f"Study: {topic['subject_name']} - {topic['topic_name']}", date.today(), topic['priority']))
    return len(topics)
>>>>>>> 1650dd9 (eduadapt project)
