# src/models/sales.py
from utils.create_app import db

class SaleTab(db.Model):
    __tablename__ = 'sale'
    __table_args__ = {'extend_existing': True}
    sale_id = db.Column(db.String, primary_key=True)
    sales_order = db.Column(db.String(128), unique=True)
    product_id = db.Column(db.String, db.ForeignKey('inventory.product_id'))
    order_date = db.Column(db.Date)
    ship_delivery_pickup_date = db.Column(db.Date)
    customer_id = db.Column(db.String, db.ForeignKey('customer.customer_id'))
    quantity = db.Column(db.Integer)
    retail_price = db.Column(db.Numeric(10, 2))
    shipping = db.Column(db.Numeric(10, 2))
    taxes = db.Column(db.Numeric(10, 2))
    total_cost = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            'sale_id': self.sale_id,
            'sales_order': self.sales_order,
            'product_id': self.product_id,
            'order_date': str(self.order_date),
            'ship_delivery_pickup_date': str(self.ship_delivery_pickup_date),
            'customer_id': self.customer_id,
            'quantity': self.quantity,
            'retail_price': str(self.retail_price),
            'shipping': str(self.shipping),
            'taxes': str(self.taxes),
            'total_cost': str(self.total_cost)
        }
