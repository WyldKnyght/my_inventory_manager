# src/configs/path_config.py
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class EnvSettings:
    SETTINGS = {
        'PROJECT_ROOT': 'PROJECT_ROOT',
        'ENTRY_POINT': 'ENTRY_POINT',
        'BACKUP_DIR': 'BACKUP_DIR',
        'DB_PATH': 'DB_PATH',
        'FIN_SCHEMA_PATH': 'FIN_SCHEMA_PATH',
        'INV_SCHEMA_PATH': 'INV_SCHEMA_PATH',
        'GLB_SCHEMA_PATH': 'GLB_SCHEMA_PATH',
        'DEFAULT_SETTINGS_PATH': 'DEFAULT_SETTINGS_PATH',
        'UI_INI_PATH': 'UI_INI_PATH'
    }

    def __init__(self):
        self.PROJECT_ROOT = os.getenv('PROJECT_ROOT')
        if not self.PROJECT_ROOT:
            raise ValueError("PROJECT_ROOT must be set in the .env file")

        self.PROJECT_ROOT = Path(self.PROJECT_ROOT)

        for attr, env_var in self.SETTINGS.items():
            if attr != 'PROJECT_ROOT':
                if env_value := os.getenv(env_var):
                    setattr(self, attr, str(self.PROJECT_ROOT / env_value))
                else:
                    raise ValueError(f"{env_var} must be set in the .env file")

env_settings = EnvSettings()

# Expose the settings at the module level
for attr in EnvSettings.SETTINGS:
    globals()[attr] = getattr(env_settings, attr)