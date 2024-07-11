# src/models/inventory_status.py
from create_app import db

class InventoryStatus(db.Model):
    __tablename__ = 'inventory_status'
    inventory_status_id = db.Column(db.String, primary_key=True)
    status_name = db.Column(db.String(128), nullable=False)
    status_prefix = db.Column(db.String(4), nullable=False)
    inventory_items = db.relationship('InventoryItem', backref='inventory_status', lazy=True)

    def to_dict(self):
        return {
            'inventory_status_id': self.inventory_status_id,
            'status_name': self.status_name,
            'status_prefix': self.status_prefix
        }