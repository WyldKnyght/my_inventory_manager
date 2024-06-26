# src/models/inventory_status.py
from utils.create_app import db

class InventoryStatus(db.Model):
    __tablename__ = 'inventory_status'
    inventory_status_id = db.Column(db.String, primary_key=True)
    status_name = db.Column(db.String(128), nullable=False)
    status_prefix = db.Column(db.String(4), nullable=False)
