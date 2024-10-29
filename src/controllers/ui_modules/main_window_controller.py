# src/controllers/ui_operations/main_window_controller.py

from PyQt6.QtWidgets import QMainWindow
from utils.custom_logging import logger
from configs.path_config import EnvSettings
from configs.settings_manager import SettingsManager

class MainWindowController:
    def __init__(self, window: QMainWindow, db_manager):
        self.window = window
        self.db_manager = db_manager
        self.env_settings = EnvSettings()
        self.settings_manager = SettingsManager()

    def load_settings(self):
        """Load main window settings."""
        try:
            self.settings_manager.load_app_settings()
            size = self.settings_manager.get_setting('window_size', (800, 600))
            self.window.resize(*size)
            position = self.settings_manager.get_setting('window_position', (100, 100))
            self.window.move(*position)
            return True, "Settings loaded successfully"
        except Exception as e:
            logger.error(f"Error loading main window settings: {e}")
            return False, f"Error loading settings: {str(e)}"

    def save_settings(self):
        """Save main window settings."""
        try:
            self.settings_manager.set_setting('window_size', (self.window.width(), self.window.height()))
            self.settings_manager.set_setting('window_position', (self.window.x(), self.window.y()))
            self.settings_manager.save_app_settings()
            return True, "Settings saved successfully"
        except Exception as e:
            logger.error(f"Error saving main window settings: {e}")
            return False, f"Error saving settings: {str(e)}"