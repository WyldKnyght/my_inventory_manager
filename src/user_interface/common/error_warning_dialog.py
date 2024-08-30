# src/user_interface/common/error_warning_dialog.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from configs.ui_config import ERROR_TITLE, WARNING_TITLE, INFO_TITLE

def show_error_message(parent, title: str, message: str):
    """Display an error message."""
    QtWidgets.QMessageBox.critical(parent, title or ERROR_TITLE, message)
    logger.error(f"Error message displayed: {title} - {message}")

def show_warning_message(parent, title: str, message: str):
    """Display a warning message."""
    QtWidgets.QMessageBox.warning(parent, title or WARNING_TITLE, message)
    logger.warning(f"Warning message displayed: {title} - {message}")

def show_info_message(parent, title: str, message: str):
    """Display an information message."""
    QtWidgets.QMessageBox.information(parent, title or INFO_TITLE, message)
    logger.info(f"Info message displayed: {title} - {message}")