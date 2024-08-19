from PyQt6 import QtWidgets, QtGui, QtCore
from controllers.vendor_controller import get_all_vendors

class PurchaseOrderDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Purchase Order")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        scroll_area = QtWidgets.QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QtWidgets.QWidget()
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)

        self.add_title(scroll_layout)

        sections = [GeneralInfoSection(self), OrderProductsSection(self), FinancialSummarySection(self)]
        for section in sections:
            scroll_layout.addWidget(section)

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        self.add_button_box(main_layout)

    def add_title(self, layout):
        title_label = QtWidgets.QLabel("Purchase Order")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Weight.Bold))
        layout.addWidget(title_label)

    def add_button_box(self, layout):
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)


class GeneralInfoSection(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__("General Information", parent)
        self.setup_ui()

    def setup_ui(self):
        self.general_layout = QtWidgets.QFormLayout(self)

        self.vendor_combo_box = QtWidgets.QComboBox()
        self.populate_vendor_combo_box()
        self.add_row("Vendor Name:", self.vendor_combo_box)

        self.add_row("Vendor Order Number:", QtWidgets.QLineEdit())
        self.add_row("PO Number:", QtWidgets.QLineEdit())
        self.add_row("PO Date:", self.create_date_edit())
        self.add_row("PO Status:", self.create_status_combo())
        self.add_row("Payment Method:", QtWidgets.QLineEdit())
        self.add_row("Shipping Date:", self.create_date_edit())
        self.add_row("Vendor Reference Number:", QtWidgets.QLineEdit())
        self.add_row("Vendor Instructions:", self.create_text_edit())
        self.add_row("Reference Number:", QtWidgets.QLineEdit())
        self.add_row("Notes:", self.create_text_edit())

    def add_row(self, label, widget):
        self.general_layout.addRow(label, widget)

    def populate_vendor_combo_box(self):
        try:
            vendors = get_all_vendors()
            vendor_names = [vendor['company_name'] for vendor in vendors]
            self.vendor_combo_box.addItems(vendor_names)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load vendors: {e}")

    def create_date_edit(self):
        date_edit = QtWidgets.QDateEdit(calendarPopup=True)
        date_edit.setDate(QtCore.QDate.currentDate())
        return date_edit

    def create_status_combo(self):
        status_combo = QtWidgets.QComboBox()
        status_combo.addItems(["Pending", "Shipped", "Delivered"])
        return status_combo

    def create_text_edit(self):
        text_edit = QtWidgets.QTextEdit()
        text_edit.setMaximumHeight(50)
        return text_edit


class OrderProductsSection(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Order Products", parent)
        self.setup_ui()

    def setup_ui(self):
        order_products_layout = QtWidgets.QVBoxLayout(self)

        self.products_table = QtWidgets.QTableWidget()
        self.products_table.setColumnCount(10)
        self.products_table.setHorizontalHeaderLabels([
            'Item Number', 'Item Description', 'Quantity Ordered', 'Unit Price (CAD)', 
            'Total Price (CAD)', 'Discounts', 'Tax', 'SKU/Part Number', 'UOM', 'Currency'
        ])
        self.products_table.setRowCount(1)  # Placeholder row
        order_products_layout.addWidget(self.products_table)


class FinancialSummarySection(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Financial Summary", parent)
        self.setup_ui()

    def setup_ui(self):
        financial_layout = QtWidgets.QFormLayout(self)

        self.purchase_amount_input = self.add_currency_input(financial_layout, "Purchase Amount:")
        self.taxes_input = self.add_currency_input(financial_layout, "Taxes:")
        self.discount_input = self.add_currency_input(financial_layout, "Discount:")
        self.customs_fees_input = self.add_currency_input(financial_layout, "Customs Fees:")
        self.shipping_cost_input = self.add_currency_input(financial_layout, "Shipping Costs:")

        self.grand_total_label = QtWidgets.QLabel("Grand Total: CAD 0.00")
        financial_layout.addRow("Grand Total:", self.grand_total_label)

    def add_currency_input(self, layout, label):
        input_widget = CurrencyInputWidget(self)
        layout.addRow(label, input_widget)
        return input_widget

    def get_financial_data(self):
        """Retrieve financial data from input fields."""
        return {
            "purchase_amount": self.purchase_amount_input.get_amount(),
            "purchase_currency": self.purchase_amount_input.get_currency(),
            "taxes": self.taxes_input.get_amount(),
            "taxes_currency": self.taxes_input.get_currency(),
            "discount": self.discount_input.get_amount(),
            "discount_currency": self.discount_input.get_currency(),
            "customs_fees": self.customs_fees_input.get_amount(),
            "customs_fees_currency": self.customs_fees_input.get_currency(),
            "shipping_cost": self.shipping_cost_input.get_amount(),
            "shipping_currency": self.shipping_cost_input.get_currency(),
        }

class CurrencyInputWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QHBoxLayout(self)

        self.amount_input = QtWidgets.QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.setMinimumWidth(100)

        self.currency_selector = QtWidgets.QComboBox(self)
        self.currency_selector.addItems(["USD", "CAD"])
        self.currency_selector.setMinimumWidth(60)

        layout.addWidget(self.amount_input)
        layout.addWidget(self.currency_selector)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

    def get_amount(self):
        """Return the amount entered as a float."""
        try:
            return float(self.amount_input.text())
        except ValueError:
            return None

    def get_currency(self):
        """Return the selected currency."""
        return self.currency_selector.currentText()

    def set_amount(self, amount):
        """Set the amount in the QLineEdit."""
        self.amount_input.setText(str(amount))

    def set_currency(self, currency):
        """Set the selected currency in the QComboBox."""
        index = self.currency_selector.findText(currency)
        if index != -1:
            self.currency_selector.setCurrentIndex(index)
