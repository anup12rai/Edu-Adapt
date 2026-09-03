from utils.db import execute_query
from utils.helper import success_response, error_response


def save_study_session(
    user_id,
    task_id,
    subject_id,
    duration_minutes,
    notes=None
):

    if duration_minutes <= 0:
        return error_response(
            "Study duration must be greater than zero."
        )

    result = execute_query(
        """
        INSERT INTO study_sessions
        (
            user_id,
            task_id,
            subject_id,
            duration_minutes,
            notes,
            start_time
        )
        VALUES
        (%s, %s, %s, %s, %s, NOW())
        """,
        (
            user_id,
            task_id,
            subject_id,
            duration_minutes,
            notes
        )
    )

    if not result:
        return error_response(
            "Unable to save study session."
        )

    return success_response(
        "Study session saved.",
        {
            "session_id": result["last_id"]
        }
    )


def get_study_sessions(user_id):

    sessions = execute_query(
        """
        SELECT *
        FROM study_sessions
        WHERE user_id = %s
        ORDER BY start_time DESC
        """,
        (user_id,),
        fetch=True
    )

    return success_response(
        "Study sessions retrieved.",
        sessions or []
    )