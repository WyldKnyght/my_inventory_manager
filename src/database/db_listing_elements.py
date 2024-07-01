# src/database/db_listing_elements.py
from flask import render_template
from utils.create_app import bp
from database.db_utils import list_items

@bp.route('/admin/items')
def list_items_route():
    items = list_items()
    return render_template('items.html', items=items)