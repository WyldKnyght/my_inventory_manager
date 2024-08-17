from src.utils.database import execute_query, fetch_all

def create_vendor(vendor_data):
    """Create a new vendor in the Vendor table."""
    query = """
    INSERT INTO Vendor (primary_contact, salutation, first_name, last_name, company_name, display_name, email, phone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    execute_query(query, vendor_data)

def get_all_vendors():
    """Retrieve all vendors from the Vendor table."""
    query = "SELECT * FROM Vendor"
    return fetch_all(query)

def update_vendor(vendor_id, updated_data):
    """Update an existing vendor in the Vendor table."""
    query = """
    UPDATE Vendor
    SET primary_contact = ?, salutation = ?, first_name = ?, last_name = ?, company_name = ?, display_name = ?, email = ?, phone = ?
    WHERE vendor_id = ?
    """
    execute_query(query, updated_data + (vendor_id,))

def delete_vendor(vendor_id):
    """Delete a vendor from the Vendor table."""
    query = "DELETE FROM Vendor WHERE vendor_id = ?"
    execute_query(query, (vendor_id,))