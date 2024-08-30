# src/user_interface/purchases/purchases_table.py
from PyQt6 import QtWidgets
from user_interface.common.table_utils import configure_table_headers, populate_table_with_data
from user_interface.common.error_warning_dialog import show_error_message
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import TableSettings, MessageBoxTitles

class PurchasesTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.setSortingEnabled(True)
        self.setSizePolicy(*TableSettings.POLICY)
        logger.info("Initialized PurchasesTable")

    @ErrorHandler.handle_errors()
    def load_purchases_data(self, purchases_controller, status_bar):
        status_bar.showMessage("Loading purchases data...")
        try:
            purchases = purchases_controller.get_all_purchases()
            if purchases is None or len(purchases) == 0:
                self.setRowCount(0)
                self.setColumnCount(0)
                status_bar.showMessage("No purchases found", 3000)
                logger.info("No purchases found")
                return

            headers = TableSettings.HEADERS.get("purchases", ["PO Number", "Date", "Vendor", "Total Amount"])
            configure_table_headers(self, headers)
            populate_table_with_data(self, purchases, headers)
            status_bar.showMessage("Purchases data loaded successfully", 3000)
            logger.info(f"Loaded {len(purchases)} purchases")
        except Exception as e:
            error_msg = f"Failed to load purchases: {str(e)}"
            show_error_message(self.parent(), MessageBoxTitles.ERROR, error_msg)
            status_bar.showMessage("Failed to load purchases data", 3000)
            logger.error(error_msg)

    @ErrorHandler.handle_errors()
    def filter_purchases(self, search_text):
        search_text = search_text.lower()
        for row in range(self.rowCount()):
            match = False
            for column in range(self.columnCount()):
                item = self.item(row, column)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.setRowHidden(row, not match)
        logger.debug(f"Filtered purchases with search text: {search_text}")

    @ErrorHandler.handle_errors()
    def get_selected_purchase_id(self):
        selected_row = self.currentRow()
        purchase_id = None if selected_row == -1 else self.item(selected_row, 0).text()
        logger.debug(f"Selected purchase ID: {purchase_id}")
        return purchase_id