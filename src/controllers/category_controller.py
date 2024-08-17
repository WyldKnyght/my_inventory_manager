from src.utils.database import execute_query, fetch_all

def create_category(category_data):
    """Create a new category in the Categories table."""
    query = """
    INSERT INTO Categories (name, description)
    VALUES (?, ?)
    """
    execute_query(query, category_data)

def get_all_categories():
    """Retrieve all categories from the Categories table."""
    query = "SELECT * FROM Categories"
    return fetch_all(query)

def update_category(category_id, updated_data):
    """Update an existing category in the Categories table."""
    query = """
    UPDATE Categories
    SET name = ?, description = ?
    WHERE category_id = ?
    """
    execute_query(query, updated_data + (category_id,))

def delete_category(category_id):
    """Delete a category from the Categories table."""
    query = "DELETE FROM Categories WHERE category_id = ?"
    execute_query(query, (category_id,))