# db_utils.py
# This script contains utility functions for interacting with the SQLite database.
import os
import sqlite3
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv('DB_PATH')

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

def execute_db_operation(operation, *args, **kwargs):
    with get_db_connection() as conn:
        try:
            result = operation(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e