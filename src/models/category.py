# src/models/category.py
from utils.create_app import db

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(128), nullable=False)
    category_prefix = db.Column(db.String(4), nullable=False)
    parent_category_id = db.Column(db.String, db.ForeignKey('category.category_id'))
    sub_categories_name = db.Column(db.String(128))
