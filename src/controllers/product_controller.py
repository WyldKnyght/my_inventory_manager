# src/controllers/product_controller.py
from utils.database import get_connection, execute_query

class ProductController:
    def get_all_products(self):
        """Retrieve all products with their category IDs."""
        query = """
        SELECT 
            product_number, 
            product_name, 
            product_category_id,  -- Retrieve the category ID
            product_description, 
            cost_price, 
            selling_price, 
            quantity 
        FROM 
            Products;
        """
        connection = get_connection()  # Get the database connection
        cursor = connection.cursor()
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()
        connection.close()

        # Convert to a list of dictionaries for easier access
        return [
            {
                'product_number': product[0],
                'product_name': product[1],
                'product_category_id': product[2],  # Use category ID
                'product_description': product[3],
                'cost_price': product[4],
                'selling_price': product[5],
                'quantity': product[6]
            }
            for product in products
        ]

    def create_product(self, product_data):
        """Create a new product in the products table."""
        query = """
        INSERT INTO products (product_category_id, product_number, unit_type, returnable, dimensions, weight, 
                            manufacturer_id, brand_id, upc, mpn, ean, isbn, selling_price, 
                            sales_account, sales_description, cost_price, purchase_account, 
                            purchase_description, preferred_vendor_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        execute_query(query, product_data)

    def update_product(self, product_id, updated_data):
        """Update an existing product in the products table."""
        query = """
        UPDATE products
        SET type = ?, product_number = ?, unit_type = ?, returnable = ?, dimensions = ?, 
            weight = ?, manufacturer_id = ?, brand_id = ?, upc = ?, mpn = ?, ean = ?, 
            isbn = ?, selling_price = ?, sales_account = ?, sales_description = ?, 
            cost_price = ?, purchase_account = ?, purchase_description = ?, 
            preferred_vendor_id = ?
        WHERE product_id = ?
        """
        execute_query(query, updated_data + (product_id,))

    def delete_product(self, product_id):
        """Delete an product from the products table."""
        query = "DELETE FROM products WHERE product_id = ?"
        execute_query(query, (product_id,))