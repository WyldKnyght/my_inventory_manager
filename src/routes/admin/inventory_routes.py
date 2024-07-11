# src/routes/admin/inventory_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from models.admin_inventory import InventoryItem
from models.admin_category import Category
from models.admin_brand import Brand
from models.admin_inventory_status import InventoryStatus
from models.admin_supplier import Supplier
from forms.admin_inventory_form import InventoryForm
from database.db_utils import add_item, edit_item, delete_item, list_items
from utils.create_app import db
from utils.logging_colors import logger

inventory_routes = Blueprint('inventory', __name__)

@inventory_routes.route('/admin/inventory', methods=['GET'])
def inventory():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    query = InventoryItem.query
    if search:
        query = query.filter(InventoryItem.product_name.ilike(f'%{search}%'))
    items = query.paginate(page=page, per_page=20)
    return render_template('inventory.html', items=items, search=search)

@inventory_routes.route('/admin/items/add', methods=['GET', 'POST'])
def add_item():
    form = InventoryForm()
    form.category_id.choices = [(c.category_id, c.category_name) for c in Category.query.all()]
    form.brand_id.choices = [(b.brand_id, b.brand_name) for b in Brand.query.all()]
    form.product_status.choices = [(s.inventory_status_id, s.status_name) for s in InventoryStatus.query.all()]
    form.supplier_id.choices = [(s.supplier_id, s.name) for s in Supplier.query.all()]

    if form.validate_on_submit():
        try:
            add_item(form.data)
            flash('Item added successfully!', 'success')
            logger.info(f"Item added: {form.data['product_name']}")
            return redirect(url_for('inventory.inventory'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding item: {str(e)}', 'error')
            logger.error(f"Error adding item: {str(e)}")
    return render_template('add_item.html', form=form)

@inventory_routes.route('/admin/items/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    form = InventoryForm(obj=item)
    form.category_id.choices = [(c.category_id, c.category_name) for c in Category.query.all()]
    form.brand_id.choices = [(b.brand_id, b.brand_name) for b in Brand.query.all()]
    form.product_status.choices = [(s.inventory_status_id, s.status_name) for s in InventoryStatus.query.all()]
    form.supplier_id.choices = [(s.supplier_id, s.name) for s in Supplier.query.all()]

    if form.validate_on_submit():
        try:
            edit_item(item_id, form.data)
            flash('Item updated successfully!', 'success')
            logger.info(f"Item updated: {item_id}")
            return redirect(url_for('inventory.inventory'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating item: {str(e)}', 'error')
            logger.error(f"Error updating item: {str(e)}")
    return render_template('edit_item.html', form=form)

@inventory_routes.route('/admin/items/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    try:
        delete_item(item_id)
        flash('Item deleted successfully!', 'success')
        logger.info(f"Item deleted: {item_id}")
    except Exception as e:
        flash(f'Error deleting item: {str(e)}', 'error')
        logger.error(f"Error deleting item: {str(e)}")
    return redirect(url_for('inventory.inventory'))

@inventory_routes.route('/admin/items/view/<string:product_id>', methods=['GET'])
def view_item(product_id):
    item = InventoryItem.query.get_or_404(product_id)
    return render_template('view_item.html', item=item)

# API endpoint
@inventory_routes.route('/api/inventory', methods=['GET'])
def api_inventory():
    items = InventoryItem.query.all()
    return jsonify([item.to_dict() for item in items])

@inventory_routes.route('/api/inventory/<string:product_id>', methods=['GET'])
def api_inventory_item(product_id):
    item = InventoryItem.query.get_or_404(product_id)
    return jsonify(item.to_dict())
