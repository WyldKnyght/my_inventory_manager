# src/user_interface/reports/reports_dialog.py

from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager

class ReportsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Reports Settings")
        self.setup_ui()
        logger.info("Initialized ReportsDialog")

    @ErrorManager.handle_errors()
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Reports settings configuration goes here.", self)
        layout.addWidget(label)
        logger.debug("Set up ReportsDialog UI")