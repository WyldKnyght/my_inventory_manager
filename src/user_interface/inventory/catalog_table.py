# src/user_interface/inventory/catalog_table.py
from PyQt6 import QtWidgets
from utils.error_manager import ErrorManager
from utils.custom_logging import logger
from user_interface.common.base_widget import BaseWidget
from user_interface.common.table_utils import configure_table_headers, populate_table_with_data
from configs.ui_config import TableSettings
from controllers.inventory_controller import InventoryController

class CatalogTable(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inventory_controller = InventoryController()
        self.setup_ui()
        self.load_catalog()

    @ErrorManager.handle_errors()
    def setup_ui(self):
        layout = self.create_vertical_layout()
        self.table = self.create_catalog_table()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def create_catalog_table(self) -> QtWidgets.QTableWidget:
        table = QtWidgets.QTableWidget(self)
        table.setSizePolicy(*TableSettings.POLICY)
        table.setSortingEnabled(True)
        table.itemSelectionChanged.connect(self.on_row_selected)
        return table

    @ErrorManager.handle_errors()
    def load_catalog(self):
        logger.debug("Loading catalog data...")
        column_headers, catalog_items = self.inventory_controller.get_data_by_table("Catalog")
        self.display_catalog(column_headers, catalog_items)

    @ErrorManager.handle_errors()
    def display_catalog(self, column_headers, catalog_items):
        configure_table_headers(self.table, column_headers)
        populate_table_with_data(self.table, catalog_items, column_headers)

    @ErrorManager.handle_errors()
    def on_row_selected(self):
        if selected_items := self.table.selectedItems():
            row = selected_items[0].row()
            item_id = self.table.item(row, 0).text()
            logger.info(f"Selected item with ID: {item_id}")

    def get_selected_item_id(self):
        if selected_items := self.table.selectedItems():
            row = selected_items[0].row()
            return self.table.item(row, 0).text()
        return None