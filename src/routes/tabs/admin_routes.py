# src/routes/tas/admin_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, session
from models.admin_inventory import InventoryItem
from models.admin_category import Category
from models.admin_supplier import Supplier
from models.admin_brand import Brand
from models.admin_inventory_status import InventoryStatus
from create_app import db
from utils.logging_colors import logger
from forms.admin_inventory_form import InventoryForm
from forms.admin_category_form import CategoryForm
from forms.admin_supplier_form import SupplierForm
from forms.admin_brand_form import BrandForm
from forms.admin_inventory_status_form import InventoryStatusForm

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

@admin_tab_routes.route('/admin/inventory', methods=['GET', 'POST'])
def manage_inventory():
    page = request.args.get('page', 1, type=int)
    items = InventoryItem.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory page {page} accessed")
    return render_template('inventory.html', items=items)

@admin_tab_routes.route('/admin/inventory/new', methods=['GET', 'POST'])
def new_inventory_item():
    form = InventoryForm()
    if form.validate_on_submit():
        item = InventoryItem()
        form.populate_obj(item)
        db.session.add(item)
        db.session.commit()
        flash('New inventory item added successfully', 'success')
        return redirect(url_for('admin.manage_inventory'))
    return render_template('new_inventory_item.html', form=form)

@admin_tab_routes.route('/admin/inventory/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_inventory_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    form = InventoryForm(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.commit()
        flash('Inventory item updated successfully', 'success')
        return redirect(url_for('admin.manage_inventory'))
    return render_template('edit_inventory_item.html', form=form, item=item)

@admin_tab_routes.route('/admin/categories', methods=['GET', 'POST'])
def manage_categories():
    page = request.args.get('page', 1, type=int)
    categories = Category.query.paginate(page=page, per_page=20)
    logger.info(f"Categories page {page} accessed")
    return render_template('categories.html', categories=categories)

@admin_tab_routes.route('/admin/categories/new', methods=['GET', 'POST'])
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category()
        form.populate_obj(category)
        db.session.add(category)
        db.session.commit()
        flash('New category added successfully', 'success')
        return redirect(url_for('admin.manage_categories'))
    return render_template('new_category.html', form=form)

@admin_tab_routes.route('/admin/categories/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        form.populate_obj(category)
        db.session.commit()
        flash('Category updated successfully', 'success')
        return redirect(url_for('admin.manage_categories'))
    return render_template('edit_category.html', form=form, category=category)

@admin_tab_routes.route('/admin/brands', methods=['GET', 'POST'])
def manage_brands():
    page = request.args.get('page', 1, type=int)
    brands = Brand.query.paginate(page=page, per_page=20)
    logger.info(f"Brands page {page} accessed")
    return render_template('brands.html', brands=brands)

@admin_tab_routes.route('/admin/brands/new', methods=['GET', 'POST'])
def new_brand():
    form = BrandForm()
    if form.validate_on_submit():
        brand = Brand()
        form.populate_obj(brand)
        db.session.add(brand)
        db.session.commit()
        flash('New brand added successfully', 'success')
        return redirect(url_for('admin.manage_brands'))
    return render_template('new_brand.html', form=form)

@admin_tab_routes.route('/admin/brands/edit/<int:brand_id>', methods=['GET', 'POST'])
def edit_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    form = BrandForm(obj=brand)
    if form.validate_on_submit():
        form.populate_obj(brand)
        db.session.commit()
        flash('Brand updated successfully', 'success')
        return redirect(url_for('admin.manage_brands'))
    return render_template('edit_brand.html', form=form, brand=brand)

@admin_tab_routes.route('/admin/inventory_status', methods=['GET', 'POST'])
def manage_inventory_status():
    page = request.args.get('page', 1, type=int)
    statuses = InventoryStatus.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory status page {page} accessed")
    return render_template('inventory_status.html', statuses=statuses)

@admin_tab_routes.route('/admin/inventory_status/new', methods=['GET', 'POST'])
def new_inventory_status():
    form = InventoryStatusForm()
    if form.validate_on_submit():
        status = InventoryStatus()
        form.populate_obj(status)
        db.session.add(status)
        db.session.commit()
        flash('New inventory status added successfully', 'success')
        return redirect(url_for('admin.manage_inventory_status'))
    return render_template('new_inventory_status.html', form=form)

@admin_tab_routes.route('/admin/inventory_status/edit/<int:status_id>', methods=['GET', 'POST'])
def edit_inventory_status(status_id):
    status = InventoryStatus.query.get_or_404(status_id)
    form = InventoryStatusForm(obj=status)
    if form.validate_on_submit():
        form.populate_obj(status)
        db.session.commit()
        flash('Inventory status updated successfully', 'success')
        return redirect(url_for('admin.manage_inventory_status'))
    return render_template('edit_inventory_status.html', form=form, status=status)

@admin_tab_routes.route('/admin/suppliers', methods=['GET', 'POST'])
def manage_suppliers():
    page = request.args.get('page', 1, type=int)
    suppliers = Supplier.query.paginate(page=page, per_page=20)
    logger.info(f"Suppliers page {page} accessed")
    return render_template('suppliers.html', suppliers=suppliers)

@admin_tab_routes.route('/admin/suppliers/new', methods=['GET', 'POST'])
def new_supplier():
    form = SupplierForm()
    if form.validate_on_submit():
        supplier = Supplier()
        form.populate_obj(supplier)
        db.session.add(supplier)
        db.session.commit()
        flash('New supplier added successfully', 'success')
        return redirect(url_for('admin.manage_suppliers'))
    return render_template('new_supplier.html', form=form)

@admin_tab_routes.route('/admin/suppliers/edit/<int:supplier_id>', methods=['GET', 'POST'])
def edit_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    form = SupplierForm(obj=supplier)
    if form.validate_on_submit():
        form.populate_obj(supplier)
        db.session.commit()
        flash('Supplier updated successfully', 'success')
        return redirect(url_for('admin.manage_suppliers'))
    return render_template('edit_supplier.html', form=form, supplier=supplier)

# API routes for admin sections

@admin_tab_routes.route('/api/admin/inventory', methods=['GET'])
def api_inventory():
    items = InventoryItem.query.all()
    return jsonify([item.to_dict() for item in items])

@admin_tab_routes.route('/api/admin/categories', methods=['GET'])
def api_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@admin_tab_routes.route('/api/admin/brands', methods=['GET'])
def api_brands():
    brands = Brand.query.all()
    return jsonify([brand.to_dict() for brand in brands])

@admin_tab_routes.route('/api/admin/inventory_status', methods=['GET'])
def api_inventory_status():
    statuses = InventoryStatus.query.all()
    return jsonify([status.to_dict() for status in statuses])

@admin_tab_routes.route('/api/admin/suppliers', methods=['GET'])
def api_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([supplier.to_dict() for supplier in suppliers])