# src/routes/supplier_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from utils.create_app import db
from models.supplier import Supplier
from forms.add_supplier_form import AddSupplierForm

supplier_routes = Blueprint('supplier', __name__)

@supplier_routes.route('/suppliers', methods=['GET'])
def suppliers():
    suppliers = Supplier.query.all()
    return render_template('suppliers.html', suppliers=suppliers)

@supplier_routes.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    form = AddSupplierForm()
    if form.validate_on_submit():
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
        flash('Supplier added successfully!')
        return redirect(url_for('supplier.suppliers'))
    return render_template('add_supplier.html', form=form)
