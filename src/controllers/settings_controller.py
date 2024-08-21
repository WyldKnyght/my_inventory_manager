# src/controllers/settings_controller.py

from controllers.database_controller import DatabaseController

class SettingsController:
    def __init__(self):
        self.db_controller = DatabaseController()
