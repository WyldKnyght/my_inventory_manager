# src/user_interface/main_window.py

from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget
from PyQt6.QtGui import QCloseEvent
from controllers.ui_modules.main_window_controller import MainWindowController
from configs.constants import APP_TITLE, APP_VERSION
from utils.custom_logging import logger
from .common.show_about_dialog import show_about_dialog
from .common.refresh_manager import RefreshManager
from .main_window_modules.main_window_initializer import MainWindowInitializer
from .main_window_modules.ui_operations_handler import UIOperationsHandler
from .tabs.financial_tab import FinancialTab
from .tabs.inventory_tab import InventoryTab

class MainWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.controller = MainWindowController(self, db_manager)
        self.refresh_manager = RefreshManager()
        
        self.setWindowTitle(f"{APP_TITLE} v{APP_VERSION}")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.financial_tab = FinancialTab(self.db_manager)
        self.tab_widget.addTab(self.financial_tab, "Financial")

        # Inventory Tab
        self.inventory_tab = InventoryTab(self.db_manager)
        self.tab_widget.addTab(self.inventory_tab, "Inventory")

        initializer = MainWindowInitializer(self, db_manager)
        initializer.initialize()

        self.ui_operations = UIOperationsHandler(self, self.controller)

        self.load_settings()

    def closeEvent(self, event: QCloseEvent):
        try:
            self.save_settings()
        except Exception as e:
            logger.error(f"Error during application close: {str(e)}")
        finally:
            super().closeEvent(event)

    def load_settings(self):
        self.controller.load_settings()

    def save_settings(self):
        self.controller.save_settings()

    def show_about_dialog(self):
        show_about_dialog(self)