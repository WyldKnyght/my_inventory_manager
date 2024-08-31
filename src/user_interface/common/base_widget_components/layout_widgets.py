# src/user_interface/common/base_widget_components/layout_widgets.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager

class LayoutWidgetsMixin:
    @ErrorManager.handle_errors()
    def create_grid_layout(self, parent=None) -> QtWidgets.QGridLayout:
        """Create a grid layout."""
        layout = QtWidgets.QGridLayout(parent)
        logger.debug("Created grid layout")
        return layout

    @ErrorManager.handle_errors()
    def create_vertical_layout(self, parent=None) -> QtWidgets.QVBoxLayout:
        """Create a vertical layout."""
        layout = QtWidgets.QVBoxLayout(parent)
        logger.debug("Created vertical layout")
        return layout

    @ErrorManager.handle_errors()
    def create_horizontal_layout(self, parent=None) -> QtWidgets.QHBoxLayout:
        """Create a horizontal layout."""
        layout = QtWidgets.QHBoxLayout(parent)
        logger.debug("Created horizontal layout")
        return layout