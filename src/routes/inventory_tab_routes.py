# src/routes/inventory_tab_routes.py
from flask import Blueprint, render_template, request
from models.inventory import InventoryItem
from utils.create_app import db

inventory_tab_routes = Blueprint('inventory_tab', __name__)

@inventory_tab_routes.route('/inventory_tab', methods=['GET'])
def inventory_tab():
    page = request.args.get('page', 1, type=int)
    items = InventoryItem.query.paginate(page=page, per_page=20)
    return render_template('inventory_tab.html', items=items)
