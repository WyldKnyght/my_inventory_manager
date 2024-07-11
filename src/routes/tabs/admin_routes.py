# src/routes/tab_admin_routes.py
from flask import Blueprint, render_template, request
from models.admin_inventory import InventoryItem
from models.admin_category import Category
from models.admin_supplier import Supplier
from models.admin_brand import Brand
from models.admin_inventory_status import InventoryStatus
from utils.logging_colors import logger

admin_tab_routes = Blueprint('admin', __name__)

@admin_tab_routes.route('/')
def index():
    """Index page."""
    return render_template('index.html')

@admin_tab_routes.route('/admin')
def admin_dashboard():
    """Admin dashboard."""
    navbar_items = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Sales', 'url': '#'},
        {'name': 'Purchases', 'url': '#'},
        {'name': 'Inventory', 'url': '/admin/inventory'},
        {'name': 'Reports', 'url': '#'},
        {'name': 'Admin', 'url': '/admin'},
    ]
    return render_template('dashboard.html', navbar_items=navbar_items, active_page='admin')

@admin_tab_routes.route('/admin/inventory')
def manage_inventory():
    page = request.args.get('page', 1, type=int)
    items = InventoryItem.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory page {page} accessed")
    return render_template('inventory.html', items=items)

@admin_tab_routes.route('/admin/categories')
def manage_categories():
    page = request.args.get('page', 1, type=int)
    categories = Category.query.paginate(page=page, per_page=20)
    logger.info(f"Categories page {page} accessed")
    return render_template('categories.html', categories=categories)

@admin_tab_routes.route('/admin/brands')
def manage_brands():
    page = request.args.get('page', 1, type=int)
    brands = Brand.query.paginate(page=page, per_page=20)
    logger.info(f"Brands page {page} accessed")
    return render_template('brands.html', brands=brands)

@admin_tab_routes.route('/admin/inventory_status')
def manage_inventory_status():
    page = request.args.get('page', 1, type=int)
    statuses = InventoryStatus.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory status page {page} accessed")
    return render_template('inventory_status.html', statuses=statuses)

@admin_tab_routes.route('/admin/suppliers')
def manage_suppliers():
    page = request.args.get('page', 1, type=int)
    suppliers = Supplier.query.paginate(page=page, per_page=20)
    logger.info(f"Suppliers page {page} accessed")
    return render_template('suppliers.html', suppliers=suppliers)