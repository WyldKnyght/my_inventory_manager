# src/routes/supplier_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from utils.create_app import db
from models.supplier import Supplier
from forms.add_supplier_form import AddSupplierForm
from utils.logging_colors import logger

supplier_routes = Blueprint('supplier', __name__)

@supplier_routes.route('/suppliers', methods=['GET'])
def suppliers():
    page = request.args.get('page', 1, type=int)
    suppliers = Supplier.query.paginate(page=page, per_page=20)
    logger.info(f"Suppliers page {page} accessed")
    return render_template('suppliers.html', suppliers=suppliers)

@supplier_routes.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    form = AddSupplierForm()
    if form.validate_on_submit():
        try:
            supplier = Supplier(
                supplier_id=form.supplier_id.data,
                name=form.name.data,
                contact_person=form.contact_person.data,
                address=form.address.data,
                phone=form.phone.data,
                email=form.email.data,
                website=form.website.data
            )
            db.session.add(supplier)
            db.session.commit()
            flash('Supplier added successfully!', 'success')
            logger.info(f"Supplier added: {supplier.name}")
            return redirect(url_for('supplier.suppliers'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding supplier: {str(e)}', 'error')
            logger.error(f"Error adding supplier: {str(e)}")
    return render_template('add_supplier.html', form=form)

@supplier_routes.route('/api/suppliers', methods=['GET'])
def api_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([supplier.to_dict() for supplier in suppliers])

@supplier_routes.route('/api/suppliers/<string:supplier_id>', methods=['GET'])
def api_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    return jsonify(supplier.to_dict())
