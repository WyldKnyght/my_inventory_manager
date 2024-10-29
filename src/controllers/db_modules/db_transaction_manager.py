# src/controllers/db_modules/db_transaction_manager.py

class TransactionManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert_transaction(self, date: str, account_id: int, category_id: int, description: str, amount: float):
        """Insert a new transaction into the transactions table."""
        command = """
        INSERT INTO transactions (date, account_id, category_id, description, 
                                  income, expense)
        VALUES (?, ?, ?, ?, CASE WHEN ? > 0 THEN ? ELSE 0 END, 
                CASE WHEN ? < 0 THEN ABS(?) ELSE 0 END)
        """
        return self.db_manager.execute_command(command, (date, account_id, category_id, description, amount, amount, amount, amount))

    def get_transactions(self, start_date: str, end_date: str):
        query = """
        SELECT t.date, coa.account_name, c.name as category, t.description, 
               t.income, t.expense,
               (SELECT SUM(COALESCE(income, 0) - COALESCE(expense, 0)) 
                FROM transactions 
                WHERE date <= t.date) AS balance
        FROM transactions t
        JOIN chart_of_accounts coa ON t.account_id = coa.id
        LEFT JOIN categories c ON t.category_id = c.id
        WHERE t.date BETWEEN ? AND ?
        ORDER BY t.date
        """
        return self.db_manager.execute_query(query, (start_date, end_date))

    # Add more transaction-related methods here