import PyQt6.QtWidgets as QtWidgets
from user_interface.dialogs.add_product_dialog import AddProductDialog

''' TODO: Move to Settings Tab, Edit Inventory
    # Buttons for actions
    button_layout = self.create_horizontal_layout()
    add_button = self.create_button("Add product", self.add_product)
    edit_button = self.create_button("Edit product", self.edit_product)
    delete_button = self.create_button("Delete product", self.delete_product)
    button_layout.addWidget(add_button)
    button_layout.addWidget(edit_button)
    button_layout.addWidget(delete_button)
    main_layout.addLayout(button_layout)
'''

def add_product(self):
    """Open a dialog to add a new product."""
    dialog = AddProductDialog(self)
    if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        self.load_products()  # Reload products to reflect the new addition

def edit_product(self):
    """Edit the selected product."""
    selected_row = self.products_table.currentRow()
    if selected_row == -1:
        QtWidgets.QMessageBox.warning(self, "Edit product", "Please select an product to edit.")
        return
    # Logic to edit the selected product
    print("Edit product functionality")

def delete_product(self):
    """Delete the selected product."""
    selected_row = self.products_table.currentRow()
    if selected_row == -1:
        QtWidgets.QMessageBox.warning(self, "Delete product", "Please select an product to delete.")
        return
    product_id = self.products_table.product(selected_row, 0).text()
    self.product_controller.delete_product(product_id)
    self.load_products()  # Reload products to reflect the deletion