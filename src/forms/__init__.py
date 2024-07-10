# src\forms\__init__.py
from .admin_brand_form import BrandForm
from .admin_category_form import CategoryForm
from .admin_customer_form import CustomerForm
from .admin_inventory_status_form import InventoryStatusForm
from .admin_inventory_form import InventoryForm
from .admin_supplier_form import SupplierForm
from .tab_inventory_form import InventoryTabForm
from .tab_purchase_form import PurchaseTabForm
from .tab_sale_form import SaleTabForm
from .tab_report_form import ReportTabForm

__all__ = [ 
            'InventoryTabForm',
            'PurchaseTabForm',
            'SaleTabForm',
            'ReportTabForm',
            'BrandForm', 
            'CategoryForm',
            'CustomerForm', 
            'InventoryStatusForm', 
            'InventoryForm', 
            'SupplierForm'
            ]