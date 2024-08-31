# src/user_interface/purchases/dialogs/purchase_order_additional_info.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import CURRENCIES, PURCHASE_STATUSES
from configs.ui_config import Units, FormFieldSizes, Placeholders

class PurchaseOrderAdditionalInfo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        logger.info("Initialized PurchaseOrderAdditionalInfo")

    @ErrorManager.handle_errors()
    def setup_ui(self):
        """Set up the UI components for additional purchase order information."""
        layout = QtWidgets.QFormLayout(self)
        self.vendor_order_number_field = QtWidgets.QLineEdit(self)
        self.vendor_order_number_field.setPlaceholderText(Placeholders.VENDOR_ORDER_NUMBER)
        self.currency_combo = QtWidgets.QComboBox(self)
        self.currency_combo.addItems(Units.CURRENCIES)
        self.status_combo = QtWidgets.QComboBox(self)
        self.status_combo.addItems(Units.PURCHASE_STATUSES)
        self.payment_method_field = QtWidgets.QLineEdit(self)
        self.payment_method_field.setPlaceholderText(Placeholders.PAYMENT_METHOD)

        for widget in [self.vendor_order_number_field, self.currency_combo, self.status_combo, self.payment_method_field]:
            widget.setFixedWidth(FormFieldSizes.MEDIUM)

        layout.addRow("Vendor Order Number:", self.vendor_order_number_field)
        layout.addRow("Currency:", self.currency_combo)
        layout.addRow("Status:", self.status_combo)
        layout.addRow("Payment Method:", self.payment_method_field)
        logger.debug("Set up UI for PurchaseOrderAdditionalInfo")

    @ErrorManager.handle_errors()
    def populate_fields(self, record_data):
        """Populate fields with existing record data."""
        self.vendor_order_number_field.setText(record_data.get('vendor_order_number', ''))
        self.currency_combo.setCurrentText(record_data.get('currency', CURRENCIES[0]))
        self.status_combo.setCurrentText(record_data.get('purchase_status', PURCHASE_STATUSES[0]))
        self.payment_method_field.setText(record_data.get('payment_method', ''))
        logger.debug("Populated fields in PurchaseOrderAdditionalInfo")

    @ErrorManager.handle_errors()
    def get_data(self):
        """Retrieve data from input fields."""
        return {
            'vendor_order_number': self.vendor_order_number_field.text(),
            'currency': self.currency_combo.currentText(),
            'purchase_status': self.status_combo.currentText(),
            'payment_method': self.payment_method_field.text()
        }