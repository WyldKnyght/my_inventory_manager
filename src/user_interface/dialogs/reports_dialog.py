# src/user_interface/dialogs/reports_dialog.py

from PyQt6 import QtWidgets

class ReportsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Reports Settings")
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Reports settings configuration goes here.", self)
        layout.addWidget(label)