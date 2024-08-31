# src/user_interface/purchases/purchases_actions.py
from PyQt6 import QtWidgets
from user_interface.purchases.dialogs.purchase_order_dialog import PurchaseOrderDialog
from user_interface.common.error_warning_dialog import show_error_message, show_warning_message, show_info_message
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import Buttons, MessageBoxTitles, Titles

class PurchasesActions:
    def __init__(self, parent, purchases_table, purchases_controller):
        self.parent = parent
        self.purchases_table = purchases_table
        self.purchases_controller = purchases_controller
        logger.info("Initialized PurchasesActions")

    @ErrorManager.handle_errors()
    def create_action_buttons(self):
        button_layout = self.parent.create_horizontal_layout()
        actions = [
            (Buttons.ADD, self.add_purchase),
            (Buttons.EDIT, self.edit_purchase),
            (Buttons.DELETE, self.delete_purchase),
            (Buttons.REFRESH, self.refresh_table)
        ]
        for text, action in actions:
            button = self.parent.create_button(text, action)
            button.setToolTip(f"{text} a purchase order")
            button_layout.addWidget(button)
        logger.debug("Created action buttons for purchases")
        return button_layout

    @ErrorManager.handle_errors()
    def add_purchase(self):
        dialog = PurchaseOrderDialog(parent=self.parent)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            purchase_data = dialog.get_data()
            try:
                self.purchases_controller.add_purchase(purchase_data)
                self.refresh_table()
                show_info_message(self.parent, MessageBoxTitles.SUCCESS, "Purchase added successfully")
                logger.info("New purchase added successfully")
            except Exception as e:
                error_msg = f"Failed to add purchase: {str(e)}"
                show_error_message(self.parent, MessageBoxTitles.ERROR, error_msg)
                logger.error(error_msg)

    @ErrorManager.handle_errors()
    def edit_purchase(self):
        purchase_id = self.purchases_table.get_selected_purchase_id()
        if not purchase_id:
            show_warning_message(self.parent, Titles.EDIT_RECORD, "Please select a purchase to edit.")
            return

        try:
            purchase_data = self.purchases_controller.get_purchase_by_id(purchase_id)
            dialog = PurchaseOrderDialog(record_data=purchase_data, parent=self.parent)
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                updated_data = dialog.get_data()
                self.purchases_controller.update_purchase(updated_data)
                self.refresh_table()
                show_info_message(self.parent, MessageBoxTitles.SUCCESS, "Purchase updated successfully")
                logger.info(f"Purchase {purchase_id} updated successfully")
        except Exception as e:
            error_msg = f"Failed to edit purchase: {str(e)}"
            show_error_message(self.parent, MessageBoxTitles.ERROR, error_msg)
            logger.error(error_msg)

    @ErrorManager.handle_errors()
    def delete_purchase(self):
        purchase_id = self.purchases_table.get_selected_purchase_id()
        if not purchase_id:
            show_warning_message(self.parent, Titles.DELETE_RECORD, "Please select a purchase to delete.")
            return

        confirm = QtWidgets.QMessageBox.question(
            self.parent,
            Titles.CONFIRM_DELETION,
            f"Are you sure you want to delete the purchase order {purchase_id}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            try:
                self.purchases_controller.delete_purchase(purchase_id)
                self.refresh_table()
                show_info_message(self.parent, MessageBoxTitles.SUCCESS, "Purchase deleted successfully")
                logger.info(f"Purchase {purchase_id} deleted successfully")
            except Exception as e:
                error_msg = f"Failed to delete purchase: {str(e)}"
                show_error_message(self.parent, MessageBoxTitles.ERROR, error_msg)
                logger.error(error_msg)

    @ErrorManager.handle_errors()
    def refresh_table(self):
        self.purchases_table.load_purchases_data(self.purchases_controller, self.parent.status_bar)
        self.purchases_table.filter_purchases(self.parent.search_bar.text())
        logger.debug("Refreshed purchases table")