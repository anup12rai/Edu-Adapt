<<<<<<< HEAD
from utils.db import execute_query
from utils.helper import (
    success_response,
    calculate_percentage
)


def get_task_statistics(user_id):

    result = execute_query(
        """
        SELECT
            COUNT(*) AS total,
            SUM(
                CASE
                    WHEN status = 'completed'
                    THEN 1
                    ELSE 0
                END
            ) AS completed
        FROM tasks
        WHERE user_id = %s
        """,
        (user_id,),
        fetch_one=True
    )

    total = result["total"] or 0
    completed = result["completed"] or 0

    percentage = calculate_percentage(
        completed,
        total
    )

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "completion_percentage": percentage
    }


def get_study_hours(user_id):

    result = execute_query(
        """
        SELECT
            COALESCE(
                SUM(duration_minutes),
                0
            ) AS total_minutes
        FROM study_sessions
        WHERE user_id = %s
        """,
        (user_id,),
        fetch_one=True
    )

    minutes = result["total_minutes"] or 0

    return round(minutes / 60, 2)


def get_subject_progress(user_id):

    subjects = execute_query(
        """
        SELECT
            s.id,
            s.name,
            COUNT(t.id) AS total_topics,
            SUM(
                CASE
                    WHEN t.status = 'completed'
                    THEN 1
                    ELSE 0
                END
            ) AS completed_topics
        FROM subjects s

        LEFT JOIN topics t
            ON s.id = t.subject_id

        WHERE s.user_id = %s

        GROUP BY s.id, s.name
        """,
        (user_id,),
        fetch=True
    )

    subjects = subjects or []

    for subject in subjects:

        total = subject["total_topics"] or 0
        completed = subject["completed_topics"] or 0

        subject["progress"] = calculate_percentage(
            completed,
            total
        )

    return subjects


def get_dashboard_analytics(user_id):

    task_stats = get_task_statistics(
        user_id
    )

    study_hours = get_study_hours(
        user_id
    )

    subject_progress = get_subject_progress(
        user_id
    )

    return success_response(
        "Analytics retrieved.",
        {
            "tasks": task_stats,
            "study_hours": study_hours,
            "subjects": subject_progress
        }
    )


def get_weekly_progress(user_id):

    data = execute_query(
        """
        SELECT
            DATE(start_time) AS study_date,
            SUM(duration_minutes) AS minutes
        FROM study_sessions
        WHERE user_id = %s
        AND start_time >=
            DATE_SUB(CURDATE(), INTERVAL 7 DAY)
        GROUP BY DATE(start_time)
        ORDER BY study_date
        """,
        (user_id,),
        fetch=True
    )

    return success_response(
        "Weekly progress retrieved.",
        data or []
    )
=======
from utils.db import query

def analytics(user_id):
    subjects = query("SELECT s.subject_name, COALESCE(SUM(ss.duration),0) minutes FROM subjects s LEFT JOIN study_sessions ss ON ss.subject_id=s.id AND ss.user_id=%s WHERE s.user_id=%s GROUP BY s.id ORDER BY minutes DESC", (user_id,user_id))
    weekly = query("SELECT DATE(session_date) day, SUM(duration) minutes FROM study_sessions WHERE user_id=%s AND session_date >= DATE_SUB(CURDATE(), INTERVAL 6 DAY) GROUP BY DATE(session_date) ORDER BY day", (user_id,))
    risk_rows = query("""SELECT s.subject_name, COALESCE(AVG(u.completion),0) completion
       FROM subjects s LEFT JOIN units u ON u.subject_id=s.id LEFT JOIN tasks t ON t.user_id=s.user_id
       WHERE s.user_id=%s GROUP BY s.id""", (user_id,))
    for row in risk_rows:
        row['risk'] = 'High' if row['completion'] < 35 else 'Medium' if row['completion'] < 70 else 'Low'
        row['recommendation'] = 'Schedule a focused block today' if row['risk'] == 'High' else 'Keep steady weekly progress'
    return {'subjects': subjects, 'weekly': weekly, 'risks': risk_rows}
>>>>>>> 1650dd9 (eduadapt project)
