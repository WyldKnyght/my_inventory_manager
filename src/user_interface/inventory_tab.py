# src/user_interface/inventory_tab.py

from configs.config_manager import config_manager
from utils.error_manager import ErrorManager
from utils.custom_logging import logger
from user_interface.common.base_widget import BaseWidget
from .inventory.catalog_table import CatalogTable
from .inventory.search_group import SearchGroup
from .inventory.item_management import ItemManagement

class InventoryTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(config_manager.get('ui.tab_titles.inventory', "Inventory"))
        logger.info("Inventory tab initialized.")
        self.setup_ui()

    @ErrorManager.handle_errors()
    def setup_ui(self):
        """Set up the UI components for the Inventory tab."""
        main_layout = self.create_vertical_layout(self)

        self.search_group = SearchGroup(self)
        main_layout.addWidget(self.search_group)

        self.catalog_table = CatalogTable(self)
        main_layout.addWidget(self.catalog_table)

        self.item_management = ItemManagement(self.catalog_table)

    @ErrorManager.handle_errors()
    def refresh_catalog(self):
        """Refresh the catalog data."""
        logger.info("Refreshing catalog data")
        self.catalog_table.load_catalog()