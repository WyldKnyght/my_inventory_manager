# src/user_interface/tabs/inventory_tab.py

from PyQt6 import QtWidgets
from user_interface.framework.base_widget import BaseWidget
from controllers.inventory_controller import InventoryController
from utils.ui_helpers import configure_table_headers, populate_table_with_data

class InventoryTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inventory_controller = InventoryController()
        self.setup_ui()
        self.load_catalog()

    def setup_ui(self):
        """Set up the UI components for the Inventory tab."""
        main_layout = self.create_vertical_layout(self)
        self.catalog_table = self.create_catalog_table()
        main_layout.addWidget(self.catalog_table)

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

    def show_error_message(self, message: str):
        """Display an error message."""
        QtWidgets.QMessageBox.critical(self, "Error", message)