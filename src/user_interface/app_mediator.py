# app_mediator.py
from user_interface.inventory_ui.inventory_add_edit_window import open_add_edit_window
from logic.inventory.inventory_functions import add_product, update_product, confirm_delete, refresh_listbox
from user_interface.purchases_ui.purchase_add_edit_window import purchase_open_add_edit_window
from logic.purchases.purchases_functions import add_purchase, update_purchase, refresh_purchases_listbox
from database.purchases.db_purchases_crud import PurchasesCRUD

class AppMediator:
    def __init__(self):
        self.inventory = None
        self.sales = None
        self.purchases = None
        self.reports = None
        self.crud = PurchasesCRUD()  # Initialize the CRUD object

    def set_inventory(self, inventory):
        self.inventory = inventory

    def set_sales(self, sales):
        self.sales = sales

    def set_purchases(self, purchases):
        self.purchases = purchases

    def set_reports(self, reports):
        self.reports = reports

    def add_product(self, entries, listbox):
        add_product(entries, listbox)

    def update_product(self, entries, listbox):
        update_product(entries, listbox)

    def delete_product(self, listbox):
        confirm_delete(listbox)

    def refresh_inventory_listbox(self, listbox):
        refresh_listbox(listbox)

    def open_inventory_add_window(self, listbox):
        open_add_edit_window("Add Product", self.add_product, listbox)

    def open_inventory_update_window(self, listbox):
        open_add_edit_window("Update Product", self.update_product, listbox)

    def delete_inventory_product(self, listbox):
        self.delete_product(listbox)

    def add_purchase(self, entries, listbox):
        add_purchase(entries, listbox)

    def update_purchase(self, entries, listbox):
        update_purchase(entries, listbox)

    def refresh_purchases_listbox(self, listbox):
        refresh_purchases_listbox(listbox)

    def open_add_purchase_window(self, listbox):
        purchase_open_add_edit_window("Add Purchase", self.add_purchase, listbox)

    def open_update_purchase_window(self, listbox):
        purchase_open_add_edit_window("Update Purchase", self.update_purchase, listbox)

