from PyQt6 import QtWidgets, QtGui, QtCore

class ProductWidget(QtWidgets.QWidget):
    def __init__(self, product_name, quantity, price, parent=None):
        super().__init__(parent)
        self.setup_ui(product_name, quantity, price)

    def setup_ui(self, product_name, quantity, price):
        layout = QtWidgets.QHBoxLayout(self)

        name_label = QtWidgets.QLabel(product_name)
        quantity_label = QtWidgets.QLabel(f"Quantity: {quantity}")
        price_label = QtWidgets.QLabel(f"Price: ${price:.2f}")

        layout.addWidget(name_label)
        layout.addWidget(quantity_label)
        layout.addWidget(price_label)

        self.setLayout(layout)