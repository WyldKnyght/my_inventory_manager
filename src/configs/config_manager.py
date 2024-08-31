# src/configs/config_manager.py

import yaml
import os
from typing import Any
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.path_manager import path_manager
from configs.config_management.database_config import DatabaseConfig
from configs.config_management.ui_config import UIConfig
from configs.config_management.general_config import GeneralConfig

class ConfigManager(DatabaseConfig, UIConfig, GeneralConfig):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    @ErrorManager.handle_errors()
    def _initialize(self) -> None:
        self.config = {}
        self._load_config('ui_config.yaml', 'ui')
        self._load_config('database_config.yaml', 'database')
        self._load_config('general_config.yaml', 'general')
        self._replace_path_placeholders()
        logger.info("ConfigManager initialized")

    def _load_config(self, filename: str, config_key: str) -> None:
        config_path = os.path.join(path_manager.configs_dir, 'config_management', filename)
        with open(config_path, 'r') as f:
            self.config[config_key] = yaml.safe_load(f)

    def _replace_path_placeholders(self):
        placeholders = {
            "{{ROOT_DIR}}": path_manager.root_dir,
            "{{SRC_DIR}}": path_manager.src_dir,
            "{{DATABASE_DIR}}": path_manager.database_dir,
            "{{CONFIGS_DIR}}": path_manager.configs_dir,
            "{{UTILS_DIR}}": path_manager.utils_dir,
            "{{CONTROLLERS_DIR}}": path_manager.controllers_dir,
            "{{USER_INTERFACE_DIR}}": path_manager.user_interface_dir,
            "{{RESOURCES_DIR}}": path_manager.resources_dir,
            "{{TESTS_DIR}}": path_manager.tests_dir,
        }
        self._replace_placeholders_recursive(self.config, placeholders)

    def _replace_placeholders_recursive(self, obj, placeholders):
        if isinstance(obj, dict):
            return {k: self._replace_placeholders_recursive(v, placeholders) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._replace_placeholders_recursive(item, placeholders) for item in obj]
        elif isinstance(obj, str):
            for placeholder, value in placeholders.items():
                obj = obj.replace(placeholder, value)
        return obj

    @ErrorManager.handle_errors(default_value=None)
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default

    @ErrorManager.handle_errors()
    def update(self, key: str, value: Any) -> None:
        keys = key.split('.')
        if keys[0] not in self.config:
            raise ValueError(f"Invalid configuration category: {keys[0]}")
        target = self.config[keys[0]]
        for k in keys[1:-1]:
            target = target.setdefault(k, {})
        target[keys[-1]] = value
        self._save_config(keys[0])
        logger.info(f"Updated configuration: {key}")

    @ErrorManager.handle_errors()
    def _save_config(self, config_key: str) -> None:
        filename = f"{config_key}_config.yaml"
        config_path = os.path.join(path_manager.configs_dir, 'config_management', filename)
        with open(config_path, 'w') as f:
            yaml.dump(self.config[config_key], f)
        logger.debug(f"Saved {config_key} configurations")

    @ErrorManager.handle_errors()
    def reload_configs(self) -> None:
        self._initialize()
        logger.info("Reloaded configurations")

config_manager = ConfigManager()