# src/utils/database.py

import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database path from the environment variable
db_path = os.getenv("DB_PATH")

def get_connection():
    """Establish a connection to the SQLite database."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file not found at {db_path}")
    return sqlite3.connect(db_path)

def execute_query(query, params=None):
    """Execute a single query with optional parameters."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()



def fetch_all(query):
    """Fetch all rows from a query and return as a list of dictionaries."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    cursor.close()
    connection.close()
    return data