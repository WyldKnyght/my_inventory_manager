# src/user_interface/tabs/financial_subtabs/reports_tab.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ReportsTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Reports tab - To be implemented"))
        self.setLayout(layout)