# src/controllers/db_modules/db_settings_manager.py

class SettingsManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_setting(self, setting_name: str) -> str:
        """Retrieve a setting value."""
        query = "SELECT setting_value FROM Global_Settings WHERE setting_name = ?"
        result = self.db_manager.execute_query(query, (setting_name,))
        return result[0][0] if result else None

    def update_setting(self, setting_name: str, setting_value: str):
        """Update a setting value."""
        command = """
        UPDATE Global_Settings
        SET setting_value = ?
        WHERE setting_name = ?
        """
        return self.db_manager.execute_command(command, (setting_value, setting_name))

    # Add more settings-related methods here