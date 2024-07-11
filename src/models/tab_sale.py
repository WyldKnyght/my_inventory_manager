# src/models/tab_sale.py
from create_app import db
from datetime import datetime, timezone

class SaleTab(db.Model):
    __tablename__ = 'sale'
    __table_args__ = {'extend_existing': True}
    sale_id = db.Column(db.String, primary_key=True)
    sales_order = db.Column(db.String(128), unique=True)
    customer_id = db.Column(db.String, db.ForeignKey('customer.customer_id'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    ship_delivery_pickup_date = db.Column(db.Date)
    total_cost = db.Column(db.Numeric(10, 2))
    shipping = db.Column(db.Numeric(10, 2))
    taxes = db.Column(db.Numeric(10, 2))

    customer = db.relationship('Customer', backref='sales')
    items = db.relationship('SaleItem', back_populates='sale', cascade='all, delete-orphan')

    def __init__(self, customer_id, total_cost, shipping=0, taxes=0):
        self.sale_id = f"SALE-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"
        self.sales_order = f"SO-{SaleTab.query.count() + 1:05d}"
        self.customer_id = customer_id
        self.total_cost = total_cost
        self.shipping = shipping
        self.taxes = taxes

    def to_dict(self):
        return {
            'sale_id': self.sale_id,
            'sales_order': self.sales_order,
            'customer_id': self.customer_id,
            'order_date': self.order_date.isoformat(),
            'ship_delivery_pickup_date': self.ship_delivery_pickup_date.isoformat() if self.ship_delivery_pickup_date else None,
            'total_cost': str(self.total_cost),
            'shipping': str(self.shipping),
            'taxes': str(self.taxes),
            'items': [item.to_dict() for item in self.items]
        }