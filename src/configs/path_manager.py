# src/configs/path_manager.py

import os
from typing import List
from utils.error_manager import ErrorManager

class PathManager:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        self.src_dir = os.path.join(self.root_dir, "src")
        self.database_dir = os.path.join(self.root_dir, "database")
        self.docs_dir = os.path.join(self.root_dir, "docs")
        self.configs_dir = os.path.join(self.src_dir, "configs")
        self.config_management_dir = os.path.join(self.configs_dir, "config_management")
        self.utils_dir = os.path.join(self.src_dir, "utils")
        self.controllers_dir = os.path.join(self.src_dir, "controllers")
        self.database_controllers_dir = os.path.join(self.controllers_dir, "database")
        self.purchases_controllers_dir = os.path.join(self.controllers_dir, "purchases")
        self.user_interface_dir = os.path.join(self.src_dir, "user_interface")
        self.resources_dir = os.path.join(self.src_dir, "resources")
        self.tests_dir = os.path.join(self.root_dir, "tests")

        # User interface subdirectories
        self.ui_common_dir = os.path.join(self.user_interface_dir, "common")
        self.ui_base_widget_components_dir = os.path.join(self.ui_common_dir, "base_widget_components")
        self.ui_inventory_dir = os.path.join(self.user_interface_dir, "inventory")
        self.ui_main_window_components_dir = os.path.join(self.user_interface_dir, "main_window_components")
        self.ui_purchases_dir = os.path.join(self.user_interface_dir, "purchases")
        self.ui_purchases_dialogs_dir = os.path.join(self.ui_purchases_dir, "dialogs")
        self.ui_reports_dir = os.path.join(self.user_interface_dir, "reports")
        self.ui_sales_dir = os.path.join(self.user_interface_dir, "sales")
        self.ui_settings_dir = os.path.join(self.user_interface_dir, "settings")

        self._ensure_all_directories()

    def _ensure_all_directories(self):
        for dir_path in self.get_all_directories():
            self.ensure_dir(dir_path)

    def get_all_directories(self) -> List[str]:
        return [
            self.src_dir,
            self.database_dir,
            self.docs_dir,
            self.configs_dir,
            self.config_management_dir,
            self.utils_dir,
            self.controllers_dir,
            self.database_controllers_dir,
            self.purchases_controllers_dir,
            self.user_interface_dir,
            self.resources_dir,
            self.tests_dir,
            self.ui_common_dir,
            self.ui_base_widget_components_dir,
            self.ui_inventory_dir,
            self.ui_main_window_components_dir,
            self.ui_purchases_dir,
            self.ui_purchases_dialogs_dir,
            self.ui_reports_dir,
            self.ui_sales_dir,
            self.ui_settings_dir
        ]

    @staticmethod
    def ensure_dir(dir_path: str):
        os.makedirs(dir_path, exist_ok=True)

    @ErrorManager.handle_errors(default_value="")
    def get_config_yaml_path(self, filename: str) -> str:
        return os.path.join(self.config_management_dir, filename)

    @ErrorManager.handle_errors(default_value="")
    def get_database_path(self) -> str:
        return os.path.join(self.database_dir, "inventory.db")

    @ErrorManager.handle_errors(default_value="")
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