from PyQt6 import QtWidgets

class ProductView(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.product_label = QtWidgets.QLabel("Item Details")
        layout.addWidget(self.product_label)

    def display_product(self, product):
        self.product_label.setText(f"Name: {product.name}, Quantity: {product.quantity}")