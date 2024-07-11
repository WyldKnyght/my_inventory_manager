from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, session
from models.tab_inventory import InventoryTab
from forms.tab_inventory_form import InventoryTabForm
from create_app import db
from utils.logging_colors import logger

inventory_tab_routes = Blueprint('inventory_tab', __name__)

@inventory_tab_routes.route('/', methods=['GET'])
def inventory():
    page = request.args.get('page', 1, type=int)
    items = InventoryTab.query.paginate(page=page, per_page=20)
    return render_template('tab_inventory.html', items=items)

@inventory_tab_routes.route('/new', methods=['GET', 'POST'])
def new_item():
    form = InventoryTabForm()
    if form.validate_on_submit():
        item = InventoryTab()
        form.populate_obj(item)
        db.session.add(item)
        db.session.commit()
        flash('New inventory item added successfully', 'success')
        return redirect(url_for('inventory_tab.inventory'))
    return render_template('new_inventory_item.html', form=form)

@inventory_tab_routes.route('/edit/<string:product_id>', methods=['GET', 'POST'])
def edit_item(product_id):
    item = InventoryTab.query.get_or_404(product_id)
    form = InventoryTabForm(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.commit()
        flash('Inventory item updated successfully', 'success')
        return redirect(url_for('inventory_tab.view_item', product_id=item.product_id))
    return render_template('edit_inventory_item.html', form=form, item=item)

@inventory_tab_routes.route('/view/<string:product_id>', methods=['GET'])
def view_item(product_id):
    item = InventoryTab.query.get_or_404(product_id)
    return render_template('inventory_tab_view_item.html', item=item)

@inventory_tab_routes.route('/api/inventory', methods=['GET'])
def api_inventory():
    items = InventoryTab.query.all()
    return jsonify([item.to_dict() for item in items])

@inventory_tab_routes.route('/api/inventory/<string:product_id>', methods=['GET'])
def api_inventory_detail(product_id):
    item = InventoryTab.query.get_or_404(product_id)
    return jsonify(item.to_dict())