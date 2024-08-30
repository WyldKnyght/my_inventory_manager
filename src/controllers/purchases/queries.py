# src/controllers/purchases/queries.py

from typing import List, Dict, Any
from ..database_controller import DatabaseController
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.config_manager import config_manager

class PurchasesQueries:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.queries = config_manager.get('database.queries.purchases', {})
        logger.info("Initialized PurchasesQueries")

    @ErrorHandler.handle_errors()
    def get_all_purchases(self) -> List[Dict[str, Any]]:
        """Retrieve all purchases from the database."""
        query = self.queries.get('get_all_purchases', """
        SELECT p.purchase_id, p.purchase_order_number, p.purchase_date, v.company_name as vendor_name, p.purchase_amount
        FROM Purchases p
        LEFT JOIN Vendors v ON p.vendor_id = v.vendor_id
        ORDER BY p.purchase_date DESC
        """)
        result = self.db_controller.execute_query(query)
        logger.debug(f"Retrieved {len(result)} purchases")
        return result

    @ErrorHandler.handle_errors()
    def add_purchase(self, purchase_data: Dict[str, Any]) -> int:
        """Add a new purchase to the database."""
        purchase_query = self.queries.get('add_purchase', """
        INSERT INTO Purchases (vendor_id, vendor_order_number, purchase_order_number, purchase_date, purchase_amount,
                               taxes, discount, customs_fees, currency, purchase_status, payment_method, shipping_cost,
                               shipping_date, reference)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)
        purchase_params = (
            purchase_data['vendor_id'], purchase_data['vendor_order_number'], purchase_data['purchase_order_number'],
            purchase_data['purchase_date'], purchase_data['purchase_amount'], purchase_data['taxes'],
            purchase_data['discount'], purchase_data['customs_fees'], purchase_data['currency'],
            purchase_data['purchase_status'], purchase_data['payment_method'], purchase_data['shipping_cost'],
            purchase_data['shipping_date'], purchase_data['reference']
        )
        purchase_id = self.db_controller.execute_query(purchase_query, purchase_params, get_last_id=True)
        
        for item in purchase_data['items']:
            self.add_product_purchase(purchase_id, item)
        
        logger.info(f"Added new purchase with ID: {purchase_id}")
        return purchase_id

    @ErrorHandler.handle_errors()
    def add_product_purchase(self, purchase_id: int, item_data: Dict[str, Any]) -> None:
        """Add a product purchase to the database."""
        query = self.queries.get('add_product_purchase', "INSERT INTO Product_Purchases (purchase_id, product_id, quantity) VALUES (?, ?, ?)")
        params = (purchase_id, item_data['product_id'], item_data['quantity'])
        self.db_controller.execute_query(query, params)
        logger.debug(f"Added product purchase for purchase ID: {purchase_id}")

    @ErrorHandler.handle_errors()
    def update_purchase(self, purchase_data: Dict[str, Any]) -> None:
        """Update an existing purchase in the database."""
        purchase_query = self.queries.get('update_purchase', """
        UPDATE Purchases SET
            vendor_id = ?, vendor_order_number = ?, purchase_date = ?, purchase_amount = ?,
            taxes = ?, discount = ?, customs_fees = ?, currency = ?, purchase_status = ?,
            payment_method = ?, shipping_cost = ?, shipping_date = ?, reference = ?
        WHERE purchase_order_number = ?
        """)
        purchase_params = (
            purchase_data['vendor_id'], purchase_data['vendor_order_number'], purchase_data['purchase_date'],
            purchase_data['purchase_amount'], purchase_data['taxes'], purchase_data['discount'],
            purchase_data['customs_fees'], purchase_data['currency'], purchase_data['purchase_status'],
            purchase_data['payment_method'], purchase_data['shipping_cost'], purchase_data['shipping_date'],
            purchase_data['reference'], purchase_data['purchase_order_number']
        )
        self.db_controller.execute_query(purchase_query, purchase_params)

        self.delete_product_purchases(purchase_data['purchase_id'])
        for item in purchase_data['items']:
            self.add_product_purchase(purchase_data['purchase_id'], item)
        
        logger.info(f"Updated purchase with ID: {purchase_data['purchase_id']}")

    @ErrorHandler.handle_errors()
    def delete_purchase(self, purchase_id: int) -> None:
        """Delete a purchase and its product purchases from the database."""
        self.delete_product_purchases(purchase_id)
        query = self.queries.get('delete_purchase', "DELETE FROM Purchases WHERE purchase_id = ?")
        self.db_controller.execute_query(query, (purchase_id,))
        logger.info(f"Deleted purchase with ID: {purchase_id}")

    @ErrorHandler.handle_errors()
    def delete_product_purchases(self, purchase_id: int) -> None:
        """Delete all product purchases associated with a purchase."""
        query = self.queries.get('delete_product_purchases', "DELETE FROM Product_Purchases WHERE purchase_id = ?")
        self.db_controller.execute_query(query, (purchase_id,))
        logger.debug(f"Deleted product purchases for purchase ID: {purchase_id}")

    @ErrorHandler.handle_errors()
    def get_purchase_by_id(self, purchase_id: int) -> Dict[str, Any]:
        """Retrieve a specific purchase and its product purchases by purchase ID."""
        purchase_query = self.queries.get('get_purchase_by_id', """
        SELECT p.*, v.company_name as vendor_name
        FROM Purchases p
        LEFT JOIN Vendors v ON p.vendor_id = v.vendor_id
        WHERE p.purchase_id = ?
        """)
        purchase = self.db_controller.execute_query(purchase_query, (purchase_id,), fetch_one=True)

        items_query = self.queries.get('get_purchase_items', """
        SELECT pp.*, c.item_name, c.cost_price
        FROM Product_Purchases pp
        JOIN Catalog c ON pp.product_id = c.item_id
        WHERE pp.purchase_id = ?
        """)
        items = self.db_controller.execute_query(items_query, (purchase_id,))

        if purchase:
            purchase['items'] = items
        logger.debug(f"Retrieved purchase with ID: {purchase_id}")
        return purchase