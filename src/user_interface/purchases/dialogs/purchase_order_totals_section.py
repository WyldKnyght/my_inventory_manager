# src/user_interface/purchases/dialogs/purchase_order_totals_section.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import Titles, FormFieldSizes

class PurchaseOrderTotalsSection(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__(Titles.GroupBoxes.ORDER_TOTALS, parent)
        self.setup_ui()
        logger.info("Initialized PurchaseOrderTotalsSection")

    @ErrorManager.handle_errors()
    def setup_ui(self):
        """Set up the UI components for the purchase order totals section."""
        layout = QtWidgets.QFormLayout(self)

        self.subtotal_edit = QtWidgets.QLineEdit(self)
        self.discount_edit = QtWidgets.QLineEdit(self)
        self.shipping_edit = QtWidgets.QLineEdit(self)
        self.taxes_edit = QtWidgets.QLineEdit(self)
        self.total_edit = QtWidgets.QLineEdit(self)
        self.custom_fees_edit = QtWidgets.QLineEdit(self)

        self.subtotal_edit.setReadOnly(True)
        self.total_edit.setReadOnly(True)

        for widget in [self.subtotal_edit, self.discount_edit, self.shipping_edit, 
                        self.taxes_edit, self.total_edit, self.custom_fees_edit]:
            widget.setFixedWidth(FormFieldSizes.MEDIUM)

        layout.addRow("Subtotal:", self.subtotal_edit)
        layout.addRow("Discount:", self.discount_edit)
        layout.addRow("Shipping:", self.shipping_edit)
        layout.addRow("Taxes:", self.taxes_edit)
        layout.addRow("Total:", self.total_edit)
        layout.addRow("Custom Fees:", self.custom_fees_edit)
        logger.debug("Set up UI for PurchaseOrderTotalsSection")


    @ErrorManager.handle_errors()
    def populate_fields(self, data: dict):
        """Populate fields with existing record data."""
        self.subtotal_edit.setText(str(data.get('subtotal', '')))
        self.discount_edit.setText(str(data.get('discount', '')))
        self.shipping_edit.setText(str(data.get('shipping', '')))
        self.taxes_edit.setText(str(data.get('taxes', '')))
        self.total_edit.setText(str(data.get('total', '')))
        self.custom_fees_edit.setText(str(data.get('custom_fees', '')))
        logger.debug("Populated fields in PurchaseOrderTotalsSection")

    @ErrorManager.handle_errors()
    def get_data(self) -> dict:
        """Retrieve data from input fields."""
        return {
            'subtotal': self.subtotal_edit.text(),
            'discount': self.discount_edit.text(),
            'shipping': self.shipping_edit.text(),
            'taxes': self.taxes_edit.text(),
            'total': self.total_edit.text(),
            'custom_fees': self.custom_fees_edit.text(),
        }

    @ErrorManager.handle_errors()
    def calculate_total(self):
        """TODO: Update Place holder calculation."""
        subtotal = self.subtotal_edit.text()
        discount = self.discount_edit.text()
        shipping = self.shipping_edit.text()
        taxes = self.taxes_edit.text()
        custom_fees = self.custom_fees_edit.text()

        total = float(subtotal) - float(discount) + float(shipping) + float(taxes) + float(custom_fees)
        self.total_edit.setText(str(total))
        logger.debug("Total calculation performed")
