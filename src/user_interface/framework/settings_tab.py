# src/user_interface/framework/settings_tab.py

from PyQt6 import QtWidgets
from user_interface.framework.base_widget import BaseWidget
from user_interface.dialogs.inventory.inventory_dialog import InventoryDialog
from user_interface.dialogs.general_dialog import GeneralDialog
from user_interface.dialogs.user_interface_dialog import UserInterfaceDialog
from user_interface.dialogs.reports_dialog import ReportsDialog
from user_interface.dialogs.purchases_dialog import PurchasesDialog
from user_interface.dialogs.sales_dialog import SalesDialog
from utils.ui_helpers import create_button  

class SettingsTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Create a new grid layout instance for this tab
        grid_layout = QtWidgets.QGridLayout(self)

        buttons = [
            ("General Settings", GeneralDialog),
            ("Inventory Management", InventoryDialog),
            ("User Interface Settings", UserInterfaceDialog),
            ("Purchases Settings", PurchasesDialog),
            ("Sales Settings", SalesDialog),
            ("Reports Settings", ReportsDialog)
        ]

        for i, (text, dialog_class) in enumerate(buttons):
            row = i // 3
            col = i % 3
            button = create_button(self, text, lambda _, dc=dialog_class: self.open_dialog(dc))
            grid_layout.addWidget(button, row, col)

        grid_layout.setSpacing(10)
        grid_layout.setContentsMargins(10, 10, 10, 10)

    def open_dialog(self, dialog_class):
        dialog = dialog_class(self)
        dialog.exec()
