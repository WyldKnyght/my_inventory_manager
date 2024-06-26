# purchase_order_crud.py
# This script manages purchase orders and adds the data to the database

from datetime import datetime
from typing import List, Dict, Any
from db_utils import execute_db_operation
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class PurchaseOrderCRUD:
    @staticmethod
    def add_purchase_order(conn, cursor, supplier_id: int, order_number: str, items: List[Dict[str, Any]], shipping: float, taxes: float) -> int:
        """
        Add a new purchase order to the database.

        :param conn: Database connection
        :param cursor: Database cursor
        :param supplier_id: Supplier ID
        :param order_number: Order number
        :param items: List of items in the purchase order
        :param shipping: Shipping cost
        :param taxes: Taxes
        :return: Purchase ID of the newly created purchase order
        """
        conn.execute("BEGIN TRANSACTION")

        try:
            # Calculate subtotal
            subtotal = sum(item['cost_price'] * item['quantity'] for item in items)
            total_cost = subtotal + shipping + taxes

            # Insert into Purchases table
            purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO Purchases (SupplierID, OrderNumber, PurchaseDate, Subtotal, Shipping, Taxes, TotalCost)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (supplier_id, order_number, purchase_date, subtotal, shipping, taxes, total_cost))

            purchase_id = cursor.lastrowid

            # Process each item
            for item in items:
                product_id = PurchaseOrderCRUD._upsert_product(cursor, item)
                # Insert into PurchaseItems table
                cursor.execute("""
                    INSERT INTO PurchaseItems (PurchaseID, ProductID, Quantity, CostPrice, Notes)
                    VALUES (?, ?, ?, ?, ?)
                """, (purchase_id, product_id, item['quantity'], item['cost_price'], item['notes']))

            conn.commit()
            return purchase_id
        except Exception as e:
            conn.rollback()
            logger.error(f"Error adding purchase order: {e}", exc_info=True)
            raise e
        finally:
            conn.execute("END TRANSACTION")

    @staticmethod
    def _upsert_product(cursor, item: Dict[str, Any]) -> int:
        """
        Insert or update a product in the database.

        :param cursor: Database cursor
        :param item: Item data
        :return: Product ID
        """
        cursor.execute("SELECT ProductID FROM Products WHERE ProductName = ?", (item['product_name'],))
        if result := cursor.fetchone():
            product_id = result[0]
            # Update existing product
            cursor.execute("""
                UPDATE Products 
                SET Description = ?, CategoryID = ?, BrandID = ?, Size = ?, Color = ?, 
                    Condition = ?, CostPrice = ?, QtyInStock = QtyInStock + ?
                WHERE ProductID = ?
            """, (item['description'], item['category'], item['brand'], item['size'], 
                  item['color'], item['condition'], item['cost_price'], item['quantity'], product_id))
        else:
            # Insert new product
            cursor.execute("""
                INSERT INTO Products (ProductName, Description, CategoryID, BrandID, Size, Color, 
                                      Condition, CostPrice, QtyInStock)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (item['product_name'], item['description'], item['category'], item['brand'], 
                  item['size'], item['color'], item['condition'], item['cost_price'], item['quantity']))
            product_id = cursor.lastrowid
        return product_id

    @classmethod
    def create_purchase_order(cls, supplier_id: int, order_number: str, items: List[Dict[str, Any]], shipping: float, taxes: float) -> int:
        """
        Create a new purchase order.

        :param supplier_id: Supplier ID
        :param order_number: Order number
        :param items: List of items in the purchase order
        :param shipping: Shipping cost
        :param taxes: Taxes
        :return: Purchase ID of the newly created purchase order
        """
        return execute_db_operation(cls.add_purchase_order, supplier_id, order_number, items, shipping, taxes)