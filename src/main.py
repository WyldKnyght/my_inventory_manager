import json
import os
import sys
from PyQt6 import QtWidgets
from user_interface.tabs.main_tab import MainTab
from user_interface.tabs.inventory_tab import InventoryTab
from user_interface.tabs.sales_tab import SalesTab
from user_interface.tabs.purchases_tab import PurchasesTab
from user_interface.tabs.reports_tab import ReportsTab
from user_interface.tabs.settings_tab import SettingsTab
from dotenv import load_dotenv  


# Load environment variables from a .env file
load_dotenv()

def load_config():
    """Load configuration from a JSON file."""
    # Get the configuration path from an environment variable, with a default fallback
    config_path = os.getenv('CONFIG_PATH', 'src/resources/config.json')

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            # Validate the configuration structure
            if any(key not in config for key in ['main_window', 'tab_widget']):
                raise ValueError("Configuration file is missing required sections.")
            return config
    except FileNotFoundError:
        print(f"Configuration file not found: {config_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the configuration file: {config_path}")
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.setup_ui()

    def setup_ui(self):
        # Set up the main window
        self.setObjectName("MainWindow")
        self.resize(self.config['main_window']['width'], self.config['main_window']['height'])
        self.setWindowTitle(self.config['main_window']['title'])

        # Create a central widget and set a layout
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        # Use a vertical layout for the main window
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        # Create a QTabWidget and add it to the main layout
        tab_widget = QtWidgets.QTabWidget(central_widget)
        main_layout.addWidget(tab_widget)

        # Dictionary to hold tab instances
        tabs = {
            "Main": MainTab(),
            "Inventory": InventoryTab(),
            "Sales": SalesTab(),
            "Purchases": PurchasesTab(),
            "Reports": ReportsTab(),
            "Settings": SettingsTab()
        }

        # Add tabs in the order specified in the config
        for tab_name in self.config['tab_widget'].get('tab_order', []):
            if tab_name in tabs:
                tab_widget.addTab(tabs[tab_name], tab_name)

        # Set up the menu bar
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Set up the status bar
        self.status_bar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.status_bar)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Load configuration
    config_data = load_config()

    # Create and show the main window
    main_window = MainWindow(config_data)
    main_window.show()

    # Execute the application
    sys.exit(app.exec())