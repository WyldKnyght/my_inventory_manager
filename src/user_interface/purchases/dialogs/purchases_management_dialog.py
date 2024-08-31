# src/user_interface/purchases/dialogs/purchases_management_dialog.py
from PyQt6 import QtWidgets
from user_interface.common.generic_management_dialog import GenericManagementDialog
from .purchase_order_dialog import PurchaseOrderDialog
from user_interface.common.error_warning_dialog import show_warning_message, show_error_message
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import Titles, MessageBoxTitles

class PurchasesManagementDialog(GenericManagementDialog):
    def __init__(self, purchases_controller, parent=None):
        super().__init__(Titles.PURCHASES_MANAGEMENT, parent)
        self.purchases_controller = purchases_controller
        self.load_data()
        logger.info("Initialized PurchasesManagementDialog")

    @ErrorManager.handle_errors()
    def load_data(self):
        """Load and display all purchases."""
        try:
            purchases = self.purchases_controller.get_all_purchases()
            self.populate_table(purchases)
            logger.debug(f"Loaded {len(purchases)} purchases")
        except Exception as e:
            error_msg = f"Failed to load purchases: {str(e)}"
            logger.error(error_msg)
            show_error_message(self, MessageBoxTitles.ERROR, error_msg)

    @ErrorManager.handle_errors()
    def add_entry(self):
        """Add a new purchase entry."""
        dialog = PurchaseOrderDialog(parent=self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            purchase_data = dialog.get_data()
            try:
                self.purchases_controller.add_purchase(purchase_data)
                self.load_data()
                logger.info("New purchase added successfully")
            except Exception as e:
                error_msg = f"Failed to add purchase: {str(e)}"
                logger.error(error_msg)
                show_error_message(self, MessageBoxTitles.ERROR, error_msg)

    @ErrorManager.handle_errors()
    def edit_entry(self):
        """Edit an existing purchase entry."""
        selected_row = self.data_table.currentRow()
        if selected_row == -1:
            show_warning_message(self, Titles.EDIT_RECORD, "Please select a purchase to edit.")
            return

        po_number = self.data_table.item(selected_row, 0).text()
        try:
            current_data = self.purchases_controller.get_purchase_by_po_number(po_number)
            dialog = PurchaseOrderDialog(record_data=current_data, parent=self)
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                updated_data = dialog.get_data()
                self.purchases_controller.update_purchase(updated_data)
                self.load_data()
                logger.info(f"Purchase {po_number} updated successfully")
        except Exception as e:
            error_msg = f"Failed to edit purchase: {str(e)}"
            logger.error(error_msg)
            show_error_message(self, MessageBoxTitles.ERROR, error_msg)

    @ErrorManager.handle_errors()
    def delete_entry(self):
        """Delete an existing purchase entry."""
        selected_row = self.data_table.currentRow()
        if selected_row == -1:
            show_warning_message(self, Titles.DELETE_RECORD, "Please select a purchase to delete.")
            return

        po_number = self.data_table.item(selected_row, 0).text()
        confirm = QtWidgets.QMessageBox.question(
            self,
            Titles.CONFIRM_DELETION,
            f"Are you sure you want to delete the purchase order {po_number}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            try:
                self.purchases_controller.delete_purchase(po_number)
                self.load_data()
                logger.info(f"Purchase {po_number} deleted successfully")
            except Exception as e:
                error_msg = f"Failed to delete purchase: {str(e)}"
                logger.error(error_msg)
                show_error_message(self, MessageBoxTitles.ERROR, error_msg)