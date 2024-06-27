# src\routes\__init__.py
from .inventory_routes import inventory_routes
from .category_routes import category_routes
from .brand_routes import brand_routes
from .supplier_routes import supplier_routes
from .inventory_status_routes import inventory_status_routes
from .admin_routes import admin_routes

__all__ = ['inventory_routes', 'category_routes', 'brand_routes', 'supplier_routes', 'inventory_status_routes', 'admin_routes']
