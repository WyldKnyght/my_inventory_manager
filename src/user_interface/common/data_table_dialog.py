# src/user_interface/common/data_table_dialog.py
from PyQt6 import QtWidgets, QtCore
from .error_warning_dialog import show_error_message
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import TABLE_STYLE, TABLE_POLICY

@ErrorManager.handle_errors()
def create_data_table() -> QtWidgets.QTableWidget:
    """Create and configure the data table."""
    table = QtWidgets.QTableWidget()
    table.setSizePolicy(*TABLE_POLICY)
    table.setSortingEnabled(True)
    table.setStyleSheet(TABLE_STYLE)
    logger.debug("Created data table")
    return table

@ErrorManager.handle_errors()
def load_data(table_name, data_table, inventory_controller):
    """Load data from the specified table and display it."""
    try:
        column_headers, data = inventory_controller.get_data_by_table(table_name)
        configure_table(data_table, column_headers, data)
        logger.info(f"Loaded data for table: {table_name}")
    except Exception as e:
        error_msg = f"Failed to load data: {str(e)}"
        logger.error(error_msg)
        show_error_message(None, "Data Loading Error", error_msg)

@ErrorManager.handle_errors()
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
    
    logger.debug(f"Configured table with {len(data)} rows and {len(headers)} columns")