# src/models/inventory_item.py
from utils.create_app import db

class InventoryItem(db.Model):
    __tablename__ = 'inventory'
    product_id = db.Column(db.String, primary_key=True)
    product_name = db.Column(db.String(128), nullable=False)
    product_code = db.Column(db.String(64), nullable=False, index=True)
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

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_code': self.product_code,
            'description': self.description,
            'category_id': self.category_id,
            'brand_id': self.brand_id,
            'size': self.size,
            'color': self.color,
            'cost_price': str(self.cost_price),
            'markup': self.markup,
            'retail_price': str(self.retail_price),
            'product_status': self.product_status,
            'notes': self.notes,
            'supplier_id': self.supplier_id,
            'singles_in_stock': self.singles_in_stock,
            'cases_in_stock': self.cases_in_stock,
            'qty_per_case': self.qty_per_case,
            'condition': self.condition
        }