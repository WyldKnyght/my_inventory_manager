# src/routes/inventory_tab_routes.py
from flask import Blueprint, render_template, request
from models.admin_inventory import InventoryItem
from utils.create_app import db

inventory_tab_routes = Blueprint('inventory_tab', __name__)

@inventory_tab_routes.route('/', methods=['GET'])
def inventory_tab():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    sort_by = request.args.get('sort_by', 'product_name')
    order = request.args.get('order', 'asc')

    query = InventoryItem.query

    if search:
        query = query.filter(InventoryItem.product_name.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(getattr(InventoryItem, sort_by).asc())
    else:
        query = query.order_by(getattr(InventoryItem, sort_by).desc())

    items = query.paginate(page=page, per_page=20)
    return render_template('inventory_tab.html', items=items, search=search, sort_by=sort_by, order=order)

@inventory_tab_routes.route('/view/<string:product_id>', methods=['GET'])
def view_item(product_id):
    item = InventoryItem.query.get_or_404(product_id)
    return render_template('inventory_tab_view_item.html', item=item)