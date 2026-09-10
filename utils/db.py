<<<<<<< HEAD
import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG


def get_connection():
    """
    Create and return a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

        return connection

    except Error as e:
        print(f"Database connection error: {e}")
        return None


def close_connection(connection, cursor=None):
    """
    Safely close cursor and database connection.
    """

    try:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

    except Error as e:
        print(f"Error closing database connection: {e}")


def execute_query(query, params=None, fetch=False, fetch_one=False):
    """
    Execute INSERT, UPDATE, DELETE or SELECT queries.
    """

    connection = get_connection()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query, params or ())

        if fetch_one:
            result = cursor.fetchone()

        elif fetch:
            result = cursor.fetchall()

        else:
            connection.commit()
            result = {
                "success": True,
                "last_id": cursor.lastrowid,
                "affected_rows": cursor.rowcount
            }

        return result

    except Error as e:
        connection.rollback()
        print(f"Query error: {e}")
        return None

    finally:
        close_connection(connection, cursor)
=======
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
>>>>>>> 1650dd9 (eduadapt project)
