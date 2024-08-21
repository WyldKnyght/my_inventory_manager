# src/user_interface/dialogs/common/data_table_dialog.py
from PyQt6 import QtWidgets, QtCore
from .error_warning_dialog import show_error_message

def create_data_table() -> QtWidgets.QTableWidget:
    """Create and configure the data table."""
    table = QtWidgets.QTableWidget()
    table.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
    table.setSortingEnabled(True)
    return table

def load_data(table_name, data_table, inventory_controller):
    """Load data from the specified table and display it."""
    try:
        column_headers, data = inventory_controller.get_data_by_table(table_name)
        configure_table(data_table, column_headers, data)
    except Exception as e:
        show_error_message("Data Loading Error", f"Failed to load data: {e}")

def configure_table(data_table, column_headers, data):
    """Configure the table with checkboxes and data."""
    data_table.clear()
    data_table.setRowCount(len(data))
    data_table.setColumnCount(len(column_headers) + 1)  # +1 for checkbox column
    
    headers = ['Select'] + column_headers
    data_table.setHorizontalHeaderLabels(headers)

    for row, item in enumerate(data):
        # Add checkbox
        checkbox = QtWidgets.QTableWidgetItem()
        checkbox.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        checkbox.setCheckState(QtCore.Qt.CheckState.Unchecked)
        data_table.setItem(row, 0, checkbox)
        
        # Add data
        for col, header in enumerate(column_headers, start=1):
            data_table.setItem(row, col, QtWidgets.QTableWidgetItem(str(item.get(header, ""))))