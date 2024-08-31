# src/user_interface/common/base_widget_components/utility_methods.py
from PyQt6 import QtGui, QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import UIConfig

class UtilityMethodsMixin:
    def _create_widget(self, widget_class, parent=None, **kwargs):
        """Helper method to create a widget with optional properties."""
        widget = widget_class(parent)
        for prop, value in kwargs.items():
            if hasattr(widget, prop):
                getattr(widget, f'set{prop.capitalize()}')(value)
        return widget

    def _set_font(self, widget, font_size: int):
        """Set the font size for a widget."""
        font = QtGui.QFont()
        font.setPointSize(font_size)
        widget.setFont(font)

    def _connect_callback(self, signal, callback):
        """Connect a signal to a callback if the callback is callable."""
        if callback:
            assert callable(callback), "Callback must be callable."
            signal.connect(callback)

    def _validate_font_size(self, font_size: int):
        """Validate that the font size is a positive integer."""
        assert isinstance(font_size, int) and font_size > 0, "Font size must be a positive integer."
        logger.debug(f"Validated font size: {font_size}")

    @ErrorManager.handle_errors()
    def apply_widget_style(self, widget, style_name: str):
        """Apply a predefined style to a widget."""
        if style_name in UIConfig.WIDGET_STYLES:
            widget.setStyleSheet(UIConfig.WIDGET_STYLES[style_name])
            logger.debug(f"Applied style '{style_name}' to {widget.__class__.__name__}")
        else:
            logger.warning(f"Style '{style_name}' not found in UIConfig.WIDGET_STYLES")

    @ErrorManager.handle_errors()
    def create_spacer(self, w: int, h: int) -> QtWidgets.QSpacerItem:
        """Create a spacer item with specified width and height."""
        spacer = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        logger.debug(f"Created spacer item: {w}x{h}")
        return spacer