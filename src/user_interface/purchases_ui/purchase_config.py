# purchase_config.py

DB_CONFIG = {
    'database': 'inventory.db',
    'host': 'localhost',
    'user': 'user',
    'password': 'password'
}

PURCHASE_COLUMNS = [
    'Purchase ID', 'Purchase Order #', 'Order Number', 'Product ID', 'Purchase Date', 
    'Shipping Date', 'Shipping Tracking Number', 'Supplier ID', 'Singles Quantity', 
    'Cases Quantity', 'Product Status', 'Payment Method', 'Currency', 'Exchange Rate', 
    'Cost Price', 'Discount', 'Shipping', 'Taxes', 'Total Cost'
]

PRODUCT_COLUMNS = [
    'Product ID', 'Product Name', 'Product Code', 'Description', 'Category ID', 
    'Brand ID', 'Size', 'Color', 'Condition', 'Cost Price', 'Markup', 'Retail Price', 
    'Product Status', 'Notes', 'Supplier ID', 'Singles In Stock', 'Cases In Stock', 
    'Qty/Case', 'Total In Stock', 'Total Number of Sales'
]

CATEGORY_COLUMNS = ['Category ID', 'Category Name', 'Category Prefix', 'Parent Category ID', 'Sub-Categories Name']

BRAND_COLUMNS = ['Brand ID', 'Brand Name']

SUPPLIER_COLUMNS = [
    'Supplier ID', 'Name', 'Contact Person', 'Address', 'Phone', 'Email', 'Website'
]

SALES_COLUMNS = [
    'Sale ID', 'Sales Order #', 'Product ID', 'Order Date', 'Ship/Delivery/Pickup Date', 
    'Customer ID', 'Quantity', 'Retail Price', 'Shipping', 'Taxes', 'Total Cost'
]

CUSTOMER_COLUMNS = ['Customer ID', 'Customer Name', 'Contact Information']

REPORT_COLUMNS = [
    'Report ID', 'Date', 'Sales Total', 'Profit Total', 'Balance Sheet', 'Stock waiting to be received'
]

INVENTORY_STATUS_COLUMNS = ['Inventory Status ID', 'Status Name', 'Status Prefix']
