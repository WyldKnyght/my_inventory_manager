from sqlite3 import DatabaseError, IntegrityError
from typing import Dict, List, Any
import tkinter as tk
from tkinter import ttk, messagebox
from database.purchases.db_purchases_crud import PurchasesCRUD
from utils.logging_colors import logger
from dataclasses import dataclass

crud = PurchasesCRUD()

@dataclass
class PurchaseData:
    supplier_id: int
    order_number: str
    shipping: float
    taxes: float

@dataclass
class ItemData:
    product_name: str
    description: str
    category: int
    brand: int
    size: str
    color: str
    condition: str
    cost_price: float
    quantity: int
    notes: str

def get_selected_purchase(listbox: ttk.Treeview) -> Dict[str, Any]:
    """Get the selected purchase from the listbox."""
    try:
        selected_item = listbox.selection()[0]
        item_id = listbox.item(selected_item, "text")
        return crud.get_purchase(item_id)
    except IndexError:
        messagebox.showwarning("Warning", "No purchase selected")
        return None

def extract_purchase_data(entries: Dict[str, ttk.Entry]) -> PurchaseData:
    """Extract and validate purchase data from the entry fields."""
    try:
        return PurchaseData(
            supplier_id=int(entries['SupplierID'].get()),
            order_number=entries['OrderNumber'].get(),
            shipping=float(entries['Shipping'].get()),
            taxes=float(entries['Taxes'].get())
        )
    except ValueError as e:
        raise ValueError(f"Invalid input in purchase data: {str(e)}") from e

def extract_item_data(entries: Dict[str, ttk.Entry], item_count: int) -> ItemData:
    """Extract and validate item data from the entry fields for a specific item."""
    try:
        return ItemData(
            product_name=entries[f'ProductName_{item_count}'].get(),
            description=entries[f'Description_{item_count}'].get(),
            category=int(entries[f'CategoryID_{item_count}'].get()),
            brand=int(entries[f'BrandID_{item_count}'].get()),
            size=entries[f'Size_{item_count}'].get(),
            color=entries[f'Color_{item_count}'].get(),
            condition=entries[f'Condition_{item_count}'].get(),
            cost_price=float(entries[f'CostPrice_{item_count}'].get()),
            quantity=int(entries[f'Quantity_{item_count}'].get()),
            notes=entries[f'Notes_{item_count}'].get()
        )
    except ValueError as e:
        raise ValueError(f"Invalid input in item {item_count} data: {str(e)}") from e

def extract_items_data(entries: Dict[str, ttk.Entry]) -> List[ItemData]:
    """Extract data for all items from the entry fields."""
    return [extract_item_data(entries, i) for i in range(1, 6) if f'ProductName_{i}' in entries]

def add_purchase(entries: Dict[str, ttk.Entry], listbox: ttk.Treeview) -> None:
    """Add a new purchase to the database."""
    try:
        purchase_data = extract_purchase_data(entries)
        items = extract_items_data(entries)

        purchase_id = crud.add_purchase_order(
            purchase_data.supplier_id,
            purchase_data.order_number,
            items,
            purchase_data.shipping,
            purchase_data.taxes
        )

        refresh_purchases_listbox(listbox)
        messagebox.showinfo("Success", f"Purchase order added successfully with ID: {purchase_id}")
    except Exception as e:
        handle_error(e)

def update_purchase(entries: Dict[str, ttk.Entry], listbox: ttk.Treeview) -> None:
    """Update an existing purchase order in the database."""
    try:
        selected_purchase = get_selected_purchase(listbox)
        if not selected_purchase:
            return

        purchase_data = extract_purchase_data(entries)
        items = extract_items_data(entries)

        crud.update_purchase_order(
            selected_purchase['purchase_id'],
            purchase_data.supplier_id,
            purchase_data.order_number,
            items,
            purchase_data.shipping,
            purchase_data.taxes
        )

        refresh_purchases_listbox(listbox)
        messagebox.showinfo("Success", "Purchase order updated successfully")
    except Exception as e:
        handle_error(e)



def refresh_purchases_listbox(self, listbox):
    for i in listbox.get_children():
        listbox.delete(i)
    purchases = self.crud.get_all_purchases()
    for purchase in purchases:
        listbox.insert("", "end", text=purchase['PurchaseID'], values=(
            purchase['PurchaseOrderNumber'],
            purchase['OrderNumber'],
            purchase['PurchaseDate'],
            purchase['SupplierID'],
            purchase['TotalCost']
        ))

def handle_error(e: Exception) -> None:
    """Handle different types of errors and display appropriate messages."""
    if isinstance(e, IntegrityError):
        messagebox.showerror("Error", "There was an issue adding the purchase due to data integrity constraints.")
    elif isinstance(e, DatabaseError):
        messagebox.showerror("Error", "There was an issue connecting to the database.")
    elif isinstance(e, ValueError):
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
    else:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    logger.error(str(e))
