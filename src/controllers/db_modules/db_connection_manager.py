# src/controllers/db_modules/db_connection_manager.py

import sqlite3
from pathlib import Path
from utils.custom_logging import logger
from contextlib import contextmanager

class ConnectionManager:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    @contextmanager
    def get_connection(self):
        """Create and return a database connection as a context manager."""
        connection = None
        try:
            connection = sqlite3.connect(self.db_path)
            yield connection
        except sqlite3.Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise
        finally:
            if connection:
                connection.close()