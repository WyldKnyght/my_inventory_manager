# src/user_interface/main_window/tab_management.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import Titles
from user_interface.home_tab import HomeTab
from user_interface.inventory_tab import InventoryTab
from user_interface.settings_tab import SettingsTab
from user_interface.purchases_tab import PurchasesTab

class TabManagement:
    @ErrorManager.handle_errors()
    def create_tabs(self) -> list[tuple[QtWidgets.QWidget, str]]:
        return [
            (HomeTab(), Titles.Tabs.HOME),
            (InventoryTab(), Titles.Tabs.INVENTORY),
            (SettingsTab(), Titles.Tabs.SETTINGS),
            (PurchasesTab(), Titles.Tabs.PURCHASES),
        ]

    @ErrorManager.handle_errors()
    def add_tabs(self, tab_widget: QtWidgets.QTabWidget) -> None:
        for tab, name in self.create_tabs():
            tab_widget.addTab(tab, name)
        logger.debug(f"Added {tab_widget.count()} tabs to the tab widget")

    @ErrorManager.handle_errors()
    def add_tab(self, tab: QtWidgets.QWidget, name: str) -> None:
        self.get_tab_widget().addTab(tab, name)
        logger.debug(f"Added tab: {name}")

    @ErrorManager.handle_errors()
    def remove_tab(self, index: int) -> None:
        tab_widget = self.get_tab_widget()
        if not 0 <= index < tab_widget.count():
            raise ValueError(f"Invalid tab index: {index}")
        removed_tab_name = tab_widget.tabText(index)
        tab_widget.removeTab(index)
        logger.debug(f"Removed tab at index {index}: {removed_tab_name}")

    @ErrorManager.handle_errors()
    def switch_to_tab(self, index: int) -> None:
        if 0 <= index < self.tab_widget.count():
            self.tab_widget.setCurrentIndex(index)
            logger.debug(f"Switched to tab at index: {index}")
        else:
            logger.warning(f"Attempted to switch to invalid tab index: {index}")

    @ErrorManager.handle_errors()
    def get_current_tab_info(self) -> tuple[int, str]:
        if not self.tab_widget or self.tab_widget.count() == 0:
            logger.warning("No tabs available")
            return -1, ""
        current_index = self.tab_widget.currentIndex()
        current_name = self.tab_widget.tabText(current_index)
        return current_index, current_name