# src/controllers/database_controller.py

import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class DatabaseController:
    def __init__(self):
        self.db_path = os.getenv("DB_PATH")
        if not self.db_path or not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found at {self.db_path}")

    def get_connection(self):
        """Establish a connection to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def execute_query(self, query, params=None):
        """Execute a single query with optional parameters."""
        conn = self.get_connection()
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

    def fetch_all(self, query, params=None):
        """Fetch all rows from a query and return as a list of dictionaries."""
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def get_table_columns(self, table_name):
        """Retrieve column names for a given table."""
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            return [column[1] for column in cursor.fetchall()]  # Column names
        finally:
            cursor.close()
            connection.close()