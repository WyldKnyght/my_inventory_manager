# src/routes/admin_routes.py
from flask import Blueprint, render_template
from models.inventory_item import InventoryItem
from models.category import Category
from models.supplier import Supplier
from models.brand import Brand
from models.inventory_status import InventoryStatus

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/admin')
def admin_dashboard():
    return render_template('dashboard.html')

@admin_routes.route('/admin/inventory')
def manage_inventory():
    items = InventoryItem.query.all()
    return render_template('inventory.html', items=items)

@admin_routes.route('/admin/categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@admin_routes.route('/admin/brands')
def manage_brands():
    brands = Brand.query.all()
    return render_template('brands.html', brands=brands)

@admin_routes.route('/admin/inventory_status')
def manage_inventory_status():
    statuses = InventoryStatus.query.all()
    return render_template('inventory_status.html', statuses=statuses)

@admin_routes.route('/admin/suppliers')
def manage_suppliers():
    suppliers = Supplier.query.all()
    return render_template('suppliers.html', suppliers=suppliers)
