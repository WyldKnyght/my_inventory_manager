# src/user_interface/tabs/settings_tab.py

from user_interface.framework.base_widget import BaseWidget
from user_interface.dialogs.common.generic_management_dialog import GenericManagementDialog

class SettingsTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Set up the UI components for the Settings tab."""
        grid_layout = self.create_grid_layout(self)
        self.add_buttons_to_layout(grid_layout)
        self.configure_layout(grid_layout)

    def add_buttons_to_layout(self, layout):
        """Add buttons to the grid layout."""
        buttons = self.get_buttons_config()
        for i, (text, table_name) in enumerate(buttons):
            button = self.create_button(text, lambda _, tn=table_name: self.open_dialog(tn))
            row, col = divmod(i, 3)
            layout.addWidget(button, row, col)

    def configure_layout(self, layout):
        """Configure the layout spacing and margins."""
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

    def get_buttons_config(self):
        """Return the configuration for buttons."""
        return [
            ("Manage Categories", "Categories"),
            ("Manage Catalog", "Catalog"),
            ("Manage Unit Types", "UnitTypes")
        ]

    def open_dialog(self, table_name):
        """Open a management dialog for the specified table."""
        dialog = GenericManagementDialog(table_name, self)
        dialog.exec()