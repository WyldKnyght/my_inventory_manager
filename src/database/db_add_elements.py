# src/database/db_add_elements.py
from flask import render_template, flash, redirect, url_for
from create_app import bp
from forms import AddItemForm
from database.db_utils import add_item

@bp.route('/admin/items/add', methods=['GET', 'POST'])
def add_item_route():
    form = AddItemForm()
    if form.validate_on_submit():
        try:
            add_item(form.data)
            flash('Item added successfully!', 'success')
            return redirect(url_for('inventory.list_items'))
        except Exception as e:
            flash(f'Error adding item: {str(e)}', 'error')
    return render_template('add_item.html', form=form)