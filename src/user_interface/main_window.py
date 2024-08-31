from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import UIConfig, Titles
from .main_window_components import UISetup, TabManagement, Configuration

class MainWindow(QtWidgets.QMainWindow, UISetup, TabManagement, Configuration):
    def __init__(self):
        super().__init__()
        self.tab_widget: QtWidgets.QTabWidget = None
        self.setWindowTitle(Titles.MAIN_WINDOW)
        self.resize(*UIConfig.MAIN_WINDOW_SIZE)
        self.setup_ui()
        logger.info("Main window initialized")
        if not self.check_initialization():
            QtWidgets.QMessageBox.warning(self, "Warning", "MainWindow not properly initialized. Some features may not work correctly.")

    @ErrorManager.handle_errors()
    def get_tab_widget(self) -> QtWidgets.QTabWidget:
        if not self.tab_widget:
            raise AttributeError("tab_widget has not been initialized")
        return self.tab_widget