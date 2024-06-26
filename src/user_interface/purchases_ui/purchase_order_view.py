# purchase_order_view.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class PurchaseOrderView:
    def __init__(self, master, crud, refresh_callback, purchase_data=None):
        self.master = master
        self.crud = crud
        self.refresh_callback = refresh_callback
        self.purchase_data = purchase_data or {}
        self.items = []
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.po_frame = ttk.Frame(self.notebook)
        self.items_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.po_frame, text="Purchase Order Details")
        self.notebook.add(self.items_frame, text="Items")

        self.create_po_details()
        self.create_items_view()

        ttk.Button(self.master, text="Add Item", command=self.add_item).pack(pady=10)
        ttk.Button(self.master, text="Confirm and Save", command=self.confirm_and_save).pack(pady=10)

    def create_po_details(self):
        labels = [
            "Purchase Order #", "Order Number", "Supplier ID", "Purchase Date", 
            "Shipping Date", "Shipping Tracking Number", "Payment Method", 
            "Currency", "Exchange Rate", "Discount", "Shipping", "Taxes"
        ]
        self.po_entries = {}

        for i, label in enumerate(labels):
            ttk.Label(self.po_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = ttk.Entry(self.po_frame)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
            self.po_entries[label] = entry

        if not self.purchase_data:
            self.po_entries["Purchase Date"].insert(0, datetime.now().strftime("%Y-%m-%d"))
            self.po_entries["Currency"].insert(0, "USD")
            self.po_entries["Exchange Rate"].insert(0, "1.0")
        else:
            for label, entry in self.po_entries.items():
                entry.insert(0, self.purchase_data.get(label, ''))

    def create_items_view(self):
        self.items_tree = ttk.Treeview(self.items_frame, columns=("Product ID", "Quantity", "Cost Price", "Total"))
        self.items_tree.heading("Product ID", text="Product ID")
        self.items_tree.heading("Quantity", text="Quantity")
        self.items_tree.heading("Cost Price", text="Cost Price")
        self.items_tree.heading("Total", text="Total")
        self.items_tree.pack(fill=tk.BOTH, expand=True)

    def add_item(self):
        add_item_window = tk.Toplevel(self.master)
        add_item_window.title("Add Item")

        labels = ["Product ID", "Singles Quantity", "Cases Quantity", "Cost Price"]
        entries = {}

        for i, label in enumerate(labels):
            ttk.Label(add_item_window, text=label).grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = ttk.Entry(add_item_window)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
            entries[label] = entry

        def save_item():
            try:
                item = {
                    "Product ID": entries["Product ID"].get(),
                    "Singles Quantity": int(entries["Singles Quantity"].get()),
                    "Cases Quantity": int(entries["Cases Quantity"].get()),
                    "Cost Price": float(entries["Cost Price"].get())
                }
                total = (item["Singles Quantity"] + item["Cases Quantity"]) * item["Cost Price"]
                self.items.append(item)
                self.items_tree.insert("", "end", values=(item["Product ID"], 
                                                          item["Singles Quantity"] + item["Cases Quantity"], 
                                                          item["Cost Price"], 
                                                          total))
                add_item_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for quantities and cost price.")

        ttk.Button(add_item_window, text="Save Item", command=save_item).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def confirm_and_save(self):
        self.purchase_data = {label: entry.get() for label, entry in self.po_entries.items()}
        
        confirmation = f"Purchase Order Details:\n\n"
        for label, value in self.purchase_data.items():
            confirmation += f"{label}: {value}\n"
        
        confirmation += f"\nItems ({len(self.items)}):\n"
        for i, item in enumerate(self.items, 1):
            confirmation += f"\nItem {i}:\n"
            for label, value in item.items():
                confirmation += f"  {label}: {value}\n"
        
        confirmation += "\nDo you want to save this purchase order?"
        
        if messagebox.askyesno("Confirm Purchase Order", confirmation):
            self.save_to_database()
        else:
            messagebox.showinfo("Cancelled", "Purchase order was not saved.")

    def save_to_database(self):
        try:
            subtotal = sum((item["Singles Quantity"] + item["Cases Quantity"]) * item["Cost Price"] for item in self.items)
            shipping = float(self.purchase_data["Shipping"])
            taxes = float(self.purchase_data["Taxes"])
            total_cost = subtotal + shipping + taxes - float(self.purchase_data["Discount"])

            purchase_data = {
                "Purchase Order #": self.purchase_data["Purchase Order #"],
                "Order Number": self.purchase_data["Order Number"],
                "Supplier ID": self.purchase_data["Supplier ID"],
                "Purchase Date": self.purchase_data["Purchase Date"],
                "Shipping Date": self.purchase_data["Shipping Date"],
                "Shipping Tracking Number": self.purchase_data["Shipping Tracking Number"],
                "Payment Method": self.purchase_data["Payment Method"],
                "Currency": self.purchase_data["Currency"],
                "Exchange Rate": float(self.purchase_data["Exchange Rate"]),
                "Discount": float(self.purchase_data["Discount"]),
                "Shipping": shipping,
                "Taxes": taxes,
                "Total Cost": total_cost
            }

            purchase_id = self.crud.create_purchase(purchase_data)

            for item in self.items:
                item_data = {
                    "Purchase ID": purchase_id,
                    "Product ID": item["Product ID"],
                    "Singles Quantity": item["Singles Quantity"],
                    "Cases Quantity": item["Cases Quantity"],
                    "Cost Price": item["Cost Price"]
                }
                self.crud.add_purchase_item(item_data)

            self.refresh_callback()
            self.master.destroy()
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving the purchase order: {e}")
