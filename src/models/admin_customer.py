# src/models/admin_customers.py
from create_app import db

class Customer(db.Model):
    __tablename__ = 'customer'
    __table_args__ = {'extend_existing': True}
    customer_id = db.Column(db.String, primary_key=True)
    customer_name = db.Column(db.String(128), nullable=False)
    contact_information = db.Column(db.Text)

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'contact_information': self.contact_information
        }
