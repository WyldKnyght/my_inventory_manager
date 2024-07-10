# src/models/purchases.py
from utils.create_app import db

class PurchaseTab(db.Model):
    __tablename__ = 'purchase'
    __table_args__ = {'extend_existing': True}
    purchase_id = db.Column(db.String, primary_key=True)
    purchase_order = db.Column(db.String(128))
    order_number = db.Column(db.String(128))
    product_id = db.Column(db.String, db.ForeignKey('inventory.product_id'))
    purchase_date = db.Column(db.Date)
    shipping_date = db.Column(db.Date)
    shipping_tracking_number = db.Column(db.String(128))
    supplier_id = db.Column(db.String, db.ForeignKey('supplier.supplier_id'))
    singles_quantity = db.Column(db.Integer)
    cases_quantity = db.Column(db.Integer)
    product_status = db.Column(db.String, db.ForeignKey('inventory_status.inventory_status_id'))
    payment_method = db.Column(db.String(64))
    currency = db.Column(db.String(3))
    exchange_rate = db.Column(db.Numeric(10, 4))
    cost_price = db.Column(db.Numeric(10, 2))
    discount = db.Column(db.Numeric(10, 2))
    shipping = db.Column(db.Numeric(10, 2))
    taxes = db.Column(db.Numeric(10, 2))
    total_cost = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            'purchase_id': self.purchase_id,
            'purchase_order': self.purchase_order,
            'order_number': self.order_number,
            'product_id': self.product_id,
            'purchase_date': str(self.purchase_date),
            'shipping_date': str(self.shipping_date),
            'shipping_tracking_number': self.shipping_tracking_number,
            'supplier_id': self.supplier_id,
            'singles_quantity': self.singles_quantity,
            'cases_quantity': self.cases_quantity,
            'product_status': self.product_status,
            'payment_method': self.payment_method,
            'currency': self.currency,
            'exchange_rate': str(self.exchange_rate),
            'cost_price': str(self.cost_price),
            'discount': str(self.discount),
            'shipping': str(self.shipping),
            'taxes': str(self.taxes),
            'total_cost': str(self.total_cost)
        }