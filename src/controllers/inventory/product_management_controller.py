# src/controllers/product_management_controller.py

from user_interface.dialogs.manage_table_dialog import ManageTableDialog

class ProductManagementController:
    def __init__(self, parent=None):
        self.parent = parent

    def open_manage_dialog(self, default_table):
        dialog = ManageTableDialog(self.parent, default_table=default_table, table_names=self.get_inventory_tables())
        dialog.exec()

    def open_manage_products_dialog(self):
        self.open_manage_dialog("Products")

    def open_manage_categories_dialog(self):
        self.open_manage_dialog("Categories")

    def open_manage_brands_dialog(self):
        self.open_manage_dialog("Brand")

    def open_manage_companies_dialog(self):
        self.open_manage_dialog("Company")

    def get_inventory_tables(self):
        """Return a list of tables related to inventory."""
        return ["Products", "Categories", "Brand", "Company"]
