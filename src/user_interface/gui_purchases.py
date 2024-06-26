# gui_purchases.py
import tkinter as tk
from tkinter import ttk, messagebox
from user_interface.purchases_ui.purchase_order_view import PurchaseOrderView

class PurchasesTab:
    def __init__(self, notebook, crud):
        self.crud = crud
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Purchases")
        self.create_widgets()

    def create_widgets(self):
        self.create_treeview(self.frame)
        self.create_buttons(self.frame)
        self.crud.refresh_purchases_listbox(self.purchases_listbox)

    def create_treeview(self, parent):
        columns = [
            "Purchase ID", "Purchase Order #", "Order Number", "Supplier ID", "Purchase Date", 
            "Shipping Date", "Shipping Tracking Number", "Total Cost"
        ]
        self.purchases_listbox = ttk.Treeview(parent, columns=columns, show='headings')
        for col in columns:
            self.purchases_listbox.heading(col, text=col)
        self.purchases_listbox.grid(row=0, column=0, columnspan=3, sticky='nsew')

        yscrollbar = ttk.Scrollbar(parent, orient='vertical', command=self.purchases_listbox.yview)
        yscrollbar.grid(row=0, column=3, sticky='ns')
        self.purchases_listbox['yscrollcommand'] = yscrollbar.set

        xscrollbar = ttk.Scrollbar(parent, orient='horizontal', command=self.purchases_listbox.xview)
        xscrollbar.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.purchases_listbox['xscrollcommand'] = xscrollbar.set

    def create_buttons(self, parent):
        ttk.Button(parent, text="New Purchase Order", command=self.new_purchase_order).grid(row=2, column=0, pady=10)
        ttk.Button(parent, text="Edit Purchase Order", command=self.edit_purchase_order).grid(row=2, column=1, pady=10)
        ttk.Button(parent, text="Delete Purchase Order", command=self.delete_purchase_order).grid(row=2, column=2, pady=10)

    def new_purchase_order(self):
        new_window = tk.Toplevel(self.frame)
        PurchaseOrderView(new_window, self.crud, lambda: self.crud.refresh_purchases_listbox(self.purchases_listbox))

    def edit_purchase_order(self):
        if selected_item := self.purchases_listbox.selection():
            purchase_id = self.purchases_listbox.item(selected_item[0], 'values')[0]
            if purchase_data := self.crud.get_purchase(purchase_id):
                edit_window = tk.Toplevel(self.frame)
                PurchaseOrderView(edit_window, self.crud, lambda: self.crud.refresh_purchases_listbox(self.purchases_listbox), purchase_data)
            else:
                messagebox.showerror("Error", "Failed to retrieve purchase order data.")
        else:
            messagebox.showwarning("Select Purchase Order", "Please select a purchase order to edit.")

    def delete_purchase_order(self):
        if selected_item := self.purchases_listbox.selection():
            purchase_id = self.purchases_listbox.item(selected_item[0], 'values')[0]
            if confirm := messagebox.askyesno(
                "Delete Purchase Order",
                f"Are you sure you want to delete purchase order {purchase_id}?",
            ):
                self.crud.delete_purchase(purchase_id)
                self.crud.refresh_purchases_listbox(self.purchases_listbox)
        else:
            messagebox.showwarning("Select Purchase Order", "Please select a purchase order to delete.")
