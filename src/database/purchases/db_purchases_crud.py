# db_purchases_crud.py
# Defines a class `PurchasesCRUD` for interacting with the SQLite database.

from database.db_base_crud import BaseCRUD
from typing import Dict, List, Any

class PurchasesCRUD(BaseCRUD):
    def create_purchase(self, purchase_data: Dict[str, Any]) -> int:
        """Create a new purchase in the database."""
        return self.execute_db_operation(self._create_purchase, purchase_data)

    def get_purchase(self, id: int) -> Dict[str, Any]:
        """Retrieve a purchase from the database by ID."""
        return self.execute_db_operation(self._get_purchase, id)

    def update_purchase(self, id: int, purchase_data: Dict[str, Any]) -> None:
        """Update an existing purchase in the database."""
        return self.execute_db_operation(self._update_purchase, id, purchase_data)

    def delete_purchase(self, id: int) -> None:
        """Delete a purchase from the database."""
        return self.execute_db_operation(self._delete_purchase, id)

    def get_all_purchases(self) -> List[Dict[str, Any]]:
        """Retrieve all purchases from the database."""
        return self.execute_db_operation(self._get_all_purchases)

    def add_purchase_order(self, supplier_id: int, order_number: str, items: List[Dict[str, Any]], shipping: float, taxes: float) -> int:
        """Add a new purchase order to the database."""
        return self.execute_db_operation(self._add_purchase_order, supplier_id, order_number, items, shipping, taxes)

    @staticmethod
    def _create_purchase(conn, cursor, purchase_data):
        cursor.execute("""
            INSERT INTO Purchases (PurchaseOrderNumber, OrderNumber, PurchaseDate, ShippingDate, ShippingTrackingNumber, 
                                   SupplierID, PaymentMethod, Currency, ExchangeRate, CostPrice, Discount, Shipping, 
                                   Taxes, TotalCost)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (purchase_data['PurchaseOrderNumber'], purchase_data['OrderNumber'], purchase_data['PurchaseDate'],
              purchase_data['ShippingDate'], purchase_data['ShippingTrackingNumber'], purchase_data['SupplierID'],
              purchase_data['PaymentMethod'], purchase_data['Currency'], purchase_data['ExchangeRate'],
              purchase_data['CostPrice'], purchase_data['Discount'], purchase_data['Shipping'],
              purchase_data['Taxes'], purchase_data['TotalCost']))
        return cursor.lastrowid

    @staticmethod
    def _get_purchase(conn, cursor, id):
        cursor.execute("SELECT * FROM Purchases WHERE PurchaseID = ?", (id,))
        return cursor.fetchone()

    @staticmethod
    def _update_purchase(conn, cursor, id, purchase_data):
        cursor.execute("""
            UPDATE Purchases
            SET PurchaseOrderNumber = ?, OrderNumber = ?, PurchaseDate = ?, ShippingDate = ?, 
                ShippingTrackingNumber = ?, SupplierID = ?, PaymentMethod = ?, Currency = ?, 
                ExchangeRate = ?, CostPrice = ?, Discount = ?, Shipping = ?, Taxes = ?, TotalCost = ?
            WHERE PurchaseID = ?
        """, (purchase_data['PurchaseOrderNumber'], purchase_data['OrderNumber'], purchase_data['PurchaseDate'],
              purchase_data['ShippingDate'], purchase_data['ShippingTrackingNumber'], purchase_data['SupplierID'],
              purchase_data['PaymentMethod'], purchase_data['Currency'], purchase_data['ExchangeRate'],
              purchase_data['CostPrice'], purchase_data['Discount'], purchase_data['Shipping'],
              purchase_data['Taxes'], purchase_data['TotalCost'], id))

    @staticmethod
    def _delete_purchase(conn, cursor, id):
        cursor.execute("DELETE FROM Purchases WHERE PurchaseID = ?", (id,))

    @staticmethod
    def _get_all_purchases(conn, cursor):
        cursor.execute("SELECT * FROM Purchase")
        return cursor.fetchall()

    @staticmethod
    def _add_purchase_order(conn, cursor, supplier_id, order_number, items, shipping, taxes):
        # Calculate subtotal and total cost
        subtotal = sum(item['cost_price'] * item['quantity'] for item in items)
        total_cost = subtotal + shipping + taxes

        # Insert into Purchases table
        cursor.execute("""
            INSERT INTO Purchases (SupplierID, OrderNumber, PurchaseDate, Subtotal, Shipping, Taxes, TotalCost)
            VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?, ?, ?)
        """, (supplier_id, order_number, subtotal, shipping, taxes, total_cost))
        purchase_id = cursor.lastrowid

        # Insert items into PurchaseItems table
        for item in items:
            cursor.execute("""
                INSERT INTO PurchaseItems (PurchaseID, ProductName, Description, CategoryID, BrandID, 
                                        Size, Color, Condition, CostPrice, Quantity, Notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (purchase_id, item['product_name'], item['description'], item['category'], item['brand'],
                item['size'], item['color'], item['condition'], item['cost_price'], item['quantity'], item['notes']))

        return purchase_id
