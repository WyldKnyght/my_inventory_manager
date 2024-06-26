# src/models/brand.py
from utils.create_app import db

class Brand(db.Model):
    __tablename__ = 'brand'
    brand_id = db.Column(db.String, primary_key=True)
    brand_name = db.Column(db.String(128), nullable=False)
