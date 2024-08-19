# src/user_interface/main_window.py

from PyQt6 import QtWidgets
from user_interface.framework.home_tab import HomeTab
from user_interface.framework.inventory_tab import InventoryTab
from user_interface.framework.sales_tab import SalesTab
from user_interface.framework.purchases_tab import PurchasesTab
from user_interface.framework.reports_tab import ReportsTab
from user_interface.framework.settings_tab import SettingsTab

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.setup_ui()

    def setup_ui(self):
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        self.setObjectName("MainWindow")
        self.resize(self.config['main_window']['width'], self.config['main_window']['height'])
        self.setWindowTitle(self.config['main_window']['title'])

        self.setMinimumSize(800, 600)
        self.setMaximumSize(screen_width, screen_height)

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)

        tab_widget = QtWidgets.QTabWidget(central_widget)
        tab_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        main_layout.addWidget(tab_widget)

        tabs = {
            "Home": HomeTab(),
            "Inventory": InventoryTab(),
            "Sales": SalesTab(),
            "Purchases": PurchasesTab(),
            "Reports": ReportsTab(),
            "Settings": SettingsTab()
        }

        for tab_name in self.config['tab_widget'].get('tab_order', []):
            if tab_name in tabs:
                tab_widget.addTab(tabs[tab_name], tab_name)

        self.menu_bar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.status_bar)
