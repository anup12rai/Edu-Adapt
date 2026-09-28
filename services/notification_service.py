from utils.db import execute, query
def all_for(user_id): return query('SELECT * FROM notifications WHERE user_id=%s ORDER BY created_at DESC', (user_id,))
def mark_read(user_id): return execute('UPDATE notifications SET is_read=1 WHERE user_id=%s', (user_id,))
