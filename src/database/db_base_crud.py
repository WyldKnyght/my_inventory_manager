# db_base_crud.py
# Defines a class `BaseCRUD` for interacting with the SQLite database.

import os
import sqlite3
from contextlib import contextmanager
from typing import Generator, Callable, Any
from dotenv import load_dotenv
import logging

load_dotenv()
db_path = os.getenv('DB_PATH')

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class BaseCRUD:
    @staticmethod
    @contextmanager
    def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
        """
        Context manager for database connections.
        Yields a connection and ensures it's closed after use.
        """
        conn = sqlite3.connect(db_path)
        try:
            yield conn
        finally:
            conn.close()

    @classmethod
    def execute_db_operation(cls, operation: Callable, *args: Any, **kwargs: Any) -> Any:
        """
        Execute a database operation within a connection context.

        :param operation: The database operation to execute
        :param args: Positional arguments for the operation
        :param kwargs: Keyword arguments for the operation
        :return: The result of the operation
        """
        with cls.get_db_connection() as conn:
            try:
                cursor = conn.cursor()
                result = operation(conn, cursor, *args, **kwargs)
                conn.commit()
                return result
            except Exception as e:
                conn.rollback()
                logger.error(f"Error executing database operation: {e}", exc_info=True)
                raise e

    @staticmethod
    def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
        """
        Convert a database row to a dictionary.

        :param cursor: The database cursor
        :param row: A database row
        :return: A dictionary representing the row
        """
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
