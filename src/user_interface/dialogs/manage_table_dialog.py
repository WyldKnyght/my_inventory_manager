from PyQt6 import QtWidgets
from controllers.manage_table_controller import ManageTableController
from user_interface.dialogs.record_dialog import RecordDialog

class ManageTableDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Manage Tables")
        self.controller = ManageTableController()
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        # Combo box for selecting the table
        self.table_selector = QtWidgets.QComboBox(self)
        self.table_selector.addItems(["Accounts", "Vendor", "Manufacturer", "Brand", "Customer", "Categories"])
        self.table_selector.currentIndexChanged.connect(self.load_data)
        layout.addWidget(self.table_selector)

        # Table widget to display data
        self.table_widget = QtWidgets.QTableWidget()
        layout.addWidget(self.table_widget)

        # Buttons for actions
        button_layout = QtWidgets.QHBoxLayout()
        self.add_button = QtWidgets.QPushButton("Add")
        self.edit_button = QtWidgets.QPushButton("Edit")
        self.delete_button = QtWidgets.QPushButton("Delete")
        self.close_button = QtWidgets.QPushButton("Close")

        self.add_button.clicked.connect(self.add_record)
        self.edit_button.clicked.connect(self.edit_record)
        self.delete_button.clicked.connect(self.delete_record)
        self.close_button.clicked.connect(self.close)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.close_button)

        layout.addLayout(button_layout)
        self.load_data()  # Load data for the initially selected table

    def load_data(self):
        """Load data from the selected table into the table widget."""
        selected_table = self.table_selector.currentText()
        try:
            data = self.controller.get_data(selected_table)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
            return

        self.table_widget.clear()
        if data:
            self.table_widget.setColumnCount(len(data[0]))
            self.table_widget.setRowCount(len(data))
            self.table_widget.setHorizontalHeaderLabels(data[0].keys())

            for row, record in enumerate(data):
                for col, value in enumerate(record.values()):
                    self.table_widget.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def delete_record(self):
        """Delete the selected record from the table."""
        selected_row = self.table_widget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Delete Record", "Please select a record to delete.")
            return

        selected_table = self.table_selector.currentText()
        record_id = self.table_widget.item(selected_row, 0).text()  # Assuming the first column is the ID
        try:
            self.controller.delete_record(selected_table, record_id)
            self.load_data()
            QtWidgets.QMessageBox.information(self, "Success", "Record deleted successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to delete record: {e}")

    def add_record(self):
        """Open a dialog to add a new record to the selected table."""
        selected_table = self.table_selector.currentText()
        dialog = RecordDialog(selected_table, parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            new_record_data = dialog.get_data()
            try:
                # Remove 'account_id' if present in the data for Accounts table
                if selected_table == "Accounts" and "account_id" in new_record_data:
                    del new_record_data["account_id"]
                self.controller.insert_record(selected_table, new_record_data)
                self.load_data()  # Reload data to reflect changes
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", f"Failed to add record: {e}")

    def get_primary_key_column(self, table_name):
        """Return the primary key column name for the given table."""
        primary_keys = {
            "Accounts": "account_id",
            "Vendor": "vendor_id",
            "Manufacturer": "manufacturer_id",
            "Brand": "brand_id",
            "Customer": "customer_id",
            "Categories": "product_category_id"
        }
        return primary_keys.get(table_name, "id")  # Default to 'id' if not found

    def edit_record(self):
        """Edit the selected record in the table."""
        selected_row = self.table_widget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Edit Record", "Please select a record to edit.")
            return
        
        selected_table = self.table_selector.currentText()
        current_record_data = {self.table_widget.horizontalHeaderItem(col).text(): self.table_widget.item(selected_row, col).text() for col in range(self.table_widget.columnCount())}
        
        dialog = RecordDialog(selected_table, current_record_data, self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            updated_record_data = dialog.get_data()
            try:
                # Use the correct primary key column for the update
                primary_key_column = self.get_primary_key_column(selected_table)
                self.controller.update_record(selected_table, current_record_data[primary_key_column], updated_record_data)
                self.load_data()  # Reload data to reflect changes
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", f"Failed to update record: {e}")