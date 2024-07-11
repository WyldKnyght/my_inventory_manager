# src/models/brand.py
from create_app import db

class Brand(db.Model):
    __tablename__ = 'brand'
    brand_id = db.Column(db.String, primary_key=True)
    brand_name = db.Column(db.String(128), nullable=False)
    inventory_items = db.relationship('InventoryItem', backref='brand', lazy=True)

    def to_dict(self):
        return {
            'brand_id': self.brand_id,
            'brand_name': self.brand_name
        }