# src/user_interface/main_window/ui_setup.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_manager import ErrorManager

class UISetup:
    @ErrorManager.handle_errors()
    def setup_ui(self):
        """Set up the main UI components."""
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)
        self.tab_widget = self.create_tab_widget(central_widget)
        main_layout.addWidget(self.tab_widget)
        logger.debug("Main UI components set up")

    @ErrorManager.handle_errors()
    def create_tab_widget(self, parent: QtWidgets.QWidget) -> QtWidgets.QTabWidget:
        """Create and configure the tab widget with all necessary tabs."""
        self.tab_widget = QtWidgets.QTabWidget(parent)
        self.add_tabs(self.tab_widget)
        logger.debug("Tab widget created and configured")
        return self.tab_widget

    @ErrorManager.handle_errors()
    def check_initialization(self) -> bool:
        if not hasattr(self, 'tab_widget'):
            logger.error("MainWindow's tab_widget not created")
            return False
        if not isinstance(self.tab_widget, QtWidgets.QTabWidget):
            logger.error("MainWindow's tab_widget is not a QTabWidget")
            return False
        if self.tab_widget.count() == 0:
            logger.error("MainWindow's tab_widget has no tabs")
            return False
        return True