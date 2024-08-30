# src/configs/config_manager.py
import yaml
from typing import Any, Dict
from PyQt6.QtWidgets import QApplication
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from .path_manager import PathManager

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    @ErrorHandler.handle_errors()
    def _initialize(self) -> None:
        self.path_manager = PathManager()
        self.config: Dict[str, Any] = {}
        self._load_configs()
        self._load_styles()
        logger.info("ConfigManager initialized")

    @ErrorHandler.handle_errors()
    def _load_configs(self) -> None:
        config_files = [
            'database_config.yaml',
            'ui_config.yaml',
            'logging_config.yaml',
        ]
        for file in config_files:
            config_path = self.path_manager.get_config_path() / file
            with open(config_path, 'r') as f:
                self.config.update(yaml.safe_load(f))
        logger.debug(f"Loaded configurations: {', '.join(config_files)}")

    @ErrorHandler.handle_errors()
    def _load_styles(self) -> None:
        style_path = self.path_manager.get_resource_path() / 'styles.qss'
        with open(style_path, 'r') as f:
            self.style_template = f.read()
        logger.debug("Loaded style template")

    @ErrorHandler.handle_errors()
    def apply_styles(self) -> None:
        style = self.style_template
        ui_config = self.config.get('ui', {})
        colors = ui_config.get('colors', {})
        
        replacements = {
            '{{BACKGROUND_COLOR}}': colors.get('background', "#A7C6ED"),
            '{{BACKGROUND_COLOR_LIGHT}}': colors.get('background_light', "#E6F2FF"),
            '{{PRIMARY_COLOR}}': colors.get('primary', "#4F8CC9"),
            '{{SECONDARY_COLOR}}': colors.get('secondary', "#B0D0E8"),
            '{{TEXT_COLOR}}': colors.get('text', "#003D7A"),
            '{{FONT_SIZE}}': str(ui_config.get('font_size', 12)),
        }
        
        for placeholder, value in replacements.items():
            style = style.replace(placeholder, value)
        
        QApplication.instance().setStyleSheet(style)
        logger.info("Applied styles to application")

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @ErrorHandler.handle_errors()
    def update(self, key: str, value: Any) -> None:
        self.config[key] = value
        self._save_configs()
        logger.info(f"Updated configuration: {key}")

    @ErrorHandler.handle_errors()
    def _save_configs(self) -> None:
        for category, data in self.config.items():
            config_path = self.path_manager.get_config_path() / f"{category}_config.yaml"
            with open(config_path, 'w') as f:
                yaml.dump({category: data}, f)
        logger.debug("Saved configurations")

    @ErrorHandler.handle_errors()
    def reload_configs(self) -> None:
        """Reload all configurations and apply styles."""
        self._load_configs()
        self._load_styles()
        self.apply_styles()
        logger.info("Reloaded configurations and applied styles")

config_manager = ConfigManager()