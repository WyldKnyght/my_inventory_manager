# src/utils/ui_helpers.py

from PyQt6 import QtWidgets, QtGui

def create_button(parent, text, slot):
    """Create a QPushButton with specified text and slot function."""
    button = QtWidgets.QPushButton(text, parent)
    button.setMinimumSize(200, 50)
    button.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Weight.Bold))
    button.clicked.connect(slot)
    return button