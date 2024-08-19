from PyQt6 import QtWidgets

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
