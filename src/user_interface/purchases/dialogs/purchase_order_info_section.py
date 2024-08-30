# src/user_interface/purchases/dialogs/purchase_order_info_section.py
from PyQt6 import QtWidgets, QtCore
from controllers.inventory_controller import InventoryController
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import Titles, FormFieldSizes, Placeholders

class PurchaseOrderInfoSection(QtWidgets.QGroupBox):
    def __init__(self, inventory_controller: InventoryController, parent=None):
        super().__init__(Titles.GroupBoxes.PURCHASE_ORDER_INFO, parent)
        self.inventory_controller = inventory_controller
        self.setup_ui()
        logger.info("Initialized PurchaseOrderInfoSection")

    @ErrorHandler.handle_errors()
    def setup_ui(self):
        """Set up the UI components for the purchase order info section."""
        layout = QtWidgets.QFormLayout(self)

        self.vendor_combo = QtWidgets.QComboBox(self)
        self.date_edit = QtWidgets.QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedHeight(FormFieldSizes.HEIGHT)
        self.order_number_edit = QtWidgets.QLineEdit(self)
        self.order_number_edit.setPlaceholderText(Placeholders.ORDER_NUMBER)
        self.po_number_edit = QtWidgets.QLineEdit(self)
        self.po_number_edit.setPlaceholderText(Placeholders.PO_NUMBER)

        for widget in [self.vendor_combo, self.date_edit, self.order_number_edit, self.po_number_edit]:
            widget.setFixedWidth(FormFieldSizes.MEDIUM)

        layout.addRow("Vendor:", self.vendor_combo)
        layout.addRow("Date:", self.date_edit)
        layout.addRow("Order Number:", self.order_number_edit)
        layout.addRow("PO Number:", self.po_number_edit)

        self.populate_vendor_combo()
        logger.debug("Set up UI for PurchaseOrderInfoSection")

    @ErrorHandler.handle_errors()
    def populate_vendor_combo(self):
        """Populate the vendor combo box with data from the inventory controller."""
        vendors = self.inventory_controller.get_vendors()
        self.vendor_combo.addItems(vendors)
        logger.debug(f"Populated vendor combo box with {len(vendors)} vendors")

    @ErrorHandler.handle_errors()
    def populate_fields(self, data: dict):
        """Populate fields with existing record data."""
        self.vendor_combo.setCurrentText(data.get('vendor', ''))
        self.date_edit.setDate(QtCore.QDate.fromString(data.get('date', ''), QtCore.Qt.DateFormat.ISODate))
        self.order_number_edit.setText(data.get('order_number', ''))
        self.po_number_edit.setText(data.get('po_number', ''))
        logger.debug("Populated fields in PurchaseOrderInfoSection")

    @ErrorHandler.handle_errors()
    def get_data(self) -> dict:
        """Retrieve data from input fields."""
        return {
            'vendor': self.vendor_combo.currentText(),
            'date': self.date_edit.date().toString(QtCore.Qt.DateFormat.ISODate),
            'order_number': self.order_number_edit.text(),
            'po_number': self.po_number_edit.text(),
        }