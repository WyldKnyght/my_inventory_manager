# Configuration Management System

The Configuration Management System is designed to handle various configuration settings for the application, including database, UI, and general settings. It provides a centralized and organized way to manage and access configuration data.

## Structure

The configuration system is organized as follows:

- `src/configs/config_manager.py`: Main configuration manager
- `src/configs/config_management/`:
  - `__init__.py`: Exports configuration classes
  - `database_config.py`: Handles database-specific configurations
  - `database_config.yaml`: Database configuration data
  - `ui_config.py`: Handles UI-specific configurations
  - `ui_config.yaml`: UI configuration data
  - `general_config.py`: Handles general application configurations
  - `general_config.yaml`: General configuration data

## Usage

### Initializing the Configuration Manager

```python
from configs.config_manager import config_manager

# The config_manager is a singleton and is automatically initialized
```

### Accessing Database Configurations

```python
# Get the primary key for a table
primary_key = config_manager.get_primary_key("Categories")

# Get fields for a table
fields = config_manager.get_table_fields("Vendors")

# Get a database query
query = config_manager.get_database_query("purchases", "add_purchase")

# Get database path
db_path = config_manager.get_database_path()
```

### Accessing UI Configurations

```python
# Get window size
main_window_size = config_manager.get_window_size("main")

# Get font size
font_size = config_manager.get_font_size()

# Get a title
main_title = config_manager.get_title("main_window")

# Get a button text
add_button_text = config_manager.get_button_text("add")

# Get table headers
headers = config_manager.get_table_headers("inventory")
```

### Accessing General Configurations

```python
# Get log level
log_level = config_manager.get_log_level()

# Get log buffer capacity
buffer_capacity = config_manager.get_log_buffer_capacity()

# Get styles path
styles_path = config_manager.get_styles_path()
```

### Updating Configurations

```python
# Update a configuration value
config_manager.update("ui.font_size", 14)

# Reload configurations (e.g., after manual YAML file edit)
config_manager.reload_configs()
```

## Extending the Configuration System

To add new configuration options:

1. Add the new configuration to the appropriate YAML file.
2. Add a corresponding method in the relevant configuration class (DatabaseConfig, UIConfig, or GeneralConfig).
3. If needed, update the ConfigManager class to expose the new method.

## Best Practices

- Use type hints and default values in configuration methods for better code clarity and error handling.
- Keep YAML files organized and well-commented for easy maintenance.
- Use the ErrorManager decorator for all configuration access methods to ensure graceful error handling.
