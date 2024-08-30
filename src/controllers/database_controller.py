# src/controllers/database_controller.py

import sqlite3
import os
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional, Tuple

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

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> Optional[int]:
        """Execute a single query with optional parameters."""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()

    def fetch_all(self, query: str, params: Optional[Tuple] = None) -> List[Dict[str, Any]]:
        """Fetch all rows from a query and return as a list of dictionaries."""
        connection = self.get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def get_table_columns(self, table_name: str) -> List[str]:
        """Retrieve column names for a given table."""
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            return [column[1] for column in cursor.fetchall()]  # Column names
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()
            connection.close()