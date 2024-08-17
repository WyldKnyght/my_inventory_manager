from src.utils.database import execute_query, fetch_all

def create_sale(sale_data):
    """Create a new sale in the Sales table."""
    query = """
    INSERT INTO Sales (customer_id, sales_number, reference, order_date, expected_shipment_date, payment_terms, delivery_method, sub_total, discount, shipping_charges, adjustment, total, customer_notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    execute_query(query, sale_data)

def get_all_sales():
    """Retrieve all sales from the Sales table."""
    query = "SELECT * FROM Sales"
    return fetch_all(query)

def update_sale(sales_id, updated_data):
    """Update an existing sale in the Sales table."""
    query = """
    UPDATE Sales
    SET customer_id = ?, sales_number = ?, reference = ?, order_date = ?, expected_shipment_date = ?, payment_terms = ?, delivery_method = ?, sub_total = ?, discount = ?, shipping_charges = ?, adjustment = ?, total = ?, customer_notes = ?
    WHERE sales_id = ?
    """
    execute_query(query, updated_data + (sales_id,))

def delete_sale(sales_id):
    """Delete a sale from the Sales table."""
    query = "DELETE FROM Sales WHERE sales_id = ?"
    execute_query(query, (sales_id,))