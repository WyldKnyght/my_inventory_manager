# src/routes/brand_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from utils.create_app import db
from models.brand import Brand
from forms.add_brand_form import AddBrandForm
from utils.logging_colors import logger

brand_routes = Blueprint('brand', __name__)

@brand_routes.route('/brands', methods=['GET'])
def brands():
    page = request.args.get('page', 1, type=int)
    brands = Brand.query.paginate(page=page, per_page=20)
    logger.info(f"Brands page {page} accessed")
    return render_template('brands.html', brands=brands)

@brand_routes.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    form = AddBrandForm()
    if form.validate_on_submit():
        try:
            brand = Brand(
                brand_id=form.brand_id.data,
                brand_name=form.brand_name.data
            )
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

@brand_routes.route('/api/brands', methods=['GET'])
def api_brands():
    brands = Brand.query.all()
    return jsonify([brand.to_dict() for brand in brands])

@brand_routes.route('/api/brands/<string:brand_id>', methods=['GET'])
def api_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    return jsonify(brand.to_dict())
