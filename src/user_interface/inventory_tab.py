# src/user_interface/inventory_tab.py
from PyQt6 import QtWidgets
from user_interface.common.base_widget import BaseWidget
from controllers.inventory_controller import InventoryController
from user_interface.common.table_utils import configure_table_headers, populate_table_with_data
from configs.ui_config import (
    INVENTORY_TAB_TITLE, SEARCH_GROUP_TITLE, CATALOG_GROUP_TITLE,
    SEARCH_PLACEHOLDER, ERROR_TITLE
)

class InventoryTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(INVENTORY_TAB_TITLE)
        self.inventory_controller = InventoryController()
        self.setup_ui()
        self.load_catalog()

    def setup_ui(self):
        """Set up the UI components for the Inventory tab."""
        main_layout = self.create_vertical_layout(self)

        # Search group
        search_group = self.create_group_box(SEARCH_GROUP_TITLE)
        search_layout = self.create_horizontal_layout()
        self.search_bar = self.create_line_edit(SEARCH_PLACEHOLDER, parent=search_group)
        self.search_bar.textChanged.connect(self.filter_inventory)
        search_layout.addWidget(self.search_bar)
        search_group.setLayout(search_layout)
        main_layout.addWidget(search_group)

        # Catalog table group
        catalog_group = self.create_group_box(CATALOG_GROUP_TITLE)
        catalog_layout = self.create_vertical_layout()
        self.catalog_table = self.create_catalog_table()
        catalog_layout.addWidget(self.catalog_table)
        catalog_group.setLayout(catalog_layout)
        main_layout.addWidget(catalog_group)

    def create_catalog_table(self) -> QtWidgets.QTableWidget:
        """Create and configure the catalog table."""
        table = QtWidgets.QTableWidget(self)
        table.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        table.setSortingEnabled(True)
        return table

    def load_catalog(self):
        """Load catalog data from the database and display it in the table."""
        try:
            column_headers, catalog_items = self.inventory_controller.get_data_by_table("Catalog")
            self.display_catalog(column_headers, catalog_items)
        except Exception as e:
            self.show_error_message(str(e))

    def display_catalog(self, column_headers, catalog_items):
        """Display the catalog items in the table."""
        configure_table_headers(self.catalog_table, column_headers)
        populate_table_with_data(self.catalog_table, catalog_items, column_headers)

    def filter_inventory(self):
        """Filter the inventory based on the search bar text."""
        # Implement inventory filtering logic here
        pass

    def show_error_message(self, message: str):
        """Display an error message."""
        QtWidgets.QMessageBox.critical(self, ERROR_TITLE, message)