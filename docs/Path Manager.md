# PathManager

The PathManager is a utility class that manages and provides access to the application's directory structure. It ensures that all necessary directories exist and offers methods to retrieve paths for various components of the application.

## Features

- Initializes and maintains the application's directory structure
- Provides easy access to all important directories
- Ensures all required directories exist
- Offers utility methods for path validation and manipulation

## Usage

### Initialization

The PathManager is implemented as a singleton. To use it, simply import the pre-initialized instance:

```python
from configs.path_manager import path_manager
```

### Accessing Directories

You can access various directories using the attributes of the PathManager:

```python
# Get the root directory
root_dir = path_manager.root_dir

# Get the source directory
src_dir = path_manager.src_dir

# Get the database directory
database_dir = path_manager.database_dir

# Get the user interface directory
ui_dir = path_manager.user_interface_dir

# Get a specific UI component directory
purchases_dir = path_manager.ui_purchases_dir
```

### Getting Configuration Paths

To get the path of a configuration YAML file:

```python
config_path = path_manager.get_config_yaml_path("database_config.yaml")
```

### Getting Database Paths

```python
# Get the main database file path
db_path = path_manager.get_database_path()

# Get the database schema file path
schema_path = path_manager.get_schema_path()
```

### Utility Methods

The PathManager also provides some utility methods:

```python
# Check if a file path is valid
is_valid = PathManager.is_valid_file_path("/path/to/file.txt")

# Get the directory of a file
directory = PathManager.get_directory("/path/to/file.txt")
```

## Directory Structure

The PathManager maintains the following directory structure:

```
my_inventory_manager/
├── database/
├── docs/
├── src
│   ├── configs
│   │   └── config_management
│   ├── controllers
│   │   ├── database
│   │   └── purchases
│   ├── resources
│   ├── user_interface
│   │   ├── common
│   │   │   └── base_widget_components
│   │   ├── inventory
│   │   ├── main_window_components
│   │   ├── purchases
│   │   │   └── dialogs
│   │   ├── reports
│   │   ├── sales
│   │   └── settings
│   └── utils
└── tests

## Best Practices

- Always use the PathManager to access directories and file paths in your application. This ensures consistency and makes it easier to manage the directory structure.
- If you need to add new directories to the application structure, update the PathManager accordingly.
- Use the utility methods provided by PathManager for path validation and manipulation to ensure consistency across your application.
