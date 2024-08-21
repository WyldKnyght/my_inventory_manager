# src/user_interface/base_widget.py
from PyQt6 import QtCore, QtGui, QtWidgets

class BaseWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def create_group_box(self, title: str, parent=None) -> QtWidgets.QGroupBox:
        """Create a group box with a specified title."""
        return self._create_widget(QtWidgets.QGroupBox, parent, title=title)

    def create_grid_layout(self, parent=None) -> QtWidgets.QGridLayout:
        """Create a grid layout."""
        return QtWidgets.QGridLayout(parent)

    def create_vertical_layout(self, parent=None) -> QtWidgets.QVBoxLayout:
        """Create a vertical layout."""
        return QtWidgets.QVBoxLayout(parent)

    def create_horizontal_layout(self, parent=None) -> QtWidgets.QHBoxLayout:
        """Create a horizontal layout."""
        return QtWidgets.QHBoxLayout(parent)

    def create_label(self, font_size: int, text: str, 
                        alignment: QtCore.Qt.AlignmentFlag = QtCore.Qt.AlignmentFlag.AlignCenter, parent=None) -> QtWidgets.QLabel:
        """Create a label with specified font size, text, and alignment."""
        self._validate_font_size(font_size)
        label = self._create_widget(QtWidgets.QLabel, parent, text=text)
        self._set_font(label, font_size)
        label.setAlignment(alignment)
        return label

    def create_button(self, text: str, callback=None, parent=None) -> QtWidgets.QPushButton:
        """Create a button with specified text and an optional callback."""
        button = self._create_widget(QtWidgets.QPushButton, parent, text=text)
        self._connect_callback(button.clicked, callback)
        return button

    def create_line_edit(self, placeholder_text: str = "", parent=None) -> QtWidgets.QLineEdit:
        """Create a line edit with an optional placeholder text."""
        line_edit = self._create_widget(QtWidgets.QLineEdit, parent)
        line_edit.setPlaceholderText(placeholder_text)
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