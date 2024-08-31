# src/controllers/inventory_controller.py

from controllers.database_controller import DatabaseController
from utils.error_manager import ErrorManager
from utils.custom_logging import logger

class InventoryController:
    def __init__(self):
        self.db_controller = DatabaseController()

    def get_data_by_table(self, table_name):
        """Fetch data and its columns for a specified table."""
        query = f"SELECT * FROM {table_name}"
        data = self.db_controller.fetch_all(query)
        columns = self.db_controller.get_table_columns(table_name)
        return columns, data

    def add_item(self, table_name, data):
        """Add a new item to the specified table."""
        self._insert_data(table_name, data)

    def update_item(self, table_name, data, item_id, id_column):
        """Update an existing item in the specified table."""
        self._update_data(table_name, data, item_id, id_column)

    def delete_item(self, table_name, item_id, id_column):
        """Delete an item from the specified table."""
        query = f"DELETE FROM {table_name} WHERE {id_column} = ?"
        self.db_controller.execute_query(query, (item_id,))

    def _insert_data(self, table_name, data):
        """Helper function to insert data into a specified table."""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.db_controller.execute_query(query, tuple(data.values()))

    def _update_data(self, table_name, data, item_id, id_column):
        """Helper function to update data in a specified table."""
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = ?"
        self.db_controller.execute_query(query, tuple(data.values()) + (item_id,))

    @ErrorManager.handle_errors()
    def get_filtered_columns(self, table_name, columns):
        """Filter out autoincrement ID columns."""
        id_columns = get_id_columns()
        filtered_columns = [col for col in columns if col != id_columns.get(table_name)]
        logger.debug(f"Filtered columns for {table_name}: {filtered_columns}")
        return filtered_columns

    @ErrorManager.handle_errors()
    def get_category_names(self):
        """Get all category names."""
        # Implement the logic to fetch category names from the database
        pass

    @ErrorManager.handle_errors()
    def get_unit_types(self):
        """Get all unit types."""
        # Implement the logic to fetch unit types from the database
        pass

    @ErrorManager.handle_errors()
    def validate_inventory_input(self, table_name, field_values):
        """Validate user input before saving."""
        for column, value in field_values.items():
            if not value.strip():
                raise ValueError(f"{column} cannot be empty")
        logger.debug("Input validation passed")