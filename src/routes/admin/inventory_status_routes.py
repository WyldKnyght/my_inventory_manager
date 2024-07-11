# src/routes/inventory_status_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from create_app import db
from models.admin_inventory_status import InventoryStatus
from forms.admin_inventory_status_form import InventoryStatusForm
from utils.logging_colors import logger

inventory_status_routes = Blueprint('status', __name__)

@inventory_status_routes.route('/statuses', methods=['GET'])
def statuses():
    page = request.args.get('page', 1, type=int)
    statuses = InventoryStatus.query.paginate(page=page, per_page=20)
    logger.info(f"Inventory status page {page} accessed")
    return render_template('statuses.html', statuses=statuses)

@inventory_status_routes.route('/add_status', methods=['GET', 'POST'])
def add_status():
    form = InventoryStatusForm()
    if form.validate_on_submit():
        try:
            status = InventoryStatus(
                inventory_status_id=form.inventory_status_id.data,
                status_name=form.status_name.data,
                status_prefix=form.status_prefix.data
            )
            db.session.add(status)
            db.session.commit()
            flash('Status added successfully!', 'success')
            logger.info(f"Inventory status added: {status.status_name}")
            return redirect(url_for('status.statuses'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding status: {str(e)}', 'error')
            logger.error(f"Error adding inventory status: {str(e)}")
    return render_template('add_status.html', form=form)

@inventory_status_routes.route('/api/statuses', methods=['GET'])
def api_statuses():
    statuses = InventoryStatus.query.all()
    return jsonify([status.to_dict() for status in statuses])

@inventory_status_routes.route('/api/statuses/<string:status_id>', methods=['GET'])
def api_status(status_id):
    status = InventoryStatus.query.get_or_404(status_id)
    return jsonify(status.to_dict())
