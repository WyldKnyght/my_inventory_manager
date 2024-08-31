# src/user_interface/inventory/inventory_record_dialog.py

from PyQt6 import QtWidgets
from user_interface.common.base_record_dialog import BaseRecordDialog
from user_interface.common.form_input_widgets import create_combobox
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.config_manager import config_manager
from controllers.inventory_controller import InventoryController
from configs.ui_config import Titles, Placeholders, FormFieldSizes, UIStrings

class InventoryRecordDialog(BaseRecordDialog):
    def __init__(self, table_name, record_data=None, columns=None, parent=None):
        self.inventory_controller = InventoryController()
        self.table_name = table_name
        self.columns = self.inventory_controller.get_filtered_columns(table_name, columns)
        title = config_manager.get(f'ui.dialog_titles.{table_name.lower()}', f"{table_name} Entry")
        title = f"Edit {title}" if record_data else f"New {title}"
        super().__init__(title, record_data, parent)
        logger.info(f"Initialized InventoryRecordDialog for {table_name}")

    @ErrorManager.handle_errors()
    def add_fields(self, layout):
        """Add input fields for each column."""
        for column in self.columns:
            self._add_field_for_column(layout, column)
        logger.debug(f"Added fields for {self.table_name}")

    def _add_field_for_column(self, layout, column):
        field = self._create_field(column)
        self.fields[column] = field
        if isinstance(field, QtWidgets.QLineEdit):
            field.setFixedWidth(FormFieldSizes.MEDIUM)
            field.setPlaceholderText(Placeholders.SEARCH)
        label = self._get_label_for_column(column)
        layout.addRow(label, field)

    def _create_field(self, column):
        if self.table_name == UIStrings.CATALOG:
            if column == UIStrings.CATEGORY_ID:
                return create_combobox(
                    self, 
                    [], 
                    data_callback=self.inventory_controller.get_category_names
                )
            elif column == UIStrings.UNIT_TYPE_ID:
                return create_combobox(
                    self, 
                    [], 
                    data_callback=self.inventory_controller.get_unit_types
                )
        return QtWidgets.QLineEdit(self)

    def _get_label_for_column(self, column):
        if self.table_name == UIStrings.CATEGORIES and column == UIStrings.CATEGORY_NAME:
            return Titles.GroupBoxes.CATALOG
        elif self.table_name == UIStrings.UNIT_TYPES and column == UIStrings.UNIT_TYPE:
            return UIStrings.UNIT_TYPE_LABEL
        else:
            return f"{column.replace('_', ' ').title()}:"

    @ErrorManager.handle_errors()
    def populate_fields(self):
        """Populate fields with existing record data."""
        super().populate_fields()
        logger.debug(f"Populated fields for {self.table_name}")

    @ErrorManager.handle_errors()
    def accept(self):
        """Override accept to include validation."""
        try:
            self.inventory_controller.validate_inventory_input(self.table_name, self.get_field_values())
            super().accept()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Validation Error", str(e))

    def get_field_values(self):
        """Get the values of all fields."""
        return {column: field.text() if isinstance(field, QtWidgets.QLineEdit) else field.currentText() 
                for column, field in self.fields.items()}