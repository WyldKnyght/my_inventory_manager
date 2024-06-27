# src/routes/inventory_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from models.inventory_item import InventoryItem
from forms.add_item_form import AddItemForm
from database.db_utils import add_item, edit_item, delete_item, list_items

inventory_routes = Blueprint('inventory', __name__)

@inventory_routes.route('/admin/inventory', methods=['GET', 'POST'])
def inventory():
    items = list_items()
    return render_template('inventory.html', items=items)

@inventory_routes.route('/admin/items/add', methods=['GET', 'POST'])
def add_item_route():
    form = AddItemForm()
    if form.validate_on_submit():
        add_item(form.data)
        flash('Item added successfully!')
        return redirect(url_for('inventory.inventory'))
    return render_template('add_item.html', form=form)

@inventory_routes.route('/admin/items/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item_route(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    form = AddItemForm(obj=item)
    if form.validate_on_submit():
        edit_item(item_id, form.data)
        flash('Item updated successfully!')
        return redirect(url_for('inventory.inventory'))
    return render_template('edit_item.html', form=form)

@inventory_routes.route('/admin/items/delete/<int:item_id>', methods=['POST'])
def delete_item_route(item_id):
    delete_item(item_id)
    flash('Item deleted successfully!')
    return redirect(url_for('inventory.inventory'))
