from src.utils.database import execute_query, fetch_all

def create_customer(customer_data):
    """Create a new customer in the Customer table."""
    query = """
    INSERT INTO Customer (customer_type, primary_contact, salutation, first_name, last_name, company_name, display_name, email, phone, billing_address, shipping_address)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    execute_query(query, customer_data)

def get_all_customers():
    """Retrieve all customers from the Customer table."""
    query = "SELECT * FROM Customer"
    return fetch_all(query)

def update_customer(customer_id, updated_data):
    """Update an existing customer in the Customer table."""
    query = """
    UPDATE Customer
    SET customer_type = ?, primary_contact = ?, salutation = ?, first_name = ?, last_name = ?, company_name = ?, display_name = ?, email = ?, phone = ?, billing_address = ?, shipping_address = ?
    WHERE customer_id = ?
    """
    execute_query(query, updated_data + (customer_id,))

def delete_customer(customer_id):
    """Delete a customer from the Customer table."""
    query = "DELETE FROM Customer WHERE customer_id = ?"
    execute_query(query, (customer_id,))