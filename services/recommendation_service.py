from algorithms.recommendation_engine import generate
from services.dashboard_service import summary
from utils.db import execute, query

def recommendations(user_id, refresh=False):
    if refresh:
        s = summary(user_id)
        for text in generate(s['risk'], s['overdue'], s['completed'], s['total']):
            execute('INSERT INTO recommendations (user_id,recommendation) VALUES (%s,%s)', (user_id,text))
    return query('SELECT * FROM recommendations WHERE user_id=%s ORDER BY created_at DESC LIMIT 10', (user_id,))
