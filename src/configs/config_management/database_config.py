import yaml
import os
from typing import List, Dict, Any
from utils.error_manager import ErrorManager
from configs.path_manager import path_manager

class DatabaseConfig:
    def __init__(self):
        self._load_config()

    def _load_config(self):
        config_path = os.path.join(path_manager.configs_dir, 'config_management', 'database_config.yaml')
        with open(config_path, 'r') as f:
            self.database_config = yaml.safe_load(f)

    @ErrorManager.handle_errors(default_value="id")
    def get_primary_key(self, table_name: str) -> str:
        return self.database_config['tables'][table_name]['primary_key']

    @ErrorManager.handle_errors(default_value=[])
    def get_table_fields(self, table_name: str) -> List[str]:
        return self.database_config['tables'][table_name]['fields']

    @ErrorManager.handle_errors(default_value={})
    def get_all_tables(self) -> Dict[str, Dict[str, Any]]:
        return self.database_config['tables']

    @ErrorManager.handle_errors(default_value="")
    def get_database_query(self, category: str, query_name: str) -> str:
        return self.database_config['queries'][category][query_name]

    @ErrorManager.handle_errors(default_value="")
    def get_database_path(self) -> str:
        return self.database_config['path']

    @ErrorManager.handle_errors(default_value="")
    def get_schema_path(self) -> str:
        return self.database_config['paths']['schema']