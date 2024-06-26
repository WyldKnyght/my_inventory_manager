# inventory_add_edit_window.py
import tkinter as tk
from tkinter import ttk
from logic.inventory.inventory_functions import get_selected_item

def open_add_edit_window(title, action, listbox):
    new_window = tk.Toplevel()
    new_window.title(title)
    new_window.state('zoomed')
    new_window.minsize(1920, 1080)

    frame = ttk.Frame(new_window, padding="10")
    frame.grid(row=0, column=0)

    labels = ["ProductID", "ProductName", "ProductCode", "Description", "CategoryID", "BrandID", 
                "Size", "Color", "Condition", "CostPrice", "Markup", "RetailPrice", "ProductStatus", 
                "Notes", "SupplierID", "SinglesInStock", "CasesInStock", "QtyPerCase"]
    entries = {label: ttk.Entry(frame) for label in labels}

    for i, (label, entry) in enumerate(entries.items()):
        ttk.Label(frame, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5, sticky='e')
        entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')

    if title == "Update Product":
        if selected_item := get_selected_item(listbox):
            for label, entry in entries.items():
                entry.insert(0, selected_item[label])

    button_action = ttk.Button(frame, text=title, command=lambda: action(entries, listbox))
    button_action.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Make the window scrollable if it's too large
    canvas = tk.Canvas(new_window)
    canvas.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(new_window, orient='vertical', command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    new_window.grid_rowconfigure(0, weight=1)
    new_window.grid_columnconfigure(0, weight=1)