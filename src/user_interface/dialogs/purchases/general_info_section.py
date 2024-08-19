from PyQt6 import QtWidgets, QtCore
from controllers.vendor_controller import get_all_vendors

class GeneralInfoSection(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__("General Information", parent)
        self.setup_ui()

    def setup_ui(self):
        self.general_layout = QtWidgets.QFormLayout(self)

        self.vendor_combo_box = QtWidgets.QComboBox()
        self.populate_vendor_combo_box()
        self.add_row("Vendor Name:", self.vendor_combo_box)

        self.vendor_order_number_edit = QtWidgets.QLineEdit()
        self.add_row("Vendor Order Number:", self.vendor_order_number_edit)

        self.po_number_edit = QtWidgets.QLineEdit()
        self.add_row("PO Number:", self.po_number_edit)

        self.po_date_edit = QtWidgets.QDateEdit(calendarPopup=True)
        self.po_date_edit.setDate(QtCore.QDate.currentDate())
        self.add_row("PO Date:", self.po_date_edit)

        self.po_status_combo = QtWidgets.QComboBox()
        self.po_status_combo.addItems(["Pending", "Shipped", "Delivered"])
        self.add_row("PO Status:", self.po_status_combo)

        self.payment_method_edit = QtWidgets.QLineEdit()
        self.add_row("Payment Method:", self.payment_method_edit)

        self.shipping_date_edit = QtWidgets.QDateEdit(calendarPopup=True)
        self.shipping_date_edit.setDate(QtCore.QDate.currentDate())
        self.add_row("Shipping Date:", self.shipping_date_edit)

        self.vendor_ref_number_edit = QtWidgets.QLineEdit()
        self.add_row("Vendor Reference Number:", self.vendor_ref_number_edit)

        self.vendor_instructions_edit = QtWidgets.QTextEdit()
        self.vendor_instructions_edit.setMaximumHeight(50)
        self.add_row("Vendor Instructions:", self.vendor_instructions_edit)

        self.reference_number_edit = QtWidgets.QLineEdit()
        self.add_row("Reference Number:", self.reference_number_edit)

        self.notes_edit = QtWidgets.QTextEdit()
        self.notes_edit.setMaximumHeight(50)
        self.add_row("Notes:", self.notes_edit)

    def add_row(self, label, widget):
        self.general_layout.addRow(label, widget)

    def populate_vendor_combo_box(self):
        try:
            vendors = get_all_vendors()
            vendor_names = [vendor['company_name'] for vendor in vendors]
            self.vendor_combo_box.addItems(vendor_names)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load vendors: {e}")
