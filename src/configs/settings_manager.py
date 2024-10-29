# src/configs/settings_manager.py

import json
import os
from configs.path_config import DEFAULT_SETTINGS_PATH
from utils.custom_logging import logger

class SettingsManager:
    def __init__(self):
        self.app_settings = {}
        self.load_app_settings()

    def load_app_settings(self):
        if os.path.exists(DEFAULT_SETTINGS_PATH):
            try:
                with open(DEFAULT_SETTINGS_PATH, 'r') as f:
                    if content := f.read().strip():
                        self.app_settings = json.loads(content)
                    else:
                        self.initialize_default_settings()
            except json.JSONDecodeError:
                logger.error(f"Error decoding JSON from {DEFAULT_SETTINGS_PATH}. Using default settings.")
                self.initialize_default_settings()
        else:
            logger.info(f"Settings file not found at {DEFAULT_SETTINGS_PATH}. Creating default settings.")
            self.initialize_default_settings()

    def initialize_default_settings(self):
        self.app_settings = {
            "theme": "light",
            "language": "en",
            "window_size": (800, 600),
            "window_position": (100, 100),
            # Add more default settings as needed
        }
        self.save_app_settings()

    def save_app_settings(self):
        try:
            os.makedirs(os.path.dirname(DEFAULT_SETTINGS_PATH), exist_ok=True)
            with open(DEFAULT_SETTINGS_PATH, 'w') as f:
                json.dump(self.app_settings, f, indent=4)
        except Exception as e:
            logger.error(f"Error saving app settings: {str(e)}")

    def get_setting(self, key, default=None):
        return self.app_settings.get(key, default)

    def set_setting(self, key, value):
        self.app_settings[key] = value
        self.save_app_settings()

    # Add more methods here for other app-wide settings as needed