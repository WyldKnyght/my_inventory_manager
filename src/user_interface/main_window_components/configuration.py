# src/user_interface/main_window/configuration.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import UIConfig, Titles
from configs.config_manager import config_manager

class Configuration:
    @ErrorManager.handle_errors()
    def reload_configurations(self) -> None:
        config_manager.reload_configs()
        if self.validate_configurations():
            self.update_ui_from_config()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Some configurations are invalid. Using default values.")
        logger.info("Configurations reloaded and applied to MainWindow")

    @ErrorManager.handle_errors()
    def update_ui_from_config(self) -> None:
        self.setWindowTitle(Titles.MAIN_WINDOW)
        self.resize(*UIConfig.MAIN_WINDOW_SIZE)
        # Update other UI elements as needed
        for i in range(self.tab_widget.count()):
            tab_name = self.tab_widget.tabText(i)
            new_name = getattr(Titles.Tabs, tab_name.upper(), tab_name)
            self.tab_widget.setTabText(i, new_name)
        logger.info("UI updated from current configuration")

    @ErrorManager.handle_errors()
    def validate_configurations(self) -> bool:
        required_configs = [
            ('ui.main_window_size', UIConfig.MAIN_WINDOW_SIZE),
            ('ui.main_window_title', Titles.MAIN_WINDOW),
            ('ui.tab_titles.home', Titles.Tabs.HOME),
            ('ui.tab_titles.inventory', Titles.Tabs.INVENTORY),
            ('ui.tab_titles.settings', Titles.Tabs.SETTINGS),
            ('ui.tab_titles.purchases', Titles.Tabs.PURCHASES),
        ]
        for config_key, config_value in required_configs:
            if not config_value:
                logger.error(f"Missing or invalid configuration: {config_key}")
                return False
        logger.info("Configuration validation passed")
        return True