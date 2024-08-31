# src/user_interface/purchases/dialogs/purchase_order_dialog.py
from PyQt6 import QtWidgets
from typing import Optional, Dict, Any
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from controllers.purchases_controller import PurchasesController
from controllers.inventory_controller import InventoryController
from user_interface.common.error_warning_dialog import show_error_message, show_info_message
from user_interface.common.button_utils import add_action_buttons
from .purchase_order_info_section import PurchaseOrderInfoSection
from .purchase_order_items_section import PurchaseOrderItemsSection
from .purchase_order_totals_section import PurchaseOrderTotalsSection
from configs.ui_config import UIConfig, Titles, MessageBoxTitles, Buttons, REQUIRED_FIELDS

class PurchaseOrderDialog(QtWidgets.QDialog):
    def __init__(self, record_data: Optional[Dict[str, Any]] = None, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(parent)
        self.setWindowTitle(Titles.PURCHASE_ORDER_DIALOG)
        self.resize(*UIConfig.DIALOG_SIZE)
        self.record_data = record_data
        self.purchases_controller = PurchasesController()
        self.inventory_controller = InventoryController()
        self.setup_ui()
        logger.info("Initialized PurchaseOrderDialog")

    @ErrorManager.handle_errors()
    def setup_ui(self):
        """Set up the UI components for the purchase order dialog."""
        main_layout = QtWidgets.QVBoxLayout(self)
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        content_widget = QtWidgets.QWidget()
        scroll_area.setWidget(content_widget)
        content_layout = QtWidgets.QVBoxLayout(content_widget)

        self.info_section = PurchaseOrderInfoSection(self.inventory_controller, self)
        content_layout.addWidget(self.info_section)

        self.items_section = PurchaseOrderItemsSection(self.inventory_controller, self)
        content_layout.addWidget(self.items_section)

        split_widget = QtWidgets.QWidget()
        split_layout = QtWidgets.QHBoxLayout(split_widget)
        left_widget = QtWidgets.QWidget()
        split_layout.addWidget(left_widget)
        self.totals_section = PurchaseOrderTotalsSection(self)
        split_layout.addWidget(self.totals_section)

        content_layout.addWidget(split_widget)
        content_layout.addStretch()

        actions = [(Buttons.SAVE, self.accept), (Buttons.CANCEL, self.reject)]
        button_layout = add_action_buttons(self, actions)
        main_layout.addLayout(button_layout)

        if self.record_data:
            self.populate_fields()
        logger.debug("Set up UI for PurchaseOrderDialog")

    @ErrorManager.handle_errors()
    def populate_fields(self):
        """Populate fields with existing record data."""
        self.info_section.populate_fields(self.record_data)
        self.items_section.populate_items(self.record_data.get('items', []))
        self.totals_section.populate_fields(self.record_data)
        logger.debug("Populated fields in PurchaseOrderDialog")

    @ErrorManager.handle_errors()
    def get_data(self) -> Optional[Dict[str, Any]]:
        """Retrieve data from all sections of the dialog."""
        return {
            'purchase_id': self.record_data.get('purchase_id') if self.record_data else None,
            'status': 'Pending',  # Default status
            **self.info_section.get_data(),
            'items': self.items_section.get_data(),
            **self.totals_section.get_data(),
        }

    @ErrorManager.handle_errors()
    def validate_data(self, data: Dict[str, Any]) -> bool:
        """Validate the input data."""
        return all(data.get(field) for field in REQUIRED_FIELDS)

    @ErrorManager.handle_errors()
    def accept(self):
        """Handle the accept action of the dialog."""
        data = self.get_data()
        if data is None or not self.validate_data(data):
            show_error_message(self, MessageBoxTitles.ERROR, "Please check your input and try again.")
            return
        
        try:
            if self.record_data:
                self.purchases_controller.update_purchase(data)
                show_info_message(self, MessageBoxTitles.SUCCESS, "Purchase order updated successfully")
            else:
                self.purchases_controller.add_purchase(data)
                show_info_message(self, MessageBoxTitles.SUCCESS, "Purchase order added successfully")
            super().accept()
            logger.info("Purchase order saved successfully")
        except Exception as e:
            logger.error(f"Failed to save purchase order: {str(e)}")
            show_error_message(self, MessageBoxTitles.ERROR, f"Failed to save purchase order: {str(e)}")