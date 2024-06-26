# src/models/inventory_item.py
from utils.create_app import db

class InventoryItem(db.Model):
    __tablename__ = 'inventory'
    product_id = db.Column(db.String, primary_key=True)
    product_name = db.Column(db.String(128), nullable=False)
    product_code = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.String, db.ForeignKey('category.category_id'))
    brand_id = db.Column(db.String, db.ForeignKey('brand.brand_id'))
    size = db.Column(db.String(64))
    color = db.Column(db.String(64))
    cost_price = db.Column(db.Numeric(10, 2))
    markup = db.Column(db.Integer)
    retail_price = db.Column(db.Numeric(10, 2))
    product_status = db.Column(db.String, db.ForeignKey('inventory_status.inventory_status_id'))
    notes = db.Column(db.Text)
    supplier_id = db.Column(db.String, db.ForeignKey('supplier.supplier_id'))
    singles_in_stock = db.Column(db.Integer)
    cases_in_stock = db.Column(db.Integer)
    qty_per_case = db.Column(db.Integer)
    condition = db.Column(db.String(64))
