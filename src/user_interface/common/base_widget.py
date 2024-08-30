# src/user_interface/common/base_widget.py
from PyQt6 import QtCore, QtGui, QtWidgets
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import DEFAULT_FONT_SIZE, DEFAULT_ALIGNMENT

class BaseWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.info("Initialized BaseWidget")

    @ErrorHandler.handle_errors()
    def create_group_box(self, title: str, parent=None) -> QtWidgets.QGroupBox:
        """Create a group box with a specified title."""
        group_box = QtWidgets.QGroupBox(title, parent)
        logger.debug(f"Created group box: {title}")
        return group_box

    @ErrorHandler.handle_errors()
    def create_grid_layout(self, parent=None) -> QtWidgets.QGridLayout:
        """Create a grid layout."""
        layout = QtWidgets.QGridLayout(parent)
        logger.debug("Created grid layout")
        return layout

    @ErrorHandler.handle_errors()
    def create_vertical_layout(self, parent=None) -> QtWidgets.QVBoxLayout:
        """Create a vertical layout."""
        layout = QtWidgets.QVBoxLayout(parent)
        logger.debug("Created vertical layout")
        return layout

    @ErrorHandler.handle_errors()
    def create_horizontal_layout(self, parent=None) -> QtWidgets.QHBoxLayout:
        """Create a horizontal layout."""
        layout = QtWidgets.QHBoxLayout(parent)
        logger.debug("Created horizontal layout")
        return layout


    @ErrorHandler.handle_errors()
    def create_label(self, font_size: int = DEFAULT_FONT_SIZE, text: str = "", 
                        alignment: QtCore.Qt.AlignmentFlag = DEFAULT_ALIGNMENT, parent=None) -> QtWidgets.QLabel:
        """Create a label with specified font size, text, and alignment."""
        self._validate_font_size(font_size)
        label = self._create_widget(QtWidgets.QLabel, parent, text=text)
        self._set_font(label, font_size)
        label.setAlignment(alignment)
        logger.debug(f"Created label: {text}")
        return label
    
    @ErrorHandler.handle_errors()
    def create_button(self, text: str, callback=None, parent=None) -> QtWidgets.QPushButton:
        """Create a button with specified text and an optional callback."""
        button = self._create_widget(QtWidgets.QPushButton, parent, text=text)
        self._connect_callback(button.clicked, callback)
        logger.debug(f"Created button: {text}")
        return button

    @ErrorHandler.handle_errors()
    def create_line_edit(self, placeholder_text: str = "", parent=None) -> QtWidgets.QLineEdit:
        """Create a line edit with an optional placeholder text."""
        line_edit = self._create_widget(QtWidgets.QLineEdit, parent)
        line_edit.setPlaceholderText(placeholder_text)
        logger.debug(f"Created line edit with placeholder: {placeholder_text}")
        return line_edit

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