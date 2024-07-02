# src\routes\__init__.py
from .admin_inventory_routes import inventory_routes
from .admin_category_routes import category_routes
from .admin_brand_routes import brand_routes
from .admin_supplier_routes import supplier_routes
from .admin_inventory_status_routes import inventory_status_routes
from .admin_routes import admin_routes

__all__ = ['admin_inventory_routes', 'admin_category_routes', 'admin_brand_routes', 'admin_supplier_routes', 'admin_inventory_status_routes', 'admin_routes']
