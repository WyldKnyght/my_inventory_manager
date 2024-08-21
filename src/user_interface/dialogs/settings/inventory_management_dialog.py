# src/user_interface/dialogs/inventory/inventory_management_dialog.py

from PyQt6 import QtWidgets
from controllers.inventory_controller import InventoryController
from user_interface.dialogs.record_dialog.inventory_record_dialog import InventoryRecordDialog
from utils.ui_helpers import add_action_buttons, configure_table_headers, populate_table_with_data

class InventoryManagementDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inventory Management")
        self.resize(800, 600)
        self.inventory_controller = InventoryController()
        self.setup_ui()

    def setup_ui(self):
        """Set up the UI components."""
        layout = QtWidgets.QVBoxLayout(self)
        self.data_table = self.create_data_table()
        layout.addWidget(self.data_table)

        button_layout = add_action_buttons(self, [
            ("Add", self.add_entry),
            ("Edit", self.edit_entry),
            ("Delete", self.delete_entry)
        ])
        layout.addLayout(button_layout)

        self.load_catalog()

    def create_data_table(self) -> QtWidgets.QTableWidget:
        """Create and configure the data table."""
        table = QtWidgets.QTableWidget(self)
        table.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        return table

    def load_catalog(self):
        """Load catalog data and display it in the table."""
        try:
            column_headers, data = self.inventory_controller.get_data_by_table("Catalog")
            configure_table_headers(self.data_table, column_headers)
            populate_table_with_data(self.data_table, data, column_headers)
        except Exception as e:
            self.show_error_message(f"Failed to load catalog data: {e}")

    def add_entry(self):
        """Add a new catalog entry."""
        column_headers, _ = self.inventory_controller.get_data_by_table("Catalog")
        dialog = InventoryRecordDialog(record_data=None, columns=column_headers, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            new_data = dialog.get_data()
            if new_data is None:
                return
            self.inventory_controller.add_item("Catalog", new_data)
            self.load_catalog()

    def edit_entry(self):
        """Edit the selected catalog entry."""
        selected_row = self.data_table.currentRow()
        if selected_row == -1:
            self.show_warning_message("Edit Record", "Please select a record to edit.")
            return

        current_data = self.get_selected_record_data(selected_row)
        column_headers, _ = self.inventory_controller.get_data_by_table("Catalog")
        dialog = InventoryRecordDialog(record_data=current_data, columns=column_headers, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            updated_data = dialog.get_data()
            item_id = current_data["item_id"]
            self.inventory_controller.update_item("Catalog", updated_data, item_id, "item_id")
            self.load_catalog()

    def delete_entry(self):
        """Delete the selected catalog entry."""
        selected_row = self.data_table.currentRow()
        if selected_row == -1:
            self.show_warning_message("Delete Record", "Please select a record to delete.")
            return

        current_data = self.get_selected_record_data(selected_row)
        item_id = current_data["item_id"]
        self.inventory_controller.delete_item("Catalog", item_id, "item_id")
        self.load_catalog()

    def get_selected_record_data(self, row):
        """Retrieve data from the selected row."""
        data = {}
        for col in range(self.data_table.columnCount()):
            header = self.data_table.horizontalHeaderItem(col).text()
            item = self.data_table.item(row, col)
            data[header] = item.text() if item else ''
        return data

    def show_error_message(self, message: str):
        """Display an error message."""
        QtWidgets.QMessageBox.critical(self, "Error", message)