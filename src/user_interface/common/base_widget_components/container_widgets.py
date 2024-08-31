# src/user_interface/common/base_widget_components/container_widgets.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager

class ContainerWidgetsMixin:
    @ErrorManager.handle_errors()
    def create_group_box(self, title: str, parent=None) -> QtWidgets.QGroupBox:
        """Create a group box with a specified title."""
        group_box = QtWidgets.QGroupBox(title, parent)
        logger.debug(f"Created group box: {title}")
        return group_box

    @ErrorManager.handle_errors()
    def create_table_widget(self, rows: int, columns: int, parent=None) -> QtWidgets.QTableWidget:
        table = self._create_widget(QtWidgets.QTableWidget, parent)
        table.setRowCount(rows)
        table.setColumnCount(columns)
        logger.debug(f"Created table widget with {rows} rows and {columns} columns")
        return table

    @ErrorManager.handle_errors()
    def create_scroll_area(self, widget: QtWidgets.QWidget, parent=None) -> QtWidgets.QScrollArea:
        """Create a scroll area containing the specified widget."""
        scroll_area = QtWidgets.QScrollArea(parent)
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)
        logger.debug(f"Created scroll area for {widget.__class__.__name__}")
        return scroll_area