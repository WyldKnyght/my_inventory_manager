# src/database/database_utils.py
from flask import flash, redirect, url_for
from utils.create_app import db
from models.inventory import InventoryItem
import logging

logger = logging.getLogger(__name__)

def add_item(form_data):
    try:
        item = InventoryItem(**form_data)
        db.session.add(item)
        db.session.commit()
        logger.info(f"Item added: {item.product_name}")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error adding item: {str(e)}")
        raise

def list_items():
    return InventoryItem.query.all()

def edit_item(item_id, form_data):
    try:
        item = InventoryItem.query.get_or_404(item_id)
        item.product_name = form_data.get('product_name')
        # Update other fields similarly...
        db.session.commit()
        logger.info(f"Item updated: {item_id}")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating item: {str(e)}")
        raise

def delete_item(item_id):
    try:
        item = InventoryItem.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        logger.info(f"Item deleted: {item_id}")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting item: {str(e)}")
        raise