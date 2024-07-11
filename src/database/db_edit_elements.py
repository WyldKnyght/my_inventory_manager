# src/database/db_edit_elements.py
from flask import render_template, flash, redirect, url_for
from create_app import bp
from forms import AddItemForm
from database.db_utils import edit_item
from models.admin_inventory import InventoryItem

@bp.route('/admin/items/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item_route(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    form = AddItemForm(obj=item)
    if form.validate_on_submit():
        try:
            edit_item(item_id, form.data)
            flash('Item updated successfully!', 'success')
            return redirect(url_for('inventory.list_items'))
        except Exception as e:
            flash(f'Error updating item: {str(e)}', 'error')
    return render_template('edit_item.html', form=form)