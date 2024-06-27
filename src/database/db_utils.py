# src/database/database_utils.py
from flask import flash, redirect, url_for
from utils.create_app import db
from models.inventory_item import InventoryItem

def add_item(form_data):
    item = InventoryItem(**form_data)
    db.session.add(item)
    db.session.commit()
    flash('Item added successfully!')
    return redirect(url_for('inventory.list_items'))

def list_items():
    return InventoryItem.query.all()

def edit_item(item_id, form_data):
    item = InventoryItem.query.get_or_404(item_id)
    item.product_name = form_data.get('product_name')
    # Update other fields similarly...
    db.session.commit()
    flash('Item updated successfully!')
    return redirect(url_for('inventory.list_items'))

def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!')
    return redirect(url_for('inventory.list_items'))
