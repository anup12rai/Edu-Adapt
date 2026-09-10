from werkzeug.security import check_password_hash, generate_password_hash
from utils.db import execute, query

def register(full_name, email, password):
    if query('SELECT id FROM users WHERE email=%s', (email,), one=True):
        return None
    return execute('INSERT INTO users (full_name,email,password) VALUES (%s,%s,%s)', (full_name, email, generate_password_hash(password)))

def authenticate(email, password):
    user = query('SELECT * FROM users WHERE email=%s', (email,), one=True)
    return user if user and check_password_hash(user['password'], password) else None
