# src/controllers/inventory_controller.py

from controllers.database_controller import DatabaseController

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