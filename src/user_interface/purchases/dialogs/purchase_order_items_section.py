# src/user_interface/purchases/dialogs/purchase_order_items_section.py
from PyQt6 import QtWidgets
from controllers.inventory_controller import InventoryController
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import TableSettings, Buttons, Titles

class PurchaseOrderItemsSection(QtWidgets.QGroupBox):
    def __init__(self, inventory_controller: InventoryController, parent=None):
        super().__init__(Titles.GroupBoxes.ORDER_ITEMS, parent)
        self.inventory_controller = inventory_controller
        self.setup_ui()
        logger.info("Initialized PurchaseOrderItemsSection")

    @ErrorHandler.handle_errors()
    def setup_ui(self):
        """Set up the UI components for the purchase order items section."""
        layout = QtWidgets.QVBoxLayout(self)
        
        self.items_table = QtWidgets.QTableWidget(0, len(TableSettings.HEADERS["purchase_order_items"]), self)
        self.items_table.setHorizontalHeaderLabels(TableSettings.HEADERS["purchase_order_items"])
        self.items_table.setSizePolicy(*TableSettings.POLICY)
        layout.addWidget(self.items_table)

        add_item_button = QtWidgets.QPushButton(Buttons.ADD_ITEM, self)
        add_item_button.clicked.connect(self.add_item_row)
        layout.addWidget(add_item_button)
        logger.debug("Set up UI for PurchaseOrderItemsSection")

    @ErrorHandler.handle_errors()
    def add_item_row(self):
        """Add a new row to the items table."""
        row = self.items_table.rowCount()
        self.items_table.insertRow(row)
        
        product_combo = QtWidgets.QComboBox()
        products = self.inventory_controller.get_products()
        product_combo.addItems(products)
        self.items_table.setCellWidget(row, 0, product_combo)

        for i in range(1, 4):
            self.items_table.setItem(row, i, QtWidgets.QTableWidgetItem())

        delete_button = QtWidgets.QPushButton(Buttons.DELETE)
        delete_button.clicked.connect(lambda: self.delete_item_row(row))
        self.items_table.setCellWidget(row, 4, delete_button)
        logger.debug(f"Added new item row at index {row}")

    @ErrorHandler.handle_errors()
    def delete_item_row(self, row):
        """Delete a row from the items table."""
        self.items_table.removeRow(row)
        logger.debug(f"Deleted item row at index {row}")

    @ErrorHandler.handle_errors()
    def populate_items(self, items):
        """Populate the items table with existing data."""
        self.items_table.setRowCount(0)
        for item in items:
            self.add_item_row()
            row = self.items_table.rowCount() - 1
            self.items_table.cellWidget(row, 0).setCurrentText(item.get('product', ''))
            self.items_table.item(row, 1).setText(str(item.get('quantity', '')))
            self.items_table.item(row, 2).setText(str(item.get('unit_price', '')))
            self.items_table.item(row, 3).setText(str(item.get('total', '')))
        logger.debug(f"Populated items table with {len(items)} items")

    @ErrorHandler.handle_errors()
    def get_data(self) -> list:
        """Retrieve data from the items table."""
        items = []
        for row in range(self.items_table.rowCount()):
            item = {
                'product': self.items_table.cellWidget(row, 0).currentText(),
                'quantity': self.items_table.item(row, 1).text(),
                'unit_price': self.items_table.item(row, 2).text(),
                'total': self.items_table.item(row, 3).text()
            }
            items.append(item)
        logger.debug(f"Retrieved data for {len(items)} items")
        return items