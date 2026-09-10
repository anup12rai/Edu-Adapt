<<<<<<< HEAD
from utils.db import execute_query
from utils.helper import success_response


def create_notification(
    user_id,
    title,
    message,
    notification_type="general"
):

    result = execute_query(
        """
        INSERT INTO notifications
        (
            user_id,
            title,
            message,
            type,
            is_read
        )
        VALUES (%s, %s, %s, %s, 0)
        """,
        (
            user_id,
            title,
            message,
            notification_type
        )
    )

    return bool(result)


def get_notifications(user_id):

    notifications = execute_query(
        """
        SELECT *
        FROM notifications
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,),
        fetch=True
    )

    return success_response(
        "Notifications retrieved.",
        notifications or []
    )


def mark_as_read(notification_id):

    result = execute_query(
        """
        UPDATE notifications
        SET is_read = 1
        WHERE id = %s
        """,
        (notification_id,)
    )

    if not result:
        return success_response(
            "Unable to update notification."
        )

    return success_response(
        "Notification marked as read."
    )


def delete_notification(notification_id):

    result = execute_query(
        """
        DELETE FROM notifications
        WHERE id = %s
        """,
        (notification_id,)
    )

    if not result:
        return success_response(
            "Unable to delete notification."
        )

    return success_response(
        "Notification deleted."
    )
=======
from utils.db import execute, query
def all_for(user_id): return query('SELECT * FROM notifications WHERE user_id=%s ORDER BY created_at DESC', (user_id,))
def mark_read(user_id): return execute('UPDATE notifications SET is_read=1 WHERE user_id=%s', (user_id,))
>>>>>>> 1650dd9 (eduadapt project)
