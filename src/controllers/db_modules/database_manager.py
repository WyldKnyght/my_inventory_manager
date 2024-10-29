# src/controllers/database_manager.py

from pathlib import Path
from configs.path_config import DB_PATH
from utils.custom_logging import error_handler
from ..schema_modules.schema_manager import SchemaManager
from .db_connection_manager import ConnectionManager
from .db_initializer import DatabaseInitializer
from .db_transaction_manager import TransactionManager
from .db_inventory_manager import InventoryManager
from .db_settings_manager import SettingsManager
from .db_query_executor import QueryExecutor
from .db_table_manager import TableManager

class DatabaseManager:
    def __init__(self):
        self.db_path = Path(DB_PATH)
        self.schema_manager = SchemaManager()
        self.connection_manager = ConnectionManager(self.db_path)
        self.query_executor = QueryExecutor(self.db_path)
        self.table_manager = TableManager(self.query_executor)
        self.database_initializer = DatabaseInitializer(self)
        self.transaction_manager = TransactionManager(self)
        self.inventory_manager = InventoryManager(self)
        self.settings_manager = SettingsManager(self)

    @error_handler
    def connect(self):
        return self.connection_manager.get_connection()

    @error_handler
    def initialize_database(self):
        self.schema_manager.load_schemas()
        self.database_initializer.initialize_database()

    def execute_query(self, query: str, params: tuple = ()):
        return self.query_executor.execute_query(query, params)

    def execute_command(self, command: str, params: tuple = ()):
        return self.query_executor.execute_command(command, params)

    def execute_many(self, command: str, param_list: list):
        return self.query_executor.execute_many(command, param_list)

    def table_exists(self, table_name: str):
        return self.table_manager.table_exists(table_name)
    
    def get_table_info(self, table_name: str):
        return self.table_manager.get_table_info(table_name)