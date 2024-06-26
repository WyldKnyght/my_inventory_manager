# inventory_functions.py
from sqlite3 import DatabaseError, IntegrityError
import tkinter as tk
from tkinter import messagebox
from database.inventory.db_inventory_crud import InventoryCRUD
from utils.logging_colors import logger

crud = InventoryCRUD()

def get_selected_item(listbox):
    try:
        selected_item = listbox.selection()[0]
        item_id = listbox.item(selected_item, "text")
        return crud.get_product(item_id)
    except IndexError:
        messagebox.showwarning("Warning", "No item selected")
        return None

def add_product(entries, listbox):
    try:
        product_data = {label: entry.get() for label, entry in entries.items()}
        crud.create_product(product_data)
        refresh_listbox(listbox)
        messagebox.showinfo("Success", "Product added successfully.")
    except IntegrityError as e:
        messagebox.showerror("Error", "There was an issue adding the product due to data integrity constraints.")
        logger.exception("IntegrityError occurred while adding product:", exc_info=True)
    except DatabaseError as e:
        messagebox.showerror("Error", "There was an issue connecting to the database.")
        logger.exception("DatabaseError occurred while adding product:", exc_info=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add product: {str(e)}")
        logger.exception("General error occurred while adding product:", exc_info=True)

def update_product(entries, listbox):
    try:
        product_data = {label: entry.get() for label, entry in entries.items()}
        crud.update_product(product_data['ProductID'], product_data)
        refresh_listbox(listbox)
        messagebox.showinfo("Success", "Product updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update product: {str(e)}")
        logger.exception("Error occurred while updating product:", exc_info=True)

def delete_product(listbox):
    try:
        selected_item = listbox.selection()[0]
        item_id = listbox.item(selected_item, "text")
        crud.delete_product(item_id)
        refresh_listbox(listbox)
        messagebox.showinfo("Success", "Product deleted successfully.")
    except IndexError:
        messagebox.showwarning("Warning", "No item selected")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete product: {str(e)}")
        logger.exception("Error occurred while deleting product:", exc_info=True)

def confirm_delete(listbox):
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected product?"):
        delete_product(listbox)

def refresh_listbox(listbox):
    for i in listbox.get_children():
        listbox.delete(i)
    products = crud.get_all_products()
    for product in products:
        listbox.insert('', 'end', text=product[0], values=product[1:])