# src/routes/customer_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from utils.create_app import db
from models.customer import Customer
from forms.customer_form import CustomerForm
from utils.logging_colors import logger

customer_routes = Blueprint('customer', __name__)

@customer_routes.route('/customers', methods=['GET'])
def customers():
    page = request.args.get('page', 1, type=int)
    customers = Customer.query.paginate(page=page, per_page=20)
    logger.info(f"Customers page {page} accessed")
    return render_template('customers.html', customers=customers)

@customer_routes.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        try:
            customer = Customer(
                customer_id=form.customer_id.data,
                customer_name=form.customer_name.data,
                contact_information=form.contact_information.data
            )
            db.session.add(customer)
            db.session.commit()
            flash('Customer added successfully!', 'success')
            logger.info(f"Customer added: {customer.customer_name}")
            return redirect(url_for('customer.customers'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding customer: {str(e)}', 'error')
            logger.error(f"Error adding customer: {str(e)}")
    return render_template('add_customer.html', form=form)

@customer_routes.route('/edit_customer/<string:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    form = CustomerForm(obj=customer)
    if form.validate_on_submit():
        try:
            form.populate_obj(customer)
            db.session.commit()
            flash('Customer updated successfully!', 'success')
            logger.info(f"Customer updated: {customer.customer_name}")
            return redirect(url_for('customer.customers'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating customer: {str(e)}', 'error')
            logger.error(f"Error updating customer: {str(e)}")
    return render_template('edit_customer.html', form=form, customer=customer)

@customer_routes.route('/delete_customer/<string:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    try:
        db.session.delete(customer)
        db.session.commit()
        flash('Customer deleted successfully!', 'success')
        logger.info(f"Customer deleted: {customer.customer_name}")
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting customer: {str(e)}', 'error')
        logger.error(f"Error deleting customer: {str(e)}")
    return redirect(url_for('customer.customers'))

@customer_routes.route('/api/customers', methods=['GET'])
def api_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers])

@customer_routes.route('/api/customers/<string:customer_id>', methods=['GET'])
def api_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict())