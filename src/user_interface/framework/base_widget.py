# src/user_interface/base_widget.py
from PyQt6 import QtCore, QtGui, QtWidgets

class BaseWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def create_group_box(self, title: str, parent=None) -> QtWidgets.QGroupBox:
        group_box = QtWidgets.QGroupBox(parent)
        group_box.setTitle(title)
        return group_box

    def create_grid_layout(self, parent=None) -> QtWidgets.QGridLayout:
        return QtWidgets.QGridLayout(parent)

    def create_vertical_layout(self, parent=None) -> QtWidgets.QVBoxLayout:
        return QtWidgets.QVBoxLayout(parent)

    def create_horizontal_layout(self, parent=None) -> QtWidgets.QHBoxLayout:
        return QtWidgets.QHBoxLayout(parent)

    def create_label(self, font_size: int, text: str, 
                     alignment: QtCore.Qt.AlignmentFlag = QtCore.Qt.AlignmentFlag.AlignCenter, parent=None) -> QtWidgets.QLabel:
        assert isinstance(font_size, int) and font_size > 0, "Font size must be a positive integer."
        label = QtWidgets.QLabel(parent)
        font = QtGui.QFont()
        font.setPointSize(font_size)
        label.setFont(font)
        label.setAlignment(alignment)
        label.setText(text)
        return label

    def create_button(self, text: str, callback=None, parent=None) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton(text, parent)
        if callback:
            assert callable(callback), "Callback must be callable."
            button.clicked.connect(callback)
        return button

    def create_line_edit(self, placeholder_text: str = "", parent=None) -> QtWidgets.QLineEdit:
        line_edit = QtWidgets.QLineEdit(parent)
        line_edit.setPlaceholderText(placeholder_text)
        return line_edit