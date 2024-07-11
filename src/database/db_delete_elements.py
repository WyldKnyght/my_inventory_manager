# src/database/db_delete_elements.py
from flask import flash, redirect, url_for
from create_app import bp
from database.db_utils import delete_item

@bp.route('/admin/items/delete/<int:item_id>', methods=['POST'])
def delete_item_route(item_id):
    try:
        delete_item(item_id)
        flash('Item deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting item: {str(e)}', 'error')
    return redirect(url_for('inventory.list_items'))