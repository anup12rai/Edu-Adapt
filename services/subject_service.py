from utils.db import execute, query

def subjects(user_id): return query('SELECT * FROM subjects WHERE user_id=%s ORDER BY created_at DESC', (user_id,))
def subject(user_id, subject_id): return query('SELECT * FROM subjects WHERE id=%s AND user_id=%s', (subject_id, user_id), one=True)
def units(subject_id): return query('SELECT * FROM units WHERE subject_id=%s ORDER BY id', (subject_id,))
def create(user_id, name, credits, priority): return execute('INSERT INTO subjects (user_id,subject_name,credits,priority) VALUES (%s,%s,%s,%s)', (user_id,name,credits,priority))
def add_unit(subject_id, name): return execute('INSERT INTO units (subject_id,unit_name) VALUES (%s,%s)', (subject_id,name))
def add_topic(unit_id, name): return execute('INSERT INTO topics (unit_id,topic_name) VALUES (%s,%s)', (unit_id,name))
def update_unit(unit_id, completion): return execute('UPDATE units SET completion=%s WHERE id=%s', (completion,unit_id))
def delete_subject(user_id, subject_id): return execute('DELETE FROM subjects WHERE id=%s AND user_id=%s', (subject_id, user_id))
