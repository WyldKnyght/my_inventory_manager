# src/user_interface/dialogs/inventory_dialog.py

from PyQt6 import QtWidgets
from controllers.inventory.product_management_controller import ProductManagementController
from utils.ui_helpers import create_button

class InventoryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inventory Management")
        self.controller = ProductManagementController(self) 
        self.setup_ui()

    def setup_ui(self):
        grid_layout = QtWidgets.QGridLayout()
        self.setLayout(grid_layout)

        for i, (text, slot) in enumerate(self.get_buttons()):
            row, col = divmod(i, 2)  # 2 buttons per row
            button = create_button(self, text, slot)
            grid_layout.addWidget(button, row, col)

        grid_layout.setSpacing(10)
        grid_layout.setContentsMargins(10, 10, 10, 10)

    def get_buttons(self):
        """Return a list of button configurations for the inventory management."""
        return [
            ("Manage Products", self.controller.open_manage_products_dialog),
            ("Manage Categories", self.controller.open_manage_categories_dialog),
            ("Manage Brands", self.controller.open_manage_brands_dialog),
            ("Manage Companies", self.controller.open_manage_companies_dialog)
        ]
