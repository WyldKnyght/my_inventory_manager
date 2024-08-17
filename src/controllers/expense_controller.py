from src.utils.database import execute_query, fetch_all

def create_expense(expense_data):
    """Create a new expense in the Expense table."""
    query = """
    INSERT INTO Expense (date, category_name, amount, vendor_id, reference, notes)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    execute_query(query, expense_data)

def get_all_expenses():
    """Retrieve all expenses from the Expense table."""
    query = "SELECT * FROM Expense"
    return fetch_all(query)

def update_expense(expense_id, updated_data):
    """Update an existing expense in the Expense table."""
    query = """
    UPDATE Expense
    SET date = ?, category_name = ?, amount = ?, vendor_id = ?, reference = ?, notes = ?
    WHERE expense_id = ?
    """
    execute_query(query, updated_data + (expense_id,))

def delete_expense(expense_id):
    """Delete an expense from the Expense table."""
    query = "DELETE FROM Expense WHERE expense_id = ?"
    execute_query(query, (expense_id,))