# src/user_interface/dialogs/common/error_warning_dialog.py
from PyQt6 import QtWidgets

def show_error_message(parent, title: str, message: str):
    """Display an error message."""
    QtWidgets.QMessageBox.critical(parent, title, message)

def show_warning_message(parent, title: str, message: str):
    """Display a warning message."""
    QtWidgets.QMessageBox.warning(parent, title, message)