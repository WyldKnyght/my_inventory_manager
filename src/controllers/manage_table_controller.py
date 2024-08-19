import logging
from PyQt6 import QtWidgets
from utils.database import fetch_all, execute_query, get_table_columns

logger = logging.getLogger(__name__)

class ManageTableController(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def get_table_data(self, table_name):
        """Fetch all data from the specified table."""
        query = f"SELECT * FROM {table_name}"
        return fetch_all(query)

    def update_table_widget(self, table_widget, data):
        """Update the table widget with new data."""
        if data:
            table_widget.clear()
            table_widget.setColumnCount(len(data[0]))
            table_widget.setRowCount(len(data))
            table_widget.setHorizontalHeaderLabels(data[0].keys())
            for row, record in enumerate(data):
                for col, value in enumerate(record.values()):
                    table_widget.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def add_record(self, table_name, data):
        """Add a new record to the specified table."""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        execute_query(query, tuple(data.values()))
        logger.info(f"Record added to {table_name}: {data}")

    def edit_record(self, table_name, current_data, updated_data):
        """Edit an existing record in the specified table."""
        primary_key_column = self.get_primary_key_column(table_name)
        updates = ', '.join([f"{col} = ?" for col in updated_data])
        query = f"UPDATE {table_name} SET {updates} WHERE {primary_key_column} = ?"
        execute_query(query, (*updated_data.values(), current_data[primary_key_column]))
        logger.info(f"Record updated in {table_name}: {updated_data}")

    def delete_record(self, table_name, record_id):
        """Delete a record from the specified table."""
        primary_key = self.get_primary_key_column(table_name)
        query = f"DELETE FROM {table_name} WHERE {primary_key} = ?"
        execute_query(query, (record_id,))
        logger.info(f"Record {record_id} deleted from {table_name}")

    def get_primary_key_column(self, table_name):
        """Determine the primary key column for the specified table."""
        columns = get_table_columns(table_name)
        return columns[0] if columns else "id"

    def handle_add_record(self, dialog, table_name):
        try:
            self.add_record(table_name, dialog.get_data())
        except Exception as e:
            logger.error(f"Failed to add record to table {table_name}: {e}")
            QtWidgets.QMessageBox.critical(dialog, "Error", f"Failed to add record: {e}")

    def handle_edit_record(self, dialog, table_name, current_data):
        try:
            self.edit_record(table_name, current_data, dialog.get_data())
        except Exception as e:
            logger.error(f"Failed to edit record in table {table_name}: {e}")
            QtWidgets.QMessageBox.critical(dialog, "Error", f"Failed to edit record: {e}")
