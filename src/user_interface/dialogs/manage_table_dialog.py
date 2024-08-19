from PyQt6 import QtWidgets
from controllers.manage_table_controller import ManageTableController
from user_interface.dialogs.record_dialog import RecordDialog
from utils.ui_helpers import create_button

import logging

logger = logging.getLogger(__name__)

class ManageTableDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, table_names=None, default_table=None, controller=None):
        super().__init__(parent)
        self.table_names = table_names or []
        self.default_table = default_table
        self.controller = controller or ManageTableController()
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.create_table_selector(layout)
        self.create_buttons(layout)
        if self.default_table:
            self.table_selector.setCurrentText(self.default_table)
        self.load_data()

    def create_table_selector(self, layout):
        self.table_selector = QtWidgets.QComboBox(self)
        self.table_selector.addItems(self.table_names)
        self.table_selector.currentIndexChanged.connect(self.load_data)
        layout.addWidget(self.table_selector)

        self.table_widget = QtWidgets.QTableWidget(self)
        layout.addWidget(self.table_widget)

    def create_buttons(self, layout):
        button_layout = QtWidgets.QHBoxLayout()
        buttons = {
            "Add": self.add_record,
            "Edit": self.edit_record,
            "Delete": self.delete_record,
            "Close": self.close
        }
        for label, callback in buttons.items():
            button = create_button(self, label, callback)
            button_layout.addWidget(button)
        layout.addLayout(button_layout)

    def load_data(self):
        selected_table = self.table_selector.currentText()
        try:
            data = self.controller.get_table_data(selected_table)
            self.controller.update_table_widget(self.table_widget, data)
        except Exception as e:
            logger.error(f"Failed to load data for table {selected_table}: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load data: {e}")

    def handle_record(self, action, dialog_class=None):
        selected_table = self.table_selector.currentText()
        selected_row = self.table_widget.currentRow()
        if action in ["edit", "delete"] and selected_row == -1:
            QtWidgets.QMessageBox.warning(self, f"{action.capitalize()} Record", f"Please select a record to {action}.")
            return
        try:
            current_data = self.get_selected_record_data(selected_row) if action in ["edit", "delete"] else None
            if action == "add":
                dialog = dialog_class(selected_table, parent=self)
            else:
                dialog = dialog_class(selected_table, current_data, parent=self)
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                getattr(self.controller, f"handle_{action}_record")(dialog, selected_table, current_data)
                self.load_data()
        except Exception as e:
            logger.error(f"Failed to {action} record in table {selected_table}: {e}")

    def add_record(self):
        self.handle_record("add", RecordDialog)

    def edit_record(self):
        self.handle_record("edit", RecordDialog)

    def delete_record(self):
        self.handle_record("delete")

    def get_selected_record_data(self, row):
        data = {}
        if row >= 0:
            for col in range(self.table_widget.columnCount()):
                header = self.table_widget.horizontalHeaderItem(col).text()
                item = self.table_widget.item(row, col)
                data[header] = item.text() if item else ''
        return data
