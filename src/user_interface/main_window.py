# src/user_interface/main_window.py
from PyQt6 import QtWidgets
from user_interface.home_tab import HomeTab
from user_interface.inventory_tab import InventoryTab
from user_interface.settings_tab import SettingsTab
from user_interface.purchases_tab import PurchasesTab
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.config_manager import config_manager
from configs.ui_config import MAIN_WINDOW_SIZE, MAIN_WINDOW_TITLE

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.resize(*MAIN_WINDOW_SIZE)
        self.setup_ui()
        logger.info("Main window initialized")

    @ErrorHandler.handle_errors()
    def setup_ui(self):
        """Set up the main UI components."""
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)
        self.tab_widget = self.create_tab_widget(central_widget)
        main_layout.addWidget(self.tab_widget)
        logger.debug("Main UI components set up")

    @ErrorHandler.handle_errors()
    def create_tab_widget(self, parent):
        """Create and configure the tab widget with all necessary tabs."""
        tab_widget = QtWidgets.QTabWidget(parent)
        self.add_tabs(tab_widget)
        logger.debug("Tab widget created and configured")
        return tab_widget

    @ErrorHandler.handle_errors()
    def add_tabs(self, tab_widget):
        """Add all tabs to the tab widget."""
        tabs = [
            (HomeTab(), config_manager.get('ui.tab_names.home', "Home")),
            (InventoryTab(), config_manager.get('ui.tab_names.inventory', "Inventory")),
            (SettingsTab(), config_manager.get('ui.tab_names.settings', "Settings")),
            (PurchasesTab(), config_manager.get('ui.tab_names.purchases', "Purchases")),
        ]
        for tab, name in tabs:
            tab_widget.addTab(tab, name)
        logger.debug(f"Added {len(tabs)} tabs to the tab widget")