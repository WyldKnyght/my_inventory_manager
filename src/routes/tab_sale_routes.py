# src/routes/tab_sale_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, session
from models.tab_inventory import InventoryTab
from models.tab_sale import SaleTab
from models.admin_customer import Customer
from forms.tab_sale_form import SaleFormTab
from utils.create_app import db
from utils.logging_colors import logger
from decimal import Decimal

sales_tab_routes = Blueprint('sales', __name__)

@sales_tab_routes.route('/sales', methods=['GET'])
def sales():
    return render_template('sales.html')

@sales_tab_routes.route('/sales/new', methods=['GET', 'POST'])
def new_sale():
    if 'current_sale' not in session:
        session['current_sale'] = []

    form = SaleFormTab()
    form.product_id.choices = [(p.product_id, p.product_name) for p in InventoryTab.query.all()]
    form.customer_id.choices = [(c.customer_id, c.customer_name) for c in Customer.query.all()]

    if form.validate_on_submit():
        if product := InventoryTab.query.get(form.product_id.data):
            item = {
                'product_id': product.product_id,
                'product_name': product.product_name,
                'quantity': form.quantity.data,
                'price': float(product.retail_price),
                'subtotal': float(product.retail_price) * form.quantity.data
            }
            session['current_sale'].append(item)
            session.modified = True
            flash('Item added to sale', 'success')
        else:
            flash('Product not found', 'error')

    total = sum(item['subtotal'] for item in session['current_sale'])
    return render_template('new_sale.html', form=form, items=session['current_sale'], total=total)

@sales_tab_routes.route('/sales/remove/<int:index>', methods=['POST'])
def remove_item(index):
    if 'current_sale' in session and 0 <= index < len(session['current_sale']):
        del session['current_sale'][index]
        session.modified = True
        flash('Item removed from sale', 'success')
    return redirect(url_for('sales.new_sale'))

@sales_tab_routes.route('/sales/finalize', methods=['POST'])
def finalize_sale():
    if 'current_sale' not in session or not session['current_sale']:
        flash('No items in the current sale', 'error')
        return redirect(url_for('sales.new_sale'))

    try:
        total = sum(item['subtotal'] for item in session['current_sale'])
        sale = SaleTab(
            customer_id=request.form.get('customer_id'),
            total_cost=Decimal(str(total)),
            # Add other necessary fields
        )
        db.session.add(sale)

        for item in session['current_sale']:
            if product := InventoryTab.query.get(item['product_id']):
                if product.singles_in_stock >= item['quantity']:
                    product.singles_in_stock -= item['quantity']
                else:
                    raise ValueError(f"Insufficient stock for {product.product_name}")

        db.session.commit()
        session.pop('current_sale', None)
        flash('Sale finalized successfully', 'success')
        logger.info(f"Sale finalized: {sale.sale_id}")
        return redirect(url_for('sales.sales'))

    except Exception as e:
        db.session.rollback()
        flash(f'Error finalizing sale: {str(e)}', 'error')
        logger.error(f"Error finalizing sale: {str(e)}")
        return redirect(url_for('sales.new_sale'))

@sales_tab_routes.route('/api/sales', methods=['GET'])
def api_sales():
    sales = SaleTab.query.all()
    return jsonify([sale.to_dict() for sale in sales])

@sales_tab_routes.route('/api/sales/<string:sale_id>', methods=['GET'])
def api_sale(sale_id):
    sale = SaleTab.query.get_or_404(sale_id)
    return jsonify(sale.to_dict())