from utils.database import fetch_all, execute_query

class ManageTableController:
    def __init__(self):
        '''
        Constructor for the ManageTableController class. To be added later
        '''
        pass

    def get_data(self, table_name):
        """Fetch all data from the specified table."""
        query = f"SELECT * FROM {table_name}"
        return fetch_all(query)

    def delete_record(self, table_name, record_id):
        """Delete a record from the specified table."""
        primary_key_column = self.get_primary_key_column(table_name)
        query = f"DELETE FROM {table_name} WHERE {primary_key_column} = ?"
        execute_query(query, (record_id,))
    
    def insert_record(self, table_name, data):
        """Insert a new record into the specified table."""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        execute_query(query, tuple(data.values()))

    def update_record(self, table_name, record_id, data):
        """Update an existing record in the specified table."""
        primary_key_column = self.get_primary_key_column(table_name)
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {primary_key_column} = ?"
        execute_query(query, (*data.values(), record_id))

    def get_primary_key_column(self, table_name):
        """Return the primary key column name for the given table."""
        primary_keys = {
            "Accounts": "account_id",
            "Vendor": "vendor_id",
            "Manufacturer": "manufacturer_id",
            "Brand": "brand_id",
            "Customer": "customer_id",
            "Categories": "product_category_id"
        }
        return primary_keys.get(table_name, "id")  # Default to 'id' if not found