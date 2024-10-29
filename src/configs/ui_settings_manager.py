# src/configs/ui_settings_manager.py

from PyQt6.QtCore import QSettings, QByteArray
import os
from configs.path_config import UI_INI_PATH

class UiSettingsManager:
    def __init__(self):
        os.makedirs(os.path.dirname(UI_INI_PATH), exist_ok=True)
        self.settings = QSettings(UI_INI_PATH, QSettings.Format.IniFormat)

    def load_window_settings(self, main_window):
        if geometry := self.settings.value("geometry", QByteArray()):
            main_window.restoreGeometry(geometry)
        else:
            main_window.setGeometry(100, 100, 800, 600)

        if state := self.settings.value("windowState", QByteArray()):
            main_window.restoreState(state)

    def save_window_settings(self, main_window):
        self.settings.setValue("geometry", main_window.saveGeometry())
        self.settings.setValue("windowState", main_window.saveState())

    # Add more methods here for other settings as needed