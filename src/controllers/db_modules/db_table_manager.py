# src/controllers/db_modules/db_table_manager.py
from typing import List, Tuple, Any

class TableManager:
    def __init__(self, query_executor):
        self.query_executor = query_executor

    def table_exists(self, table_name: str) -> bool:
        """Check if a table exists in the database."""
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        result = self.query_executor.execute_query(query, (table_name,))
        return bool(result)

    def get_table_info(self, table_name: str) -> List[Tuple[Any, ...]]:
        """Get information about table columns."""
        return self.query_executor.execute_query(f"PRAGMA table_info({table_name})")

    # Add more table-related methods here