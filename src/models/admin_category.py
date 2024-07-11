# src/models/category.py
from create_app import db

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(128), nullable=False)
    category_prefix = db.Column(db.String(4), nullable=False)
    parent_category_id = db.Column(db.String, db.ForeignKey('category.category_id'))
    sub_categories_name = db.Column(db.String(128))
    sub_categories = db.relationship('Category', backref=db.backref('parent_category', remote_side=[category_id]), lazy=True)
    inventory_items = db.relationship('InventoryItem', backref='category', lazy=True)

    def to_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_prefix': self.category_prefix,
            'parent_category_id': self.parent_category_id,
            'sub_categories_name': self.sub_categories_name
        }