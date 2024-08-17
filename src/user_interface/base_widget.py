# src\user_interface\base_widget.py
from PyQt6 import QtCore, QtGui, QtWidgets

class BaseWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def create_group_box(self, title: str) -> QtWidgets.QGroupBox:
        """Create a QGroupBox with a given title."""
        group_box = QtWidgets.QGroupBox(self)
        group_box.setTitle(title)
        return group_box

    def create_grid_layout(self) -> QtWidgets.QGridLayout:
        """Create a QGridLayout."""
        return QtWidgets.QGridLayout()

    def create_vertical_layout(self) -> QtWidgets.QVBoxLayout:
        """Create a QVBoxLayout."""
        return QtWidgets.QVBoxLayout()

    def create_horizontal_layout(self) -> QtWidgets.QHBoxLayout:
        """Create a QHBoxLayout."""
        return QtWidgets.QHBoxLayout()

    def create_label(self, font_size: int, text: str, 
                     alignment: QtCore.Qt.AlignmentFlag = QtCore.Qt.AlignmentFlag.AlignCenter) -> QtWidgets.QLabel:
        """
        Create a QLabel with specified font size, text, and alignment.

        :param font_size: The size of the font.
        :param text: The text to display in the label.
        :param alignment: The alignment of the text within the label.
        :return: A QLabel instance.
        :raises ValueError: If font_size is not a positive integer.
        """
        if not isinstance(font_size, int) or font_size <= 0:
            raise ValueError("Font size must be a positive integer.")
        label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(font_size)
        label.setFont(font)
        label.setAlignment(alignment)
        label.setText(text)
        return label

    def create_button(self, text: str, callback=None) -> QtWidgets.QPushButton:
        """
        Create a QPushButton with specified text and optional callback.

        :param text: The text to display on the button.
        :param callback: A callable to connect to the button's clicked signal.
        :return: A QPushButton instance.
        :raises ValueError: If callback is not callable.
        """
        button = QtWidgets.QPushButton(self)
        button.setText(text)
        if callback:
            if not callable(callback):
                raise ValueError("Callback must be callable.")
            button.clicked.connect(callback)
        return button

    def create_line_edit(self, placeholder_text: str = "") -> QtWidgets.QLineEdit:
        """
        Create a QLineEdit with an optional placeholder text.

        :param placeholder_text: The placeholder text to display in the line edit.
        :return: A QLineEdit instance.
        """
        line_edit = QtWidgets.QLineEdit(self)
        line_edit.setPlaceholderText(placeholder_text)
        return line_edit