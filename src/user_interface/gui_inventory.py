# gui_inventory.py
from tkinter import ttk

class InventoryTab:
    def __init__(self, notebook, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(notebook, padding="10")
        notebook.add(self.frame, text="Inventory")
        self.create_widgets()

    def create_widgets(self):
        columns = ("ProductID", "ProductName", "ProductCode", "Description", "CategoryID", "BrandID", 
                   "Size", "Color", "Condition", "CostPrice", "Markup", "RetailPrice", "ProductStatus", 
                   "SupplierID", "SinglesInStock", "CasesInStock", "QtyPerCase", "TotalInStock", "TotalNumberOfSales")

        self.listbox = ttk.Treeview(self.frame, columns=columns, show='headings')
        for col in columns:
            self.listbox.heading(col, text=col)
            self.listbox.column(col, width=75)  # Adjust width as needed

        self.listbox.grid(row=1, column=0, columnspan=3, sticky='nsew')

        # Add scrollbars
        yscrollbar = ttk.Scrollbar(self.frame, orient='vertical', command=self.listbox.yview)
        yscrollbar.grid(row=1, column=3, sticky='ns')
        self.listbox.configure(yscrollcommand=yscrollbar.set)

        xscrollbar = ttk.Scrollbar(self.frame, orient='horizontal', command=self.listbox.xview)
        xscrollbar.grid(row=2, column=0, columnspan=3, sticky='ew')
        self.listbox.configure(xscrollcommand=xscrollbar.set)

        self.mediator.refresh_inventory_listbox(self.listbox)

        self.create_buttons()

    def create_buttons(self):
        frame_buttons = ttk.Frame(self.frame)
        frame_buttons.grid(row=3, column=0, columnspan=3, pady=20)

        button_add = ttk.Button(frame_buttons, text="Add Product", command=self.open_add_window)
        button_add.grid(row=0, column=0, padx=5, pady=5)

        button_update = ttk.Button(frame_buttons, text="Update Product", command=self.open_update_window)
        button_update.grid(row=0, column=1, padx=5, pady=5)

        button_delete = ttk.Button(frame_buttons, text="Delete Product", command=self.delete_product)
        button_delete.grid(row=0, column=2, padx=5, pady=5)

    def open_add_window(self):
        self.mediator.open_inventory_add_window(self.listbox)

    def open_update_window(self):
        self.mediator.open_inventory_update_window(self.listbox)

    def delete_product(self):
        self.mediator.delete_inventory_product(self.listbox)