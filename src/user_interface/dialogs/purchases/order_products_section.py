# src/user_interface/dialogs/purchase_ui/order_products_section.py
from PyQt6 import QtWidgets

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