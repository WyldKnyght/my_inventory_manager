# src/user_interface/settings_tab.py
from user_interface.common.base_widget import BaseWidget
from user_interface.common.generic_management_dialog import GenericManagementDialog
from configs.ui_config import (
    SETTINGS_TAB_TITLE, DATA_MANAGEMENT_GROUP_TITLE, APP_SETTINGS_GROUP_TITLE,
    APP_SETTINGS_PLACEHOLDER, BUTTON_CONFIG
)

class SettingsTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(SETTINGS_TAB_TITLE)
        self.setup_ui()

    def setup_ui(self):
        """Set up the UI components for the Settings tab."""
        main_layout = self.create_vertical_layout(self)

        # Data Management group
        data_management_group = self.create_group_box(DATA_MANAGEMENT_GROUP_TITLE)
        data_management_layout = self.create_grid_layout()
        self.add_buttons_to_layout(data_management_layout)
        data_management_group.setLayout(data_management_layout)
        main_layout.addWidget(data_management_group)

        # Application Settings group (placeholder for future settings)
        app_settings_group = self.create_group_box(APP_SETTINGS_GROUP_TITLE)
        app_settings_layout = self.create_vertical_layout()
        placeholder_label = self.create_label(12, APP_SETTINGS_PLACEHOLDER)
        app_settings_layout.addWidget(placeholder_label)
        app_settings_group.setLayout(app_settings_layout)
        main_layout.addWidget(app_settings_group)

        # Add stretch to push groups to the top
        main_layout.addStretch()

    def add_buttons_to_layout(self, layout):
        """Add buttons to the grid layout."""
        buttons = BUTTON_CONFIG
        for i, (text, table_name) in enumerate(buttons):
            button = self.create_button(text, lambda _, tn=table_name: self.open_dialog(tn))
            row, col = divmod(i, 3)
            layout.addWidget(button, row, col)

    def open_dialog(self, table_name):
        """Open a management dialog for the specified table."""
        dialog = GenericManagementDialog(table_name, self)
        dialog.exec()