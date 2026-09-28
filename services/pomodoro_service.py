from utils.db import execute
def record(user_id, subject_id, minutes): return execute('INSERT INTO study_sessions (user_id,subject_id,duration) VALUES (%s,%s,%s)', (user_id, subject_id or None, minutes))
