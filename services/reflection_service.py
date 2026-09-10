from utils.db import execute, query
def create(user_id, notes, mood): return execute('INSERT INTO reflections (user_id,notes,mood) VALUES (%s,%s,%s)', (user_id,notes,mood))
def all_for(user_id): return query('SELECT * FROM reflections WHERE user_id=%s ORDER BY created_at DESC', (user_id,))
