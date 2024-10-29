# src/controllers/schema_manager.py
from pathlib import Path
from typing import Dict, Any
from controllers.schema_modules import schema_loader, schema_query
from configs.path_config import FIN_SCHEMA_PATH, INV_SCHEMA_PATH, GLB_SCHEMA_PATH
from utils.custom_logging import logger

class SchemaManager:
    """
    Manages the schemas, which serve as the reference for the database structure.

    This class provides an interface to load and query the schemas from SQL files defined in
    the environment settings. The schemas are used ONLY as a reference for retrieving information 
    about tables, columns, types, and constraints. It does not interact with or modify the 
    actual database in any way.

    For detailed usage instructions and best practices, refer to the project's documentation.
    """
    def __init__(self):
        self.schemas: Dict[str, Dict[str, Any]] = {
            'finance': {},
            'inventory': {},
            'global': {}
        }

    def load_schemas(self):
        """Load the schemas from the SQL files specified in the environment settings."""
        logger.info("Loading schemas")
        self.schemas['finance'] = schema_loader.load_schema(Path(FIN_SCHEMA_PATH))
        self.schemas['inventory'] = schema_loader.load_schema(Path(INV_SCHEMA_PATH))
        self.schemas['global'] = schema_loader.load_schema(Path(GLB_SCHEMA_PATH))
        logger.info("Schemas loaded successfully")

    def get_table_names(self, schema_name: str):
        """Get a list of all table names defined in the specified schema."""
        return schema_query.get_table_names(self.schemas[schema_name])

    def get_table_schema(self, schema_name: str, table_name: str):
        """Get the schema for a specific table in the specified schema."""
        return schema_query.get_table_schema(self.schemas[schema_name], table_name)

    def get_column_names(self, schema_name: str, table_name: str):
        """Get a list of column names for a specific table in the specified schema."""
        return schema_query.get_column_names(self.schemas[schema_name], table_name)

    def get_column_type(self, schema_name: str, table_name: str, column_name: str):
        """Get the data type of a specific column in a table in the specified schema."""
        return schema_query.get_column_type(self.schemas[schema_name], table_name, column_name)

    def get_column_constraints(self, schema_name: str, table_name: str, column_name: str):
        """Get the constraints for a specific column in a table in the specified schema."""
        return schema_query.get_column_constraints(self.schemas[schema_name], table_name, column_name)