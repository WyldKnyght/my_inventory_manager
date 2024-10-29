# src/controllers/db_modules/db_query_executor.py

from pathlib import Path
from typing import List, Tuple, Any
from .db_connection_manager import ConnectionManager

class QueryExecutor:
    def __init__(self, db_path: Path):
        self.connection_manager = ConnectionManager(db_path)

    def execute_query(self, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
        """Execute a SELECT query and return the results."""
        with self.connection_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute_command(self, command: str, params: Tuple[Any, ...] = ()) -> int:
        """Execute an INSERT, UPDATE, or DELETE command and return the number of affected rows."""
        with self.connection_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(command, params)
            conn.commit()
            return cursor.rowcount

    def execute_many(self, command: str, param_list: List[Tuple[Any, ...]]) -> int:
        """Execute a command with multiple parameter sets."""
        with self.connection_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(command, param_list)
            conn.commit()
            return cursor.rowcount