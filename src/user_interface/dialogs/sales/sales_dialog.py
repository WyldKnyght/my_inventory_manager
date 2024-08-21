# src/user_interface/dialogs/sales_dialog.py

from PyQt6 import QtWidgets

class SalesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sales Settings")
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Sales settings configuration goes here.", self)
        layout.addWidget(label)