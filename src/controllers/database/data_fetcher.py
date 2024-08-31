# src/controllers/database/data_fetcher.py
from controllers.database_controller import DatabaseController
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.config_manager import config_manager

class DataFetcher:
    """Class for fetching data from the database."""

    def __init__(self):
        self.db_controller = DatabaseController()

    @ErrorManager.handle_errors()
    def fetch_foreign_key_data(self, table_name: str, key_column: str, value_column: str) -> list:
        """
        Fetch data for foreign key fields.
        
        Args:
            table_name (str): The name of the table to fetch data from.
            key_column (str): The name of the column to use as the key.
            value_column (str): The name of the column to use as the value.

        Returns:
            list: A list of tuples containing the key-value pairs.
        """
        query = self._get_foreign_key_query(table_name, key_column, value_column)
        result = self.db_controller.fetch_all(query)
        logger.debug(f"Fetched {len(result)} rows from {table_name}")
        return result

    @ErrorManager.handle_errors()
    def _get_foreign_key_query(self, table_name: str, key_column: str, value_column: str) -> str:
        """
        Get the query for fetching foreign key data.

        Args:
            table_name (str): The name of the table to fetch data from.
            key_column (str): The name of the column to use as the key.
            value_column (str): The name of the column to use as the value.

        Returns:
            str: The SQL query string.
        """
        query_template = config_manager.get('database.queries.fetch_foreign_key', 
                                            "SELECT {key}, {value} FROM {table}")
        query = query_template.format(key=key_column, value=value_column, table=table_name)
        logger.debug(f"Generated foreign key query: {query}")
        return query

    @ErrorManager.handle_errors()
    def fetch_table_data(self, table_name: str, columns: list = None, 
                            where_clause: str = None, order_by: str = None) -> list:
        """
        Fetch data from a specified table with optional filtering and ordering.

        Args:
            table_name (str): The name of the table to fetch data from.
            columns (list, optional): List of column names to fetch. Defaults to None (all columns).
            where_clause (str, optional): WHERE clause for filtering. Defaults to None.
            order_by (str, optional): ORDER BY clause for sorting. Defaults to None.

        Returns:
            list: A list of dictionaries containing the fetched data.
        """
        query = self._get_table_data_query(table_name, columns, where_clause, order_by)
        result = self.db_controller.fetch_all(query)
        logger.debug(f"Fetched {len(result)} rows from {table_name}")
        return result

    @ErrorManager.handle_errors()
    def _get_table_data_query(self, table_name: str, columns: list = None, 
                                where_clause: str = None, order_by: str = None) -> str:
        """
        Get the query for fetching table data.

        Args:
            table_name (str): The name of the table to fetch data from.
            columns (list, optional): List of column names to fetch. Defaults to None (all columns).
            where_clause (str, optional): WHERE clause for filtering. Defaults to None.
            order_by (str, optional): ORDER BY clause for sorting. Defaults to None.

        Returns:
            str: The SQL query string.
        """
        columns_str = ", ".join(columns) if columns else "*"
        query = f"SELECT {columns_str} FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"
        if order_by:
            query += f" ORDER BY {order_by}"
        logger.debug(f"Generated table data query: {query}")
        return query