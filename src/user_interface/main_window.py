# src/user_interface/main_window.py

from PyQt6 import QtWidgets
from user_interface.framework.home_tab import HomeTab
from user_interface.framework.inventory_tab import InventoryTab
from user_interface.framework.settings_tab import SettingsTab
from user_interface.framework.purchases_tab import PurchasesTab

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt Application")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        """Set up the main UI components."""
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)
        tab_widget = self.create_tab_widget(central_widget)
        main_layout.addWidget(tab_widget)

    def create_tab_widget(self, parent):
        """Create and configure the tab widget with all necessary tabs."""
        tab_widget = QtWidgets.QTabWidget(parent)
        self.add_tabs(tab_widget)
        return tab_widget

    def add_tabs(self, tab_widget):
        """Add all tabs to the tab widget."""
        tabs = [
            (HomeTab(), "Home"),
            (InventoryTab(), "Inventory"),
            (SettingsTab(), "Settings"),
            (PurchasesTab(), "Purchases"),
        ]
        for tab, name in tabs:
            tab_widget.addTab(tab, name)