# src/routes/brand_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from utils.create_app import db
from models.brand import Brand
from forms.add_brand_form import AddBrandForm

brand_routes = Blueprint('brand', __name__)

@brand_routes.route('/brands', methods=['GET'])
def brands():
    brands = Brand.query.all()
    return render_template('brands.html', brands=brands)

@brand_routes.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    form = AddBrandForm()
    if form.validate_on_submit():
        brand = Brand(
            brand_id=form.brand_id.data,
            brand_name=form.brand_name.data
        )
        db.session.add(brand)
        db.session.commit()
        flash('Brand added successfully!')
        return redirect(url_for('brand.brands'))
    return render_template('add_brand.html', form=form)
