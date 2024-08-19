# src/utils/config_loader.py
import json
import os
from dotenv import load_dotenv
from utils.logging_colors import logger

# Load environment variables from a .env file
load_dotenv()

def load_config():
    """Load configuration from a JSON file."""
    config_path = os.getenv('CONFIG_PATH', 'src/resources/config.json')

    if not os.path.isfile(config_path):
        logger.error(f"Configuration file does not exist: {config_path}")
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            config = validate_config(config)  # Validate and update the configuration
            return config
    except FileNotFoundError as e:
        logger.error(str(e))
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from the configuration file: {config_path}. Error: {str(e)}")
        raise
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        raise

def validate_config(config):
    """Validate the configuration data to ensure all required keys and values are present."""
    required_keys = {
        'main_window': {
            'width': int,
            'height': int,
            'title': str,
        },
        'tab_widget': {
            'tab_order': list
        }
    }

    default_config = {
        'main_window': {
            'width': 800,  # Example default value
            'height': 600,
            'title': "Default Title",
        },
        'tab_widget': {
            'tab_order': ["Home", "Inventory"]  # Default tab order
        }
    }

    for section, keys in required_keys.items():
        if section not in config:
            logger.warning(f"Section '{section}' is missing. Using default settings.")
            config[section] = default_config[section]
        else:
            for key, expected_type in keys.items():
                if key not in config[section]:
                    logger.warning(f"Key '{key}' in section '{section}' is missing. Using default value.")
                    config[section][key] = default_config[section][key]
                elif not isinstance(config[section][key], expected_type):
                    logger.warning(f"Value for key '{key}' in section '{section}' is incorrect type. Expected {expected_type.__name__}. Using default value.")
                    config[section][key] = default_config[section][key]

    return config