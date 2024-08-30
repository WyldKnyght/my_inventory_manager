# src/configs/path_management/path_manager.py

import os
from typing import List
from utils.error_handler import ErrorHandler

class PathManager:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        self.src_dir = os.path.join(self.root_dir, "src")
        self.database_dir = os.path.join(self.root_dir, "database")
        self.configs_dir = os.path.join(self.src_dir, "configs")
        self.utils_dir = os.path.join(self.src_dir, "utils")
        self.controllers_dir = os.path.join(self.src_dir, "controllers")
        self.user_interface_dir = os.path.join(self.src_dir, "user_interface")
        self.resources_dir = os.path.join(self.src_dir, "resources")
        self.tests_dir = os.path.join(self.root_dir, "tests")

        self._ensure_all_directories()

    def _ensure_all_directories(self):
        for dir_path in self.get_all_directories():
            self.ensure_dir(dir_path)

    def get_all_directories(self) -> List[str]:
        return [
            self.src_dir,
            self.database_dir,
            self.configs_dir,
            self.utils_dir,
            self.controllers_dir,
            self.user_interface_dir,
            self.resources_dir,
            self.tests_dir
        ]

    @staticmethod
    def ensure_dir(dir_path: str):
        os.makedirs(dir_path, exist_ok=True)

    @ErrorHandler.handle_errors(default_value="")
    def get_config_yaml_path(self) -> str:
        return os.path.join(self.configs_dir, "config.yaml")

    @ErrorHandler.handle_errors(default_value="")
    def get_database_path(self) -> str:
        return os.path.join(self.database_dir, "inventory.db")

    @ErrorHandler.handle_errors(default_value="")
    def get_schema_path(self) -> str:
        return os.path.join(self.database_dir, "schema.sql")

    @staticmethod
    def is_valid_file_path(path: str) -> bool:
        try:
            if not os.path.isabs(path):
                return False
            dir_path = os.path.dirname(path)
            if not os.path.exists(dir_path):
                return False
            return not set(path) & {'<', '>', ':', '"', '|', '?', '*'}
        except Exception:
            return False

    @staticmethod
    def get_directory(file_path: str) -> str:
        return os.path.dirname(file_path)

path_manager = PathManager()