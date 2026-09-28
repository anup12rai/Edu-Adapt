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
