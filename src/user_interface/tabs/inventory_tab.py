from PyQt6 import QtWidgets
from user_interface.base_widget import BaseWidget
from controllers.product_controller import ProductController

class InventoryTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.product_controller = ProductController()  # Initialize the controller
        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        """Set up the UI components for the Inventory tab."""
        main_layout = self.create_vertical_layout()
        self.setLayout(main_layout)

        # Table to display inventory products
        self.products_table = QtWidgets.QTableWidget(self)
        self.products_table.setColumnCount(7)
        self.products_table.setHorizontalHeaderLabels([
            'Product Number', 'Product Name', 'Type', 'Description', 
            'Actual Cost', 'Selling Price', 'Stock'
        ])
        main_layout.addWidget(self.products_table)

        # Enable sorting
        self.products_table.setSortingEnabled(True)
        
    def load_products(self):
        """Load products from the database and display them in the table."""
        try:
            products = self.product_controller.get_all_products()
            self.products_table.setRowCount(len(products))
            for row, product in enumerate(products):
                self.populate_table_row(row, product)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load products: {e}")

    def populate_table_row(self, row, product):
        """Populate a table row with product data."""
        self.products_table.setItem(row, 0, QtWidgets.QTableWidgetItem(product['product_number']))
        self.products_table.setItem(row, 1, QtWidgets.QTableWidgetItem(product['product_name']))
        self.products_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(product['product_category_id'])))  # Display category ID
        self.products_table.setItem(row, 3, QtWidgets.QTableWidgetItem(product['product_description']))
        self.products_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(product['actual_cost'])))
        self.products_table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(product['selling_price'])))
        self.products_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(product['quantity'])))