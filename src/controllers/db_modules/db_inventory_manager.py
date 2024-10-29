# src/controllers/db_modules/db_inventory_manager.py

from typing import List, Tuple, Any, Dict

class InventoryManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.schema_manager = db_manager.schema_manager

    def get_inventory(self) -> List[Tuple[Any, ...]]:
        """Retrieve all items in the inventory based on the schema."""
        columns = self.schema_manager.get_column_names('inventory', 'catalog')
        columns_str = ', '.join([f"c.{col}" for col in columns])
        
        query = f"""
        SELECT {columns_str}
        FROM catalog c
        ORDER BY c.item_name
        """
        return self.db_manager.execute_query(query)

    def add_item(self, item: Dict[str, Any]):
        """Add a new item to the catalog based on the schema."""
        columns = self.schema_manager.get_column_names('inventory', 'catalog')
        columns = [col for col in columns if col != 'item_id']  # Exclude item_id as it's auto-generated
        placeholders = ', '.join(['?' for _ in columns])
        columns_str = ', '.join(columns)
        
        command = f"""
        INSERT INTO catalog ({columns_str})
        VALUES ({placeholders})
        """
        
        values = [item.get(col) for col in columns]
        
        return self.db_manager.execute_command(command, tuple(values))

    def search_inventory(self, search_term: str) -> List[Tuple[Any, ...]]:
        """Search for items in the inventory."""
        columns = self.schema_manager.get_column_names('inventory', 'catalog')
        columns_str = ', '.join([f"c.{col}" for col in columns])
        
        searchable_columns = [col for col in columns if 
                              self.schema_manager.get_column_type('inventory', 'catalog', col).upper() in ['TEXT', 'VARCHAR']]
        search_conditions = ' OR '.join([f"c.{col} LIKE ?" for col in searchable_columns])
        
        query = f"""
        SELECT {columns_str}
        FROM catalog c
        WHERE {search_conditions}
        ORDER BY c.item_name
        """
        search_pattern = f"%{search_term}%"
        return self.db_manager.execute_query(query, tuple(search_pattern for _ in searchable_columns))

    def update_item_quantity(self, item_id: int, new_quantity: int):
        """Update the quantity of an item in the inventory."""
        command = """
        UPDATE catalog
        SET quantity = ?
        WHERE item_id = ?
        """
        return self.db_manager.execute_command(command, (new_quantity, item_id))

    def delete_item(self, item_id: int):
        """Delete an item from the inventory."""
        command = """
        DELETE FROM catalog
        WHERE item_id = ?
        """
        return self.db_manager.execute_command(command, (item_id,))

    def generate_item_number(self) -> str:
        """Generate a unique item number."""
        query = "SELECT MAX(CAST(SUBSTR(item_number, 4) AS INTEGER)) FROM catalog WHERE item_number LIKE 'ITM%'"
        result = self.db_manager.execute_query(query)
        max_number = result[0][0] if result[0][0] is not None else 0
        return f"ITM{max_number + 1:04d}"

    def get_categories(self) -> List[Tuple[int, str]]:
        """Get all categories."""
        query = "SELECT category_id, category_name FROM categories ORDER BY category_name"
        return self.db_manager.execute_query(query)

    def get_unit_types(self) -> List[Tuple[int, str]]:
        """Get all unit types."""
        query = "SELECT unit_type_id, unit_type FROM unit_types ORDER BY unit_type"
        return self.db_manager.execute_query(query)