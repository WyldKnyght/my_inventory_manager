# src/user_interface/dialogs/purchases_dialog.py

from PyQt6 import QtWidgets

class PurchasesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Purchases Settings")
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Purchases settings configuration goes here.", self)
        layout.addWidget(label)