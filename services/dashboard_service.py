from utils.db import query
from algorithms.readiness import calculate
from algorithms.risk_prediction import predict

def summary(user_id):
    counts = query("SELECT COUNT(*) total, SUM(status='Completed') completed, SUM(status!='Completed' AND due_date < CURDATE()) overdue FROM tasks WHERE user_id=%s", (user_id,), one=True)
    units = query('SELECT COALESCE(AVG(u.completion),0) completion FROM units u JOIN subjects s ON s.id=u.subject_id WHERE s.user_id=%s', (user_id,), one=True)
    minutes = query('SELECT COALESCE(SUM(duration),0) minutes FROM study_sessions WHERE user_id=%s AND session_date >= DATE_SUB(NOW(), INTERVAL 7 DAY)', (user_id,), one=True)
    total, completed = counts['total'] or 0, int(counts['completed'] or 0)
    completion = float(units['completion'] or 0)
    return {'total': total, 'completed': completed, 'overdue': int(counts['overdue'] or 0), 'completion': round(completion), 'minutes': int(minutes['minutes'] or 0), 'readiness': calculate(completed, total, completion), 'risk': predict(completion, int(counts['overdue'] or 0), int(minutes['minutes'] or 0))}

def sidebar(user_id):
    active = query('SELECT subject_name, priority FROM subjects WHERE user_id=%s ORDER BY priority="High" DESC, created_at DESC LIMIT 1', (user_id,), one=True)
    return {'active_subject': active, 'today_done': query("SELECT COUNT(*) done FROM tasks WHERE user_id=%s AND status='Completed' AND due_date=CURDATE()", (user_id,), one=True)['done']}
