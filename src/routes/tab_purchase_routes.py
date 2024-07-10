# src/routes/tab_purchase_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, session
from decimal import Decimal
from forms.tab_purchase_form import PurchaseTabForm
from models.admin_inventory import InventoryItem
from models.admin_category import Category
from models.admin_supplier import Supplier
from models.admin_brand import Brand
from models.admin_inventory_status import InventoryStatus
from models.tab_purchase import PurchaseTab
from utils.create_app import db
from utils.logging_colors import logger

purchase_tab_routes = Blueprint('purchases', __name__)

@purchase_tab_routes.route('/purchases', methods=['GET'])
def purchases():
    page = request.args.get('page', 1, type=int)
    purchases = PurchaseTabForm.query.paginate(page=page, per_page=20)
    return render_template('purchases.html', purchases=purchases)

@purchase_tab_routes.route('/purchases/new', methods=['GET', 'POST'])
def new_purchase():
    if 'current_purchase' not in session:
        session['current_purchase'] = []

    form = PurchaseTabForm()
    form.product_id.choices = [(p.product_id, p.product_name) for p in InventoryItem.query.all()]
    form.supplier_id.choices = [(s.supplier_id, s.name) for s in Supplier.query.all()]

    if form.validate_on_submit():
        if product := InventoryItem.query.get(form.product_id.data):
            item = {
                'product_id': product.product_id,
                'product_name': product.product_name,
                'quantity': form.quantity.data,
                'cost_price': float(form.cost_price.data),
                'subtotal': float(form.cost_price.data) * form.quantity.data
            }
            session['current_purchase'].append(item)
            session.modified = True
            flash('Item added to purchase order', 'success')
        else:
            flash('Product not found', 'error')

    total = sum(item['subtotal'] for item in session['current_purchase'])
    return render_template('new_purchase.html', form=form, items=session['current_purchase'], total=total)

@purchase_tab_routes.route('/purchases/remove/<int:index>', methods=['POST'])
def remove_item(index):
    if 'current_purchase' in session and 0 <= index < len(session['current_purchase']):
        del session['current_purchase'][index]
        session.modified = True
        flash('Item removed from purchase order', 'success')
    return redirect(url_for('purchases.new_purchase'))

@purchase_tab_routes.route('/purchases/finalize', methods=['POST'])
def finalize_purchase():
    if 'current_purchase' not in session or not session['current_purchase']:
        flash('No items in the current purchase order', 'error')
        return redirect(url_for('purchases.new_purchase'))

    try:
        total_cost = sum(item['subtotal'] for item in session['current_purchase'])
        purchase = PurchaseTabForm(
            supplier_id=request.form.get('supplier_id'),
            purchase_order=f"PO-{PurchaseTab.query.count() + 1:05d}",
            total_cost=Decimal(str(total_cost)),
            # Add other necessary fields
        )
        db.session.add(purchase)

        for item in session['current_purchase']:
            if product := InventoryItem.query.get(item['product_id']):
                product.singles_in_stock += item['quantity']
        db.session.commit()
        session.pop('current_purchase', None)
        flash('Purchase order finalized successfully', 'success')
        logger.info(f"Purchase order finalized: {purchase.purchase_id}")
        return redirect(url_for('purchases.purchases'))

    except Exception as e:
        db.session.rollback()
        flash(f'Error finalizing purchase order: {str(e)}', 'error')
        logger.error(f"Error finalizing purchase order: {str(e)}")
        return redirect(url_for('purchases.new_purchase'))

@purchase_tab_routes.route('/api/purchases', methods=['GET'])
def api_purchases():
    purchases = PurchaseTab.query.all()
    return jsonify([purchase.to_dict() for purchase in purchases])

@purchase_tab_routes.route('/api/purchases/<string:purchase_id>', methods=['GET'])
def api_purchase(purchase_id):
    purchase = PurchaseTab.query.get_or_404(purchase_id)
    return jsonify(purchase.to_dict())