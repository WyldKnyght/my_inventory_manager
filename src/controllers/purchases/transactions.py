# src/controllers/purchases/transactions.py

from typing import Dict, Any, List
from controllers.database_controller import DatabaseController
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.config_manager import config_manager

class PurchaseTransactions:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.queries = config_manager.get('database.queries.purchases', {})
        logger.info("Initialized PurchaseTransactions")

    @ErrorHandler.handle_errors()
    def execute_purchase_transaction(self, operation: str, purchase_data: Dict[str, Any]) -> None:
        """Execute a purchase transaction (add, update, or delete)."""
        operations = {
            'add': self._add_purchase,
            'update': self._update_purchase,
            'delete': self._delete_purchase
        }
        
        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")

        try:
            with self.db_controller.get_connection() as conn:
                cursor = conn.cursor()
                operations[operation](cursor, purchase_data)
                conn.commit()
                logger.info(f"Executed {operation} transaction for purchase")
        except Exception as e:
            conn.rollback()
            logger.error(f"Transaction failed: {str(e)}")
            raise

    @ErrorHandler.handle_errors()
    def _add_purchase(self, cursor, purchase_data: Dict[str, Any]) -> None:
        """Add a new purchase and its associated product purchases."""
        purchase_query = self.queries.get('add_purchase', """
        INSERT INTO Purchases (vendor_id, vendor_order_number, purchase_order_number, purchase_date, purchase_amount,
                                taxes, discount, customs_fees, currency, purchase_status, payment_method, shipping_cost,
                                shipping_date, reference)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)
        cursor.execute(purchase_query, (
            purchase_data['vendor_id'], purchase_data['vendor_order_number'], purchase_data['purchase_order_number'],
            purchase_data['purchase_date'], purchase_data['purchase_amount'], purchase_data['taxes'],
            purchase_data['discount'], purchase_data['customs_fees'], purchase_data['currency'],
            purchase_data['purchase_status'], purchase_data['payment_method'], purchase_data['shipping_cost'],
            purchase_data['shipping_date'], purchase_data['reference']
        ))
        purchase_id = cursor.lastrowid

        self._add_product_purchases(cursor, purchase_id, purchase_data['items'])
        logger.debug(f"Added purchase with ID: {purchase_id}")

    @ErrorHandler.handle_errors()
    def _update_purchase(self, cursor, purchase_data: Dict[str, Any]) -> None:
        """Update an existing purchase and its associated product purchases."""
        purchase_query = self.queries.get('update_purchase', """
        UPDATE Purchases SET
            vendor_id = ?, vendor_order_number = ?, purchase_date = ?, purchase_amount = ?,
            taxes = ?, discount = ?, customs_fees = ?, currency = ?, purchase_status = ?,
            payment_method = ?, shipping_cost = ?, shipping_date = ?, reference = ?
        WHERE purchase_id = ?
        """)
        cursor.execute(purchase_query, (
            purchase_data['vendor_id'], purchase_data['vendor_order_number'], purchase_data['purchase_date'],
            purchase_data['purchase_amount'], purchase_data['taxes'], purchase_data['discount'],
            purchase_data['customs_fees'], purchase_data['currency'], purchase_data['purchase_status'],
            purchase_data['payment_method'], purchase_data['shipping_cost'], purchase_data['shipping_date'],
            purchase_data['reference'], purchase_data['purchase_id']
        ))

        self._delete_product_purchases(cursor, purchase_data['purchase_id'])
        self._add_product_purchases(cursor, purchase_data['purchase_id'], purchase_data['items'])
        logger.debug(f"Updated purchase with ID: {purchase_data['purchase_id']}")

    @ErrorHandler.handle_errors()
    def _delete_purchase(self, cursor, purchase_id: int) -> None:
        """Delete a purchase and its associated product purchases."""
        self._delete_product_purchases(cursor, purchase_id)
        delete_query = self.queries.get('delete_purchase', "DELETE FROM Purchases WHERE purchase_id = ?")
        cursor.execute(delete_query, (purchase_id,))
        logger.debug(f"Deleted purchase with ID: {purchase_id}")

    @ErrorHandler.handle_errors()
    def _add_product_purchases(self, cursor, purchase_id: int, items: List[Dict[str, Any]]) -> None:
        """Add product purchases for a given purchase."""
        query = self.queries.get('add_product_purchase', """
        INSERT INTO Product_Purchases (purchase_id, product_id, quantity, unit_price)
        VALUES (?, ?, ?, ?)
        """)
        for item in items:
            cursor.execute(query, (purchase_id, item['product_id'], item['quantity'], item['unit_price']))
        logger.debug(f"Added {len(items)} product purchases for purchase ID: {purchase_id}")

    @ErrorHandler.handle_errors()
    def _delete_product_purchases(self, cursor, purchase_id: int) -> None:
        """Delete all product purchases associated with a purchase."""
        query = self.queries.get('delete_product_purchases', "DELETE FROM Product_Purchases WHERE purchase_id = ?")
        cursor.execute(query, (purchase_id,))
        logger.debug(f"Deleted product purchases for purchase ID: {purchase_id}")