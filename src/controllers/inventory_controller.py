# src/controllers/inventory_controller.py

from utils.database import execute_query, fetch_all
import logging

logger = logging.getLogger(__name__)

class InventoryController:
    def get_all_products(self):
        """Retrieve all products with their category IDs."""
        query = """
        SELECT 
            product_number, 
            product_name, 
            category_id, 
            product_description, 
            cost_price, 
            selling_price, 
            quantity 
        FROM 
            products;
        """
        try:
            return fetch_all(query)
        except Exception as e:
            logger.error(f"Failed to fetch products: {e}")
            return []

    def add_product(self, product_data):
        """Create a new product in the products table."""
        query = f"""
        INSERT INTO products (
            category_id, product_number, unit_type, returnable, dimensions, weight, 
            company_id, brand_id, upc, mpn, ean, isbn, selling_price, 
            sales_account, sales_description, cost_price, purchase_account, 
            purchase_description, preferred_vendor_id
        ) VALUES ({', '.join(['?' for _ in product_data])})
        """
        try:
            execute_query(query, product_data)
        except Exception as e:
            logger.error(f"Failed to add product: {e}")

    def modify_product(self, product_id, updated_data):
        """Update an existing product in the products table."""
        query = """
        UPDATE products
        SET 
            type = ?, product_number = ?, unit_type = ?, returnable = ?, dimensions = ?, 
            weight = ?, company_id = ?, brand_id = ?, upc = ?, mpn = ?, ean = ?, 
            isbn = ?, selling_price = ?, sales_account = ?, sales_description = ?, 
            cost_price = ?, purchase_account = ?, purchase_description = ?, 
            preferred_vendor_id = ?
        WHERE 
            product_id = ?
        """
        try:
            execute_query(query, updated_data + (product_id,))
        except Exception as e:
            logger.error(f"Failed to modify product with ID {product_id}: {e}")

    def remove_product(self, product_id):
        """Delete a product from the products table."""
        query = "DELETE FROM products WHERE product_id = ?"
        try:
            execute_query(query, (product_id,))
        except Exception as e:
            logger.error(f"Failed to remove product with ID {product_id}: {e}")