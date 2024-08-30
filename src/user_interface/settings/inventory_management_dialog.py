# src/user_interface/dialogs/inventory/inventory_management_dialog.py
from PyQt6 import QtWidgets
from controllers.inventory_controller import InventoryController
from user_interface.inventory.inventory_record_dialog import InventoryRecordDialog
from user_interface.common.button_utils import add_action_buttons
from user_interface.common.table_utils import configure_table_headers, populate_table_with_data
from user_interface.common.error_warning_dialog import show_error_message, show_warning_message
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import UIConfig, TableSettings, Titles, Buttons, MessageBoxTitles

class InventoryManagementDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(Titles.INVENTORY_MANAGEMENT)
        self.resize(*UIConfig.DIALOG_SIZE)
        self.inventory_controller = InventoryController()
        self.setup_ui()
        logger.info("Initialized InventoryManagementDialog")

    @ErrorHandler.handle_errors()
    def setup_ui(self):
        """Set up the UI components."""
        layout = QtWidgets.QVBoxLayout(self)
        self.data_table = self.create_data_table()
        layout.addWidget(self.data_table)

        button_layout = add_action_buttons(self, [
            (Buttons.ADD, self.add_entry),
            (Buttons.EDIT, self.edit_entry),
            (Buttons.DELETE, self.delete_entry)
        ])
        layout.addLayout(button_layout)

        self.load_catalog()
        logger.debug("Set up UI for InventoryManagementDialog")

    @ErrorHandler.handle_errors()
    def create_data_table(self) -> QtWidgets.QTableWidget:
        """Create and configure the data table."""
        table = QtWidgets.QTableWidget(self)
        table.setSizePolicy(*TableSettings.POLICY)
        logger.debug("Created data table for inventory management")
        return table

    @ErrorHandler.handle_errors()
    def load_catalog(self):
        """Load catalog data and display it in the table."""
        try:
            column_headers, data = self.inventory_controller.get_data_by_table("Catalog")
            configure_table_headers(self.data_table, column_headers)
            populate_table_with_data(self.data_table, data, column_headers)
            logger.info(f"Loaded {len(data)} catalog items")
        except Exception as e:
            error_msg = f"Failed to load catalog data: {str(e)}"
            logger.error(error_msg)
            show_error_message(self, MessageBoxTitles.ERROR, error_msg)

    @ErrorHandler.handle_errors()
    def add_entry(self):
        """Add a new catalog entry."""
        column_headers, _ = self.inventory_controller.get_data_by_table("Catalog")
        dialog = InventoryRecordDialog(table_name="Catalog", record_data=None, columns=column_headers, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            new_data = dialog.get_data()
            if new_data is None:
                return
            self.inventory_controller.add_item("Catalog", new_data)
            self.load_catalog()
            logger.info("Added new catalog entry")

    @ErrorHandler.handle_errors()
    def edit_entry(self):
        """Edit the selected catalog entry."""
        selected_row = self.data_table.currentRow()
        if selected_row == -1:
            show_warning_message(self, Titles.EDIT_RECORD, "Please select a record to edit.")
            return

        current_data = self.get_selected_record_data(selected_row)
        column_headers, _ = self.inventory_controller.get_data_by_table("Catalog")
        dialog = InventoryRecordDialog(table_name="Catalog", record_data=current_data, columns=column_headers, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            updated_data = dialog.get_data()
            item_id = current_data["item_id"]
            self.inventory_controller.update_item("Catalog", updated_data, item_id, "item_id")
            self.load_catalog()
            logger.info(f"Edited catalog entry with ID: {item_id}")

    @ErrorHandler.handle_errors()
    def delete_entry(self):
        """Delete the selected catalog entry."""
        selected_row = self.data_table.currentRow()
        if selected_row == -1:
            show_warning_message(self, Titles.DELETE_RECORD, "Please select a record to delete.")
            return

        current_data = self.get_selected_record_data(selected_row)
        item_id = current_data["item_id"]
        confirm = QtWidgets.QMessageBox.question(
            self,
            Titles.CONFIRM_DELETION,
            f"Are you sure you want to delete the catalog item with ID {item_id}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            self.inventory_controller.delete_item("Catalog", item_id, "item_id")
            self.load_catalog()
            logger.info(f"Deleted catalog entry with ID: {item_id}")

    @ErrorHandler.handle_errors()
    def get_selected_record_data(self, row):
        """Retrieve data from the selected row."""
        data = {}
        for col in range(self.data_table.columnCount()):
            header = self.data_table.horizontalHeaderItem(col).text()
            item = self.data_table.item(row, col)
            data[header] = item.text() if item else ''
        logger.debug(f"Retrieved data for selected row: {row}")
        return data