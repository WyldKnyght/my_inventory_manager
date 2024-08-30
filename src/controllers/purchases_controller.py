# src/controllers/purchases_controller.py

from typing import List, Dict, Any
from .database_controller import DatabaseController
from .purchases import validate_purchase_data

class PurchasesController:
    def __init__(self):
        self.db_controller = DatabaseController()

    def get_all_purchases(self) -> List[Dict[str, Any]]:
        """Retrieve all purchases from the database."""
        query = """
        SELECT p.purchase_id, p.purchase_order_number, p.purchase_date, v.company_name as vendor_name, p.purchase_amount
        FROM Purchases p
        LEFT JOIN Vendors v ON p.vendor_id = v.vendor_id
        ORDER BY p.purchase_date DESC
        """
        return self.db_controller.fetch_all(query)

    def add_purchase(self, purchase_data):
        """Add a new purchase to the database."""
        if not validate_purchase_data(purchase_data):
            raise ValueError("Invalid purchase data")
        try:
            self.queries.add_purchase(purchase_data)
        except Exception as e:
            self.logger.error(f"Error adding purchase: {str(e)}")
            raise

    def update_purchase(self, purchase_data):
        """Update an existing purchase in the database."""
        if not validate_purchase_data(purchase_data):
            raise ValueError("Invalid purchase data")
        try:
            self.queries.update_purchase(purchase_data)
        except Exception as e:
            self.logger.error(f"Error updating purchase: {str(e)}")
            raise

    def delete_purchase(self, purchase_id):
        """Delete a purchase and its product purchases from the database."""
        try:
            self.queries.delete_purchase(purchase_id)
        except Exception as e:
            self.logger.error(f"Error deleting purchase: {str(e)}")
            raise

    def get_purchase_by_id(self, purchase_id):
        """Retrieve a specific purchase and its product purchases by purchase ID."""
        return self.queries.get_purchase_by_id(purchase_id)