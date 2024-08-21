# src/user_interface/dialogs/record_dialog/inventory_record_dialog.py

from PyQt6 import QtWidgets, QtGui
from .base_record_dialog import BaseRecordDialog
from utils.field_helpers import create_combobox

class InventoryRecordDialog(BaseRecordDialog):
    def __init__(self, table_name, record_data=None, columns=None, parent=None):
        self.table_name = table_name
        self.columns = self.filter_columns(columns or [])
        super().__init__(f"{table_name} Entry", record_data, parent)

    def filter_columns(self, columns):
        """Filter out autoincrement ID columns."""
        id_columns = {
            "Categories": "category_id",
            "UnitTypes": "unit_type_id",
            "Catalog": "item_id",
            # Add other tables and their ID columns here
        }
        return [col for col in columns if col != id_columns.get(self.table_name)]

    def add_fields(self, layout):
        """Add input fields for each column."""
        for column in self.columns:
            if self.table_name == "Categories" and column == "category_name":
                self.fields[column] = QtWidgets.QLineEdit(self)
                layout.addRow("Category Name:", self.fields[column])
            elif self.table_name == "UnitTypes" and column == "unit_type":
                self.fields[column] = QtWidgets.QLineEdit(self)
                layout.addRow("Unit Type:", self.fields[column])
            elif self.table_name == "Catalog":
                if column == "category_id":
                    self.fields[column] = create_combobox(self, "category_name", "Categories")
                    layout.addRow("Category:", self.fields[column])
                elif column == "unit_type_id":
                    self.fields[column] = create_combobox(self, "unit_type", "UnitTypes")
                    layout.addRow("Unit Type:", self.fields[column])
                elif column in ["product_height", "product_width", "product_length", "product_size",
                                "product_weight", "cost_price", "selling_price", "quantity"]:
                    line_edit = QtWidgets.QLineEdit(self)
                    line_edit.setValidator(QtGui.QDoubleValidator(0.0, 10000.0, 2))
                    self.fields[column] = line_edit
                    layout.addRow(f"{column.replace('_', ' ').title()}:", line_edit)
                elif column == "discontinued":
                    self.fields[column] = QtWidgets.QCheckBox(self)
                    layout.addRow("Discontinued:", self.fields[column])
                else:
                    self.fields[column] = QtWidgets.QLineEdit(self)
                    layout.addRow(f"{column.replace('_', ' ').title()}:", self.fields[column])
            else:
                # Default to a simple line edit for other fields
                self.fields[column] = QtWidgets.QLineEdit(self)
                layout.addRow(f"{column.replace('_', ' ').title()}:", self.fields[column])

    def populate_fields(self):
        """Populate fields with existing record data."""
        for key, value in self.record_data.items():
            if key in self.fields:
                widget = self.fields[key]
                if isinstance(widget, QtWidgets.QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QtWidgets.QComboBox):
                    index = widget.findData(value)
                    widget.setCurrentIndex(index)
                elif isinstance(widget, QtWidgets.QCheckBox):
                    widget.setChecked(value.lower() == 'yes')

    
    def add_buttons(self, layout):
        """Add Save and Exit buttons."""
        button_layout = QtWidgets.QHBoxLayout()
        save_button = QtWidgets.QPushButton("Save", self)
        save_button.clicked.connect(self.accept)
        exit_button = QtWidgets.QPushButton("Exit", self)
        exit_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(exit_button)
        layout.addRow(button_layout)