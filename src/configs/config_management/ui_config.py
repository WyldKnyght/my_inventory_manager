# src/configs/config_management/ui_config.py
import yaml
import os
from typing import Tuple, List
from PyQt6 import QtCore
from PyQt6.QtWidgets import QSizePolicy
from utils.error_manager import ErrorManager
from configs.path_manager import path_manager

class UIConfig:
    def __init__(self):
        self._load_config()

    def _load_config(self):
        config_path = os.path.join(path_manager.configs_dir, 'config_management', 'ui_config.yaml')
        with open(config_path, 'r') as f:
            self.ui_config = yaml.safe_load(f)

    @ErrorManager.handle_errors(default_value=(800, 600))
    def get_window_size(self, window_type: str) -> Tuple[int, int]:
        return tuple(self.ui_config['window_sizes'].get(window_type, (800, 600)))

    @ErrorManager.handle_errors(default_value=12)
    def get_font_size(self) -> int:
        return self.ui_config.get('font_size', 12)

    @ErrorManager.handle_errors(default_value=30)
    def get_button_height(self) -> int:
        return self.ui_config.get('button_height', 30)

    @ErrorManager.handle_errors(default_value=10)
    def get_padding(self) -> int:
        return self.ui_config.get('padding', 10)

    @ErrorManager.handle_errors(default_value="")
    def get_title(self, title_type: str) -> str:
        return self.ui_config.get('titles', {}).get(title_type, "")

    @ErrorManager.handle_errors(default_value="")
    def get_tab_title(self, tab_name: str) -> str:
        return self.ui_config.get('tabs', {}).get(tab_name, "")

    @ErrorManager.handle_errors(default_value="")
    def get_subtab_title(self, subtab_name: str) -> str:
        return self.ui_config.get('subtabs', {}).get(subtab_name, "")

    @ErrorManager.handle_errors(default_value="")
    def get_group_title(self, group_name: str) -> str:
        return self.ui_config.get('group_titles', {}).get(group_name, "")

    @ErrorManager.handle_errors(default_value="")
    def get_placeholder(self, placeholder_name: str) -> str:
        return self.ui_config.get('placeholders', {}).get(placeholder_name, "")

    @ErrorManager.handle_errors(default_value="")
    def get_button_text(self, button_name: str) -> str:
        return self.ui_config.get('buttons', {}).get(button_name, "")

    @ErrorManager.handle_errors(default_value="")
    def get_action_button_label(self, action_name: str) -> str:
        return self.ui_config.get('action_button_labels', {}).get(action_name, "")

    @ErrorManager.handle_errors(default_value="")
    def get_dialog_button_label(self, button_name: str) -> str:
        return self.ui_config.get('dialog_button_labels', {}).get(button_name, "")

    @ErrorManager.handle_errors(default_value=[])
    def get_button_config(self) -> List[Tuple[str, str]]:
        return self.ui_config.get('button_config', [])

    @ErrorManager.handle_errors(default_value="")
    def get_message_title(self, message_type: str) -> str:
        return self.ui_config.get('message_titles', {}).get(message_type, "")

    @ErrorManager.handle_errors(default_value=[])
    def get_table_headers(self, table_name: str) -> List[str]:
        return self.ui_config.get('table_headers', {}).get(table_name, [])

    @ErrorManager.handle_errors(default_value=100)
    def get_field_width(self, width_type: str) -> int:
        return self.ui_config.get('field_widths', {}).get(width_type, 100)

    @ErrorManager.handle_errors(default_value=[])
    def get_units(self, unit_type: str) -> List[str]:
        return self.ui_config.get('units', {}).get(unit_type, [])

    # Constants
    DEFAULT_ALIGNMENT = QtCore.Qt.AlignmentFlag.AlignCenter
    TABLE_POLICY = (QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)