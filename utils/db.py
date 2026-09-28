import pymysql
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host=current_app.config['MYSQL_HOST'], port=current_app.config['MYSQL_PORT'],
            user=current_app.config['MYSQL_USER'], password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DATABASE'], cursorclass=pymysql.cursors.DictCursor,
            autocommit=True, charset='utf8mb4')
    return g.db


def query(sql, params=(), one=False):
    with get_db().cursor() as cursor:
        cursor.execute(sql, params)
        return cursor.fetchone() if one else cursor.fetchall()


def execute(sql, params=()):
    with get_db().cursor() as cursor:
        cursor.execute(sql, params)
        return cursor.lastrowid


def init_app(app):
    @app.teardown_appcontext
    def close_db(_error=None):
        db = g.pop('db', None)
        if db:
            db.close()
