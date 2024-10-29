# src\controllers\schema_modules\schema_loader.py
import re
from pathlib import Path
from typing import Dict, Any
from utils.custom_logging import get_logger

logger = get_logger(__name__)

def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Load the schema from an SQL file."""
    with open(schema_path, 'r') as schema_file:
        sql_content = schema_file.read()

    schema = {}
    statements = re.split(r';(?=\s*(?:CREATE|DROP))', sql_content)

    for statement in statements:
        statement = statement.strip()
        if not statement:
            continue

        if statement.upper().startswith('CREATE TABLE'):
            if table_info := parse_create_table(statement):
                schema[table_info['name']] = table_info
        elif statement.upper().startswith('CREATE VIEW'):
            if view_info := parse_create_view(statement):
                schema[view_info['name']] = view_info

    return schema

def parse_create_table(statement: str) -> Dict[str, Any]:
    """Parse a CREATE TABLE statement."""
    match = re.match(r'CREATE TABLE (\w+)\s*\((.*)\)', statement, re.DOTALL | re.IGNORECASE)
    if not match:
        return {}

    table_name = match[1]
    columns_part = match[2]

    columns = {}
    foreign_keys = []
    for column_def in re.finditer(r'(\w+)\s+([\w()]+)(?:\s+(.*))?|FOREIGN KEY\s*\((.*?)\)\s*REFERENCES\s*(.*)', columns_part):
        if column_def.group(1):  # Regular column
            column_name = column_def.group(1)
            column_type = column_def.group(2)
            constraints = column_def.group(3) or ''

            columns[column_name] = {
                'type': column_type,
                'constraints': [c.strip() for c in re.split(r',(?![^(]*\))', constraints) if c.strip()]
            }
        else:  # Foreign key
            foreign_keys.append({
                'column': column_def.group(4),
                'references': column_def.group(5)
            })

    return {
        'name': table_name,
        'type': 'table',
        'columns': columns,
        'foreign_keys': foreign_keys
    }

def parse_create_view(statement: str) -> Dict[str, Any]:
    """Parse a CREATE VIEW statement."""
    match = re.match(r'CREATE VIEW (\w+)\s+AS\s+(.*)', statement, re.DOTALL | re.IGNORECASE)
    if not match:
        return {}

    view_name = match[1]
    view_definition = match[2]

    return {
        'name': view_name,
        'type': 'view',
        'definition': view_definition.strip()
    }