# src/configs/database_config.py
from utils.custom_logging import logger

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
    primary_key = primary_keys.get(table_name, "id")
    logger.debug(f"Retrieved primary key for {table_name}: {primary_key}")
    return primary_key

def get_id_columns():
    """Return a dictionary of table names and their corresponding ID column names."""
    return {
        "Categories": "category_id",
        "UnitTypes": "unit_type_id",
        "Catalog": "item_id",
        "Vendors": "vendor_id",
        "Customers": "customer_id",
        "Accounts": "account_id",
        "Settings": "setting_id",
        "Sales": "sales_id",
        "Product_Sales": "product_sales_id",
        "Purchases": "purchase_id",
        "Product_Purchases": "product_purchase_id",
        "Expenses": "expense_id"
    }