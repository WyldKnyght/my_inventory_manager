from src.utils.database import execute_query, fetch_all

def create_purchase(purchase_data):
    """Create a new purchase in the Purchase table."""
    query = """
    INSERT INTO Purchase (vendor_id, purchase_order_number, reference, date, expected_delivery_date, items)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    execute_query(query, purchase_data)

def get_all_purchases():
    """Retrieve all purchases from the Purchase table."""
    query = "SELECT * FROM Purchase"
    return fetch_all(query)

def update_purchase(purchase_id, updated_data):
    """Update an existing purchase in the Purchase table."""
    query = """
    UPDATE Purchase
    SET vendor_id = ?, purchase_order_number = ?, reference = ?, date = ?, expected_delivery_date = ?, items = ?
    WHERE purchase_id = ?
    """
    execute_query(query, updated_data + (purchase_id,))

def delete_purchase(purchase_id):
    """Delete a purchase from the Purchase table."""
    query = "DELETE FROM Purchase WHERE purchase_id = ?"
    execute_query(query, (purchase_id,))