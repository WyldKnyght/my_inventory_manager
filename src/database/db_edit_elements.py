# src/database/db_edit_elements.py
from flask import render_template
from utils.create_app import bp
from forms import AddItemForm
from database.db_utils import edit_item

@bp.route('/admin/items/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item_route(item_id):
    form = AddItemForm()
    if form.validate_on_submit():
        return edit_item(item_id, form.data)
    return render_template('admin/edit_item.html', form=form)
