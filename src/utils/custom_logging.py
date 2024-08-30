# src/utils/custom_logging.py
import logging
import logging.config
import os
import yaml
from rich.console import Console
from rich.theme import Theme
from typing import Any, Dict, Optional

# Constants for magic strings
LOG_ASCTIME = "asctime"
LOG_CREATED = "created"
LOG_FACILITY = "facility"
LOG_PID = "pid"
LOG_TID = "tid"
LOG_LEVEL = "level"
LOG_MODULE = "module"
LOG_FUNC = "func"
LOG_MSG = "msg"

# Logging format string
LOG_FORMAT = (
    f'{{ "{LOG_ASCTIME}":"%({LOG_ASCTIME})s", "{LOG_CREATED}":%({LOG_CREATED})f, '
    f'"{LOG_FACILITY}":"%({LOG_FACILITY})s", "{LOG_PID}":%({LOG_PID})d, '
    f'"{LOG_TID}":%({LOG_TID})d, "{LOG_LEVEL}":"%({LOG_LEVEL})s", '
    f'"{LOG_MODULE}":"%({LOG_MODULE})s", "{LOG_FUNC}":"%({LOG_FUNC})s", '
    f'"{LOG_MSG}":"%({LOG_MSG})s" }}'
)

# Module-specific logger
logger = logging.getLogger(__name__)

class RingBuffer(logging.StreamHandler):
    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.capacity = capacity
        self.buffer = []
        self.formatter = logging.Formatter(LOG_FORMAT)

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        self.buffer.append(msg)
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)

    def get(self) -> list[str]:
        return self.buffer

def load_yaml_config(config_file: str) -> Dict[str, Any]:
    """Load the YAML configuration file."""
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Configuration file {config_file} not found.") from e
    except yaml.YAMLError as error:
        raise RuntimeError(f"Error parsing YAML configuration file: {error}") from error

def setup_logging(config_file: Optional[str] = os.path.join('src', 'configs', 'logging_config.yaml')) -> None:
    config = load_yaml_config(config_file)

    # Dynamically set logging level from environment variables
    env_log_level = os.getenv("LOG_LEVEL", config['logging']['level'].upper())
    config['logging']['level'] = env_log_level

    # Validate required keys
    required_keys = ['logging', 'ring_buffer_capacity']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key '{key}' in configuration")

    # Use fileConfig to load logging configuration
    logging_config_file = config.get('logging_config_file')
    if logging_config_file and os.path.exists(logging_config_file):
        try:
            logging.config.fileConfig(logging_config_file)
        except Exception as e:
            print(f"Error loading logging configuration from file: {e}")
            # Fallback to dictionary configuration
            logging_config = {
                'version': 1,
                'disable_existing_loggers': False,
                'formatters': {
                    'default': {
                        'format': LOG_FORMAT
                    }
                },
                'handlers': {
                    'console': {
                        'class': 'rich.logging.RichHandler',
                        'formatter': 'default',
                        'level': config['logging']['level'],
                        'rich_tracebacks': True,
                        'console': Console(
                            log_time=True, 
                            log_time_format='%H:%M:%S-%f', 
                            theme=Theme({
                                "traceback.border": "black",
                                "traceback.border.syntax_error": "black",
                                "inspect.value.border": "black",
                            })
                        ),
                    },
                    'ring_buffer': {
                        'class': 'src.utils.logging_colors.RingBuffer',
                        'capacity': config['logging']['ring_buffer_capacity'],
                        'formatter': 'default',
                        'level': config['logging']['level'],
                    },
                },
                'loggers': {
                    __name__: {
                        'handlers': ['console', 'ring_buffer'],
                        'level': config['logging']['level'],
                    },
                }
            }

            logging.config.dictConfig(logging_config)

    # Suppress unnecessary logging from other libraries
    libraries_to_suppress = ["urllib3", "httpx", "diffusers", "torch"]
    for library in libraries_to_suppress:
        logging.getLogger(library).setLevel(logging.ERROR)

    logging.getLogger("lycoris").handlers = logging.getLogger(__name__).handlers

# Call setup_logging to initialize the logging system
setup_logging()