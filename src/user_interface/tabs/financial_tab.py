# src/user_interface/tabs/financial_tab.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from .financial_subtabs.transactions_tab import TransactionsTab
from .financial_subtabs.accounts_tab import AccountsTab
from .financial_subtabs.reports_tab import ReportsTab

class FinancialTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Create sub-tabs
        self.sub_tabs = QTabWidget()
        
        # Transactions sub-tab
        self.transactions_tab = TransactionsTab(self.db_manager)
        self.sub_tabs.addTab(self.transactions_tab, "Transactions")
        
        # Accounts sub-tab (placeholder for now)
        self.accounts_tab = AccountsTab(self.db_manager)
        self.sub_tabs.addTab(self.accounts_tab, "Accounts")
        
        # Reports sub-tab (placeholder for now)
        self.reports_tab = ReportsTab(self.db_manager)
        self.sub_tabs.addTab(self.reports_tab, "Reports")
        
        layout.addWidget(self.sub_tabs)
        self.setLayout(layout)