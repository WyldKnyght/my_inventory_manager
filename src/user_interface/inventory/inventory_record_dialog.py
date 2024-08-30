# src/user_interface/inventory/inventory_record_dialog.py

from PyQt6 import QtWidgets
from user_interface.common.base_record_dialog import BaseRecordDialog
from user_interface.common.form_input_widgets import create_combobox
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.database_config import get_id_columns
from controllers.inventory_controller import InventoryController
from configs.ui_config import Titles, Placeholders, FormFieldSizes

class InventoryRecordDialog(BaseRecordDialog):
    def __init__(self, table_name, record_data=None, columns=None, parent=None):
        self.inventory_controller = InventoryController()
        self.table_name = table_name
        self.columns = self.filter_columns(columns or [])
        title = f"{table_name} Entry"
        title = f"Edit {title}" if record_data else f"New {title}"
        super().__init__(title, record_data, parent)
        logger.info(f"Initialized InventoryRecordDialog for {table_name}")

    @ErrorHandler.handle_errors()
    def filter_columns(self, columns):
        """Filter out autoincrement ID columns."""
        id_columns = get_id_columns()
        filtered_columns = [col for col in columns if col != id_columns.get(self.table_name)]
        logger.debug(f"Filtered columns for {self.table_name}: {filtered_columns}")
        return filtered_columns

    @ErrorHandler.handle_errors()
    def add_fields(self, layout):
        """Add input fields for each column."""
        for column in self.columns:
            self._add_field_for_column(layout, column)
        logger.debug(f"Added fields for {self.table_name}")

    def _add_field_for_column(self, layout, column):
        if self.table_name == "Categories" and column == "category_name":
            self._add_line_edit(layout, column, Titles.GroupBoxes.CATALOG)
        elif self.table_name == "UnitTypes" and column == "unit_type":
            self._add_line_edit(layout, column, "Unit Type:")
        elif self.table_name == "Catalog":
            self._add_catalog_field(layout, column)
        else:
            self._add_line_edit(layout, column)

    def _add_line_edit(self, layout, column, label=None):
        self.fields[column] = QtWidgets.QLineEdit(self)
        self.fields[column].setFixedWidth(FormFieldSizes.MEDIUM)
        self.fields[column].setPlaceholderText(Placeholders.SEARCH)
        layout.addRow(label or f"{column.replace('_', ' ').title()}:", self.fields[column])

    def _add_catalog_field(self, layout, column):
        if column == "category_id":
            self.fields[column] = create_combobox(
                self, 
                [], 
                data_callback=lambda: self.inventory_controller.get_category_names()
            )
            layout.addRow(Titles.GroupBoxes.CATALOG, self.fields[column])
        elif column == "unit_type_id":
            self.fields[column] = create_combobox(
                self, 
                [], 
                data_callback=lambda: self.inventory_controller.get_unit_types()
            )
            layout.addRow("Unit Type:", self.fields[column])

    @ErrorHandler.handle_errors()
    def populate_fields(self):
        """Populate fields with existing record data."""
        super().populate_fields()
        logger.debug(f"Populated fields for {self.table_name}")

    @ErrorHandler.handle_errors()
    def add_buttons(self, layout):
        """Add Save and Exit buttons."""
        super().add_buttons(layout)
        logger.debug("Added buttons to InventoryRecordDialog")