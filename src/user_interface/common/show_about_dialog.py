# src/user_interface/common/show_about_dialog.py

from PyQt6.QtWidgets import QMessageBox
from configs.constants import APP_TITLE, APP_VERSION

def show_about_dialog(parent):
    QMessageBox.about(parent, "About", f"{APP_TITLE} v{APP_VERSION}\n\nA simple inventory and financial management system.")
