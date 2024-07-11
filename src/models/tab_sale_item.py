# src/models/tab_sale_item.py
from utils.create_app import db

class SaleItem(db.Model):
    __tablename__ = 'sale_item'
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.String, db.ForeignKey('sale.sale_id'), nullable=False)
    product_id = db.Column(db.String, db.ForeignKey('inventory.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)

    sale = db.relationship('SaleTab', back_populates='items')
    product = db.relationship('InventoryTab')

    def __init__(self, sale_id, product_id, quantity, price):
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.subtotal = quantity * price

    def to_dict(self):
        return {
            'id': self.id,
            'sale_id': self.sale_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': str(self.price),
            'subtotal': str(self.subtotal)
        }