# src/database/db_add_elements.py
from flask import render_template
from utils.create_app import bp
from forms import AddItemForm
from database. db_utils import add_item

@bp.route('/admin/items/add', methods=['GET', 'POST'])
def add_item_route():
    form = AddItemForm()
    if form.validate_on_submit():
        return add_item(form.data)
    return render_template('admin/add_item.html', form=form)
