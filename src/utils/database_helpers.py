from controllers.database_controller import DatabaseController

def fetch_foreign_key_data(table_name, key_column, value_column):
    """Fetch data for foreign key fields."""
    db_controller = DatabaseController()
    query = f"SELECT {key_column}, {value_column} FROM {table_name}"
    try:
        return db_controller.fetch_all(query)
    except Exception as e:
        print(f"Error fetching foreign key data: {e}")
        return []