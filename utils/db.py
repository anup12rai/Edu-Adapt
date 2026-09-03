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