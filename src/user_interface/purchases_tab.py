# src/user_interface/purchases_tab.py
from PyQt6 import QtWidgets
from controllers.purchases_controller import PurchasesController
from user_interface.common.base_widget import BaseWidget
from user_interface.purchases.purchases_table import PurchasesTable
from user_interface.purchases.purchases_actions import PurchasesActions
from configs.ui_config import (
    PURCHASES_TAB_TITLE, PURCHASES_SUBTAB_TITLE, EXPENSES_SUBTAB_TITLE,
    SEARCH_GROUP_TITLE, PURCHASES_GROUP_TITLE, ACTIONS_GROUP_TITLE,
    SEARCH_PLACEHOLDER, EXPENSES_PLACEHOLDER
)

class PurchasesTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(PURCHASES_TAB_TITLE)
        self.purchases_controller = PurchasesController()
        self.purchases_table = None
        self.purchases_actions = None
        self.status_bar = QtWidgets.QStatusBar(self)
        self.setup_ui()

    def setup_ui(self):
        layout = self.create_vertical_layout(self)
        
        tabs = QtWidgets.QTabWidget(self)
        layout.addWidget(tabs)

        purchases_widget = self.create_purchases_tab()
        tabs.addTab(purchases_widget, PURCHASES_SUBTAB_TITLE)

        expenses_widget = self.create_expenses_tab()
        tabs.addTab(expenses_widget, EXPENSES_SUBTAB_TITLE)

        layout.addWidget(self.status_bar)

    def create_purchases_tab(self):
        widget = QtWidgets.QWidget(self)
        layout = self.create_vertical_layout(widget)

        # Search group
        search_group = self.create_group_box(SEARCH_GROUP_TITLE)
        search_layout = self.create_horizontal_layout()
        self.search_bar = self.create_line_edit(SEARCH_PLACEHOLDER, parent=search_group)
        self.search_bar.textChanged.connect(self.filter_purchases)
        search_layout.addWidget(self.search_bar)
        search_group.setLayout(search_layout)
        layout.addWidget(search_group)

        # Purchases table group
        table_group = self.create_group_box(PURCHASES_GROUP_TITLE)
        table_layout = self.create_vertical_layout()
        self.purchases_table = PurchasesTable(self)
        table_layout.addWidget(self.purchases_table)
        table_group.setLayout(table_layout)
        layout.addWidget(table_group)

        # Actions group
        actions_group = self.create_group_box(ACTIONS_GROUP_TITLE)
        self.purchases_actions = PurchasesActions(self, self.purchases_table, self.purchases_controller)
        button_layout = self.purchases_actions.create_action_buttons()
        actions_group.setLayout(button_layout)
        layout.addWidget(actions_group)

        self.purchases_table.load_purchases_data(self.purchases_controller, self.status_bar)

        return widget

    def create_expenses_tab(self):
        widget = QtWidgets.QWidget(self)
        layout = self.create_vertical_layout(widget)
        
        label = self.create_label(12, EXPENSES_PLACEHOLDER)
        layout.addWidget(label)
        
        return widget

    def filter_purchases(self):
        self.purchases_table.filter_purchases(self.search_bar.text())