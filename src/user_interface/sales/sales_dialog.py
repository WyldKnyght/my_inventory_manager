# src/user_interface/sales/sales_dialog.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager

class SalesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sales Settings")
        self.setup_ui()
        logger.info("Initialized SalesDialog")

    @ErrorManager.handle_errors()
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Sales settings configuration goes here.", self)
        layout.addWidget(label)
        logger.debug("Set up SalesDialog UI")