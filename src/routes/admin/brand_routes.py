# src/routes/admin_brand_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from create_app import db
from models.admin_brand import Brand
from forms.admin_brand_form import BrandForm, BrandSearchForm
from utils.logging_colors import logger

brand_routes = Blueprint('brand', __name__)

@brand_routes.route('/admin/brands', methods=['GET', 'POST'])
def brands():
    form = BrandSearchForm()
    page = request.args.get('page', 1, type=int)
    query = Brand.query

    if form.validate_on_submit() or request.args.get('search'):
        if search_term := form.search_term.data or request.args.get('search'):
            query = query.filter(Brand.brand_name.like(f'%{search_term}%'))

    brands = query.paginate(page=page, per_page=20)
    return render_template('brands.html', brands=brands, form=form)

@brand_routes.route('/admin/brands/add', methods=['GET', 'POST'])
def add_brand():
    form = BrandForm()
    if form.validate_on_submit():
        try:
            brand = Brand(brand_name=form.brand_name.data)
            db.session.add(brand)
            db.session.commit()
            flash('Brand added successfully!', 'success')
            logger.info(f"Brand added: {brand.brand_name}")
            return redirect(url_for('brand.brands'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding brand: {str(e)}', 'error')
            logger.error(f"Error adding brand: {str(e)}")
    return render_template('add_brand.html', form=form)

@brand_routes.route('/admin/brands/edit/<string:brand_id>', methods=['GET', 'POST'])
def edit_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    form = BrandForm(obj=brand)
    if form.validate_on_submit():
        try:
            brand.brand_name = form.brand_name.data
            db.session.commit()
            flash('Brand updated successfully!', 'success')
            logger.info(f"Brand updated: {brand.brand_name}")
            return redirect(url_for('brand.brands'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating brand: {str(e)}', 'error')
            logger.error(f"Error updating brand: {str(e)}")
    return render_template('edit_brand.html', form=form, brand=brand)

@brand_routes.route('/admin/brands/delete/<string:brand_id>', methods=['POST'])
def delete_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    try:
        db.session.delete(brand)
        db.session.commit()
        flash('Brand deleted successfully!', 'success')
        logger.info(f"Brand deleted: {brand.brand_name}")
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting brand: {str(e)}', 'error')
        logger.error(f"Error deleting brand: {str(e)}")
    return redirect(url_for('brand.brands'))

@brand_routes.route('/api/brands', methods=['GET'])
def api_brands():
    brands = Brand.query.all()
    return jsonify([brand.to_dict() for brand in brands])

@brand_routes.route('/api/brands/<string:brand_id>', methods=['GET'])
def api_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    return jsonify(brand.to_dict())