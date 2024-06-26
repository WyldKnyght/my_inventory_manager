# src/routes/category_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from utils.create_app import db
from models.category import Category
from forms.add_category_form import AddCategoryForm

bp = Blueprint('category', __name__)

@bp.route('/categories', methods=['GET'])
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@bp.route('/add_category', methods=['GET', 'POST'])
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        category = Category(
            category_id=form.category_id.data,
            category_name=form.category_name.data,
            category_prefix=form.category_prefix.data,
            parent_category_id=form.parent_category_id.data,
            sub_categories_name=form.sub_categories_name.data
        )
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!')
        return redirect(url_for('category.categories'))
    return render_template('add_category.html', form=form)
