# src/controllers/schema_modules/schema_query.py
from typing import List, Dict, Any

def get_table_names(schema: Dict[str, Any]) -> List[str]:
    """Get all table names from the schema."""
    return list(schema.keys())

def get_table_schema(schema: Dict[str, Any], table_name: str) -> Dict[str, Any]:
    """Get the schema for a specific table."""
    return schema.get(table_name, {})

def get_column_names(schema: Dict[str, Any], table_name: str) -> List[str]:
    """Get all column names for a specific table."""
    table_schema = get_table_schema(schema, table_name)
    if 'columns' in table_schema:
        return [col for col in table_schema['columns'].keys() if col != 'FOREIGN']
    return []

def get_column_type(schema: Dict[str, Any], table_name: str, column_name: str) -> str:
    """Get the type of a specific column in a table."""
    table_schema = get_table_schema(schema, table_name)
    return table_schema.get(column_name, {}).get('type', '')

def get_column_constraints(schema: Dict[str, Any], table_name: str, column_name: str) -> List[str]:
    """Get the constraints for a specific column in a table."""
    table_schema = get_table_schema(schema, table_name)
    return table_schema.get(column_name, {}).get('constraints', [])