# src/user_interface/dialogs/common/generic_management_dialog.py
from PyQt6 import QtWidgets, QtCore
from controllers.inventory_controller import InventoryController
from .data_table_dialog import create_data_table, load_data
from .action_buttons_dialog import create_action_buttons
from .get_primary_keys import get_primary_key
from .error_warning_dialog import show_error_message, show_warning_message
from user_interface.dialogs.record_dialog.inventory_record_dialog import InventoryRecordDialog

class GenericManagementDialog(QtWidgets.QDialog):
    EDIT_RECORD_TITLE = "Edit Record"

    def __init__(self, table_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{table_name} Management")
        self.resize(800, 600)
        self.table_name = table_name
        self.inventory_controller = InventoryController()
        self.setup_ui()

    def setup_ui(self):
        """Set up the UI components."""
        layout = QtWidgets.QVBoxLayout(self)
        self.data_table = create_data_table()
        layout.addWidget(self.data_table)

        button_layout = create_action_buttons(self)
        layout.addLayout(button_layout)

        load_data(self.table_name, self.data_table, self.inventory_controller)

    def add_entry(self):
        """Add a new entry."""
        column_headers = [self.data_table.horizontalHeaderItem(col).text() for col in range(1, self.data_table.columnCount())]
        dialog = InventoryRecordDialog(table_name=self.table_name, record_data=None, columns=column_headers, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            if new_data := dialog.get_data():
                self.inventory_controller.add_item(self.table_name, new_data)
                load_data(self.table_name, self.data_table, self.inventory_controller)


    def edit_entry(self):
        """Edit the selected entries."""
        selected_items = self.get_selected_items()
        if not selected_items:
            show_warning_message(self, self.EDIT_RECORD_TITLE, "Please select at least one record to edit.")
            return

        if len(selected_items) > 1:
            show_warning_message(self, self.EDIT_RECORD_TITLE, "Please select only one record to edit.")
            return

        current_data = selected_items[0]
        column_headers = [self.data_table.horizontalHeaderItem(col).text() for col in range(1, self.data_table.columnCount())]
        dialog = InventoryRecordDialog(table_name=self.table_name, record_data=current_data, columns=column_headers, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            if updated_data := dialog.get_data():
                primary_key = get_primary_key(self.table_name)
                if primary_key not in current_data:
                    show_error_message(self, self.EDIT_RECORD_TITLE, f"Primary key '{primary_key}' not found in the selected record.")
                    return
                self.inventory_controller.update_item(self.table_name, updated_data, current_data[primary_key], primary_key)
                load_data(self.table_name, self.data_table, self.inventory_controller)

    def delete_entry(self):
        """Delete the selected entries."""
        selected_items = self.get_selected_items()
        if not selected_items:
            show_warning_message(self, "Delete Record", "Please select at least one record to delete.")
            return

        confirm = QtWidgets.QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete {len(selected_items)} selected record(s)?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        
        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            primary_key = get_primary_key(self.table_name)
            for item in selected_items:
                self.inventory_controller.delete_item(self.table_name, item[primary_key], primary_key)
            load_data(self.table_name, self.data_table, self.inventory_controller)

    def get_selected_items(self):
        """Get the selected items based on checkboxes."""
        selected_items = []
        for row in range(self.data_table.rowCount()):
            if self.data_table.item(row, 0).checkState() == QtCore.Qt.CheckState.Checked:
                item_data = {}
                for col in range(1, self.data_table.columnCount()):
                    header = self.data_table.horizontalHeaderItem(col).text()
                    item_data[header] = self.data_table.item(row, col).text()
                selected_items.append(item_data)
        return selected_items