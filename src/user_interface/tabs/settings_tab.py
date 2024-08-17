# src/user_interface/tabs/settings_tab.py

from PyQt6 import QtWidgets, QtGui
from user_interface.base_widget import BaseWidget
from user_interface.dialogs.manage_table_dialog import ManageTableDialog

class SettingsTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        # Create a single button for managing tables
        manage_button = QtWidgets.QPushButton("Manage Tables")
        manage_button.setMinimumSize(200, 100)
        manage_button.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Weight.Bold))
        manage_button.clicked.connect(self.manage_tables)
        main_layout.addWidget(manage_button)

        main_layout.addStretch(1)  # Add stretch to push widgets to the top

    def manage_tables(self):
        dialog = ManageTableDialog(self)
        dialog.exec()