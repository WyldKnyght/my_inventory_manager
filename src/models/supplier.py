# src/models/supplier.py
from utils.create_app import db

class Supplier(db.Model):
    __tablename__ = 'supplier'
    supplier_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    contact_person = db.Column(db.String(128))
    address = db.Column(db.Text)
    phone = db.Column(db.String(15))  # Adjusted to string for flexibility in format
    email = db.Column(db.String(128))
    website = db.Column(db.String(128))
