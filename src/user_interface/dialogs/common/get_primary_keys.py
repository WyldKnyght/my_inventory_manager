# src/user_interface/dialogs/common/get_primary_keys.py
def get_primary_key(table_name):
    """Return the primary key column name for the specified table."""
    primary_keys = {
        "Categories": "category_id",
        "Vendors": "vendor_id",
        "Customers": "customer_id",
        "Accounts": "account_id",
        "Settings": "setting_id",
        "UnitTypes": "unit_type_id",
        "Catalog": "item_id",
        "Sales": "sales_id",
        "Product_Sales": "product_sales_id",
        "Purchases": "purchase_id",
        "Product_Purchases": "product_purchase_id",
        "Expenses": "expense_id"
    }
    return primary_keys.get(table_name, "id")
