# src\routes\__init__.py
from .tab_admin_routes import admin_tab_routes
from .tab_inventory_routes import inventory_tab_routes
from .tab_purchase_routes import purchase_tab_routes
from .tab_report_routes import report_tab_routes
from .tab_sale_routes import sales_tab_routes
from .admin_brand_routes import brand_routes
from .admin_category_routes import category_routes
from .admin_customer_routes import customer_routes
from .admin_inventory_routes import inventory_routes
from .admin_inventory_status_routes import inventory_status_routes
from .admin_supplier_routes import supplier_routes

__all__ = [
    'tab_admin_routes', 
    'tab_inventory_routes',
    'tab_purchase_routes', 
    'tab_report_routes', 
    'tab_sale_routes', 
    'admin_brand_routes', 
    'admin_category_routes', 
    'admin_customer_routes',
    'admin_inventory_routes', 
    'admin_inventory_status_routes', 
    'admin_supplier_routes' 
    ]
