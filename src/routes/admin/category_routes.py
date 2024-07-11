# src/routes/category_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from create_app import db
from models.admin_category import Category
from forms.admin_category_form import CategoryForm
from utils.logging_colors import logger

category_routes = Blueprint('category', __name__)

@category_routes.route('/categories', methods=['GET'])
def categories():
    page = request.args.get('page', 1, type=int)
    categories = Category.query.paginate(page=page, per_page=20)
    logger.info(f"Categories page {page} accessed")
    return render_template('categories.html', categories=categories)

@category_routes.route('/add_category', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        try:
            category = Category(
                category_id=form.category_id.data,
                category_name=form.category_name.data,
                category_prefix=form.category_prefix.data,
                parent_category_id=form.parent_category_id.data,
                sub_categories_name=form.sub_categories_name.data
            )
            db.session.add(category)
            db.session.commit()
            flash('Category added successfully!', 'success')
            logger.info(f"Category added: {category.category_name}")
            return redirect(url_for('category.categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding category: {str(e)}', 'error')
            logger.error(f"Error adding category: {str(e)}")
    return render_template('add_category.html', form=form)

@category_routes.route('/api/categories', methods=['GET'])
def api_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@category_routes.route('/api/categories/<string:category_id>', methods=['GET'])
def api_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify(category.to_dict())
