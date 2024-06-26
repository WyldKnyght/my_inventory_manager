from flask import Blueprint, render_template, flash, redirect, url_for, request
from utils.create_app import db
from models.inventory_item import InventoryItem
from forms.add_item_form import AddItemForm

bp = Blueprint('inventory', __name__)

@bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    items = InventoryItem.query.all()
    return render_template('index.html', items=items)

@bp.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        item = InventoryItem(
            product_name=form.product_name.data,
            product_code=form.product_code.data,
            description=form.description.data,
            category_id=form.category_id.data,
            brand_id=form.brand_id.data,
            size=form.size.data,
            color=form.color.data,
            cost_price=form.cost_price.data,
            markup=form.markup.data,
            retail_price=form.retail_price.data,
            product_status=form.product_status.data,
            notes=form.notes.data,
            supplier_id=form.supplier_id.data,
            singles_in_stock=form.singles_in_stock.data,
            cases_in_stock=form.cases_in_stock.data,
            qty_per_case=form.qty_per_case.data,
            condition=form.condition.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Item added successfully!')
        return redirect(url_for('inventory.inventory'))
    return render_template('add_item.html', form=form)
