from datetime import date
from utils.db import execute, query


def create_due_notifications(user_id):
    tasks = query("SELECT title, due_date FROM tasks WHERE user_id=%s AND status!='Completed' AND due_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 1 DAY)", (user_id,))
    for task in tasks:
        execute('INSERT INTO notifications (user_id, message) VALUES (%s, %s)', (user_id, f"Reminder: {task['title']} is due {task['due_date']}"))
    return len(tasks)
