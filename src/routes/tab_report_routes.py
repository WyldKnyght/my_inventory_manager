# src/routes/tab_report_routes.py
from flask import Blueprint, render_template, request, jsonify, send_file
from utils.create_app import db
from models.tab_inventory import InventoryTab
from models.tab_sale import Sale
from models.tab_purchase import Purchase
from utils.logging_colors import logger
from sqlalchemy import func
from datetime import datetime, timedelta
import io
import csv

report_tab_routes = Blueprint('report', __name__)

@report_tab_routes.route('/reports', methods=['GET'])
def reports():
    return render_template('reports.html')

@report_tab_routes.route('/reports/inventory', methods=['GET'])
def inventory_report():
    inventory = InventoryTab.query.all()
    total_value = sum(item.cost_price * item.singles_in_stock for item in inventory)
    return render_template('inventory_report.html', inventory=inventory, total_value=total_value)

@report_tab_routes.route('/reports/sales', methods=['GET'])
def sales_report():
    start_date = request.args.get('start_date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', default=datetime.now().strftime('%Y-%m-%d'))
    
    sales = Sale.query.filter(Sale.order_date.between(start_date, end_date)).all()
    total_sales = sum(sale.total_cost for sale in sales)
    return render_template('sales_report.html', sales=sales, total_sales=total_sales, start_date=start_date, end_date=end_date)

@report_tab_routes.route('/reports/purchases', methods=['GET'])
def purchases_report():
    start_date = request.args.get('start_date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', default=datetime.now().strftime('%Y-%m-%d'))
    
    purchases = Purchase.query.filter(Purchase.purchase_date.between(start_date, end_date)).all()
    total_purchases = sum(purchase.total_cost for purchase in purchases)
    return render_template('purchases_report.html', purchases=purchases, total_purchases=total_purchases, start_date=start_date, end_date=end_date)

@report_tab_routes.route('/reports/profit_loss', methods=['GET'])
def profit_loss_report():
    start_date = request.args.get('start_date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', default=datetime.now().strftime('%Y-%m-%d'))
    
    sales = db.session.query(func.sum(Sale.total_cost)).filter(Sale.order_date.between(start_date, end_date)).scalar() or 0
    purchases = db.session.query(func.sum(Purchase.total_cost)).filter(Purchase.purchase_date.between(start_date, end_date)).scalar() or 0
    profit = sales - purchases
    
    return render_template('profit_loss_report.html', sales=sales, purchases=purchases, profit=profit, start_date=start_date, end_date=end_date)

@report_tab_routes.route('/reports/low_stock', methods=['GET'])
def low_stock_report():
    threshold = request.args.get('threshold', default=10, type=int)
    low_stock_items = InventoryTab.query.filter(InventoryTab.singles_in_stock < threshold).all()
    return render_template('low_stock_report.html', items=low_stock_items, threshold=threshold)

@report_tab_routes.route('/reports/export_inventory', methods=['GET'])
def export_inventory():
    inventory = InventoryTab.query.all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Product ID', 'Product Name', 'Quantity', 'Cost Price', 'Retail Price'])
    for item in inventory:
        writer.writerow([item.product_id, item.product_name, item.singles_in_stock, item.cost_price, item.retail_price])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='inventory_report.csv'
    )

@report_tab_routes.route('/api/reports/inventory', methods=['GET'])
def api_inventory_report():
    inventory = InventoryTab.query.all()
    return jsonify([item.to_dict() for item in inventory])

@report_tab_routes.route('/api/reports/sales', methods=['GET'])
def api_sales_report():
    start_date = request.args.get('start_date', default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', default=datetime.now().strftime('%Y-%m-%d'))
    
    sales = Sale.query.filter(Sale.order_date.between(start_date, end_date)).all()
    return jsonify([sale.to_dict() for sale in sales])