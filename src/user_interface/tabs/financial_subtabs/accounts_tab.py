# src/user_interface/tabs/financial_subtabs/accounts_tab.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AccountsTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Accounts tab - To be implemented"))
        self.setLayout(layout)

