# src/configs/config_management/general_config.py
import yaml
import os
from utils.error_manager import ErrorManager
from configs.path_manager import path_manager

class GeneralConfig:
    def __init__(self):
        self._load_config()

    def _load_config(self):
        config_path = os.path.join(path_manager.configs_dir, 'config_management', 'general_config.yaml')
        with open(config_path, 'r') as f:
            self.general_config = yaml.safe_load(f)

    @ErrorManager.handle_errors(default_value="DEBUG")
    def get_log_level(self) -> str:
        return self.general_config['logging']['level']

    @ErrorManager.handle_errors(default_value=100)
    def get_log_buffer_capacity(self) -> int:
        return self.general_config['logging']['ring_buffer_capacity']

    @ErrorManager.handle_errors(default_value="")
    def get_styles_path(self) -> str:
        return self.general_config['paths']['styles']
