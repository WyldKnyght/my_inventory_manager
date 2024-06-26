# src/routes/inventory_status_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from utils.create_app import db
from models.inventory_status import InventoryStatus
from forms.add_inventory_status_form import AddInventoryStatusForm

bp = Blueprint('status', __name__)

@bp.route('/statuses', methods=['GET'])
def statuses():
    statuses = InventoryStatus.query.all()
    return render_template('statuses.html', statuses=statuses)

@bp.route('/add_status', methods=['GET', 'POST'])
def add_status():
    form = AddInventoryStatusForm()
    if form.validate_on_submit():
        status = InventoryStatus(
            inventory_status_id=form.inventory_status_id.data,
            status_name=form.status_name.data,
            status_prefix=form.status_prefix.data
        )
        db.session.add(status)
        db.session.commit()
        flash('Status added successfully!')
        return redirect(url_for('status.statuses'))
    return render_template('add_status.html', form=form)
