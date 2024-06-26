# purchase_add_edit_window.py
# This script defines the GUI components for the purchase add/edit window

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable, Dict, Any
from logic.purchases.purchases_functions import get_selected_purchase

# Constants
MAIN_LABELS = ["SupplierID", "OrderNumber", "Shipping", "Taxes"]
ITEM_LABELS = ["ProductName", "Description", "CategoryID", "BrandID", "Size", "Color", "Condition", "CostPrice", "Quantity", "Notes"]
MAX_ITEMS = 5

def create_main_entries(frame: ttk.Frame) -> Dict[str, ttk.Entry]:
    """Create the main entry fields for the purchase."""
    entries = {}
    for i, label in enumerate(MAIN_LABELS):
        ttk.Label(frame, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5, sticky='e')
        entries[label] = ttk.Entry(frame)
        entries[label].grid(row=i, column=1, padx=5, pady=5, sticky='w')
    return entries

def create_item_entries(frame: ttk.Frame, start_row: int) -> Dict[str, ttk.Entry]:
    """Create the entry fields for the purchase items."""
    item_entries = {}
    for j in range(1, MAX_ITEMS + 1):
        for k, label in enumerate(ITEM_LABELS):
            row = start_row + j * len(ITEM_LABELS) + k
            ttk.Label(frame, text=f"{label}_{j}:").grid(row=row, column=0, padx=5, pady=5, sticky='e')
            item_entries[f"{label}_{j}"] = ttk.Entry(frame)
            item_entries[f"{label}_{j}"].grid(row=row, column=1, padx=5, pady=5, sticky='w')
    return item_entries

def purchase_open_add_edit_window(title: str, action: Callable[[Dict[str, ttk.Entry], ttk.Treeview], None], listbox: ttk.Treeview) -> None:
    """
    Open a new window for adding or editing a purchase.

    :param title: The title of the window
    :param action: The action to perform when the submit button is clicked
    :param listbox: The listbox containing the purchases
    """
    new_window = tk.Toplevel()
    new_window.title(title)
    new_window.state('zoomed')
    new_window.minsize(1920, 1080)

    main_frame = ttk.Frame(new_window, padding="10")
    main_frame.grid(row=0, column=0, sticky='nsew')

    canvas = tk.Canvas(main_frame)
    canvas.grid(row=0, column=0, sticky='nsew')

    scrollbar_y = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
    scrollbar_y.grid(row=0, column=1, sticky='ns')
    scrollbar_x = ttk.Scrollbar(main_frame, orient='horizontal', command=canvas.xview)
    scrollbar_x.grid(row=1, column=0, sticky='ew')

    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    entries = create_main_entries(frame)
    item_entries = create_item_entries(frame, len(MAIN_LABELS))
    entries.update(item_entries)

    if title == "Update Purchase":
        if selected_purchase := get_selected_purchase(listbox):
            for label, entry in entries.items():
                entry.insert(0, selected_purchase.get(label, ""))

    button_action = ttk.Button(frame, text=title, command=lambda: action(entries, listbox))
    button_action.grid(row=len(MAIN_LABELS) + len(ITEM_LABELS) * MAX_ITEMS, column=0, columnspan=2, pady=10)

    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

    new_window.grid_rowconfigure
