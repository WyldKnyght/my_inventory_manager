# src/routes/admin_routes.py
from flask import Blueprint, render_template, request
from models.inventory import InventoryItem
from models.category import Category
from models.supplier import Supplier
from models.brand import Brand
from models.inventory_status import InventoryStatus
from utils.logging_colors import logger

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/admin')
def admin_dashboard():
    logger.info("Admin dashboard accessed")
    return render_template('dashboard.html')

@admin_routes.route('/admin/inventory')
def manage_inventory():
    page = request.args.get('page', 1, type=int)
    items = InventoryItem.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory page {page} accessed")
    return render_template('inventory.html', items=items)

@admin_routes.route('/admin/categories')
def manage_categories():
    page = request.args.get('page', 1, type=int)
    categories = Category.query.paginate(page=page, per_page=20)
    logger.info(f"Categories page {page} accessed")
    return render_template('categories.html', categories=categories)

@admin_routes.route('/admin/brands')
def manage_brands():
    page = request.args.get('page', 1, type=int)
    brands = Brand.query.paginate(page=page, per_page=20)
    logger.info(f"Brands page {page} accessed")
    return render_template('brands.html', brands=brands)

@admin_routes.route('/admin/inventory_status')
def manage_inventory_status():
    page = request.args.get('page', 1, type=int)
    statuses = InventoryStatus.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory status page {page} accessed")
    return render_template('inventory_status.html', statuses=statuses)

@admin_routes.route('/admin/suppliers')
def manage_suppliers():
    page = request.args.get('page', 1, type=int)
    suppliers = Supplier.query.paginate(page=page, per_page=20)
    logger.info(f"Suppliers page {page} accessed")
    return render_template('suppliers.html', suppliers=suppliers)
