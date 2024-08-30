# src/user_interface/common/table_utils.py
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import TABLE_STYLE

@ErrorHandler.handle_errors()
def configure_table_headers(table: QTableWidget, column_headers):
    """Configure the table headers."""
    table.setColumnCount(len(column_headers))
    table.setHorizontalHeaderLabels(column_headers)
    table.setStyleSheet(TABLE_STYLE)
    logger.debug(f"Configured table headers: {column_headers}")

@ErrorHandler.handle_errors()
def populate_table_with_data(table: QTableWidget, data, column_headers):
    """Populate the table with data."""
    table.setRowCount(len(data))
    table.setUpdatesEnabled(False)
    for row, item in enumerate(data):
        populate_table_row(table, row, item, column_headers)
    table.setUpdatesEnabled(True)
    logger.debug(f"Populated table with {len(data)} rows")

@ErrorHandler.handle_errors()
def populate_table_row(table: QTableWidget, row, item, column_headers):
    """Populate a single row in the table."""
    for col, header in enumerate(column_headers):
        value = item.get(header, "")
        table.setItem(row, col, QTableWidgetItem(str(value)))
    logger.debug(f"Populated table row {row}")