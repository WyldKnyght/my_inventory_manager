# src\forms\__init__.py
from .admin_brand_form import BrandForm
from .admin_category_form import CategoryForm
from .admin_inventory_status_form import InventoryStatusForm
from .admin_inventory_form import InventoryForm
from .admin_supplier_form import SupplierForm
from .tab_inventory_form import InventoryTabForm
from .tab_purchases_form import PurchasesTabForm
from .tab_sales_form import SalesTabForm
from .tab_reports_form import ReportsTabForm

__all__ = [ 
            'InventoryTabForm',
            'PurchasesTabForm',
            'SalesTabForm',
            'ReportsTabForm',
            'BrandForm', 
            'CategoryForm', 
            'InventoryStatusForm', 
            'InventoryForm', 
            'SupplierForm'
            ]