# Custom Logging System Overview

The custom logging system is a comprehensive utility designed to provide flexible and detailed logging capabilities across the application. Here's an overview of its structure and key features:

1. `__init__.py`: 
   - Serves as the entry point for the logging system.
   - Imports and exposes main components and functions.
   - Provides a pre-configured logger and a function to get named loggers.

2. `constants.py`:
   - Defines constants for log record attributes.
   - Contains format strings for detailed and simple log formats.
   - Specifies default logging configuration.

3. `handlers.py`:
   - Implements custom logging handlers:
     - `RingBuffer`: Maintains a fixed-size buffer of recent log messages.
     - `DetailedRichHandler`: Provides rich console output with customizable themes.
     - `ConditionalFileHandler`: Allows conditional file logging with buffering capabilities.

4. `decorators.py`:
   - Offers utility decorators and context managers:
     - `error_handler`: A decorator for handling and logging exceptions.
     - `temporary_log_level`: A context manager for temporarily changing log levels.

5. `setup_file_logging.py`:
   - Provides functions for file-based logging:
     - `setup_file_logging()`: Creates a new log file with a timestamp.
     - `get_update_logger()`: Returns a logger configured for update operations.
     - `enable_file_logging()`: Activates file logging for a ConditionalFileHandler.

6. `setup_logging.py`:
   - Contains the main `setup_logging()` function to configure the logging system.
   - Allows for custom configuration or uses default settings.
   - Dynamically sets logging levels from environment variables.
   - Configures console, ring buffer, and file handlers.

Key Features:
- Flexible logging with console, file, and in-memory (ring buffer) options.
- Rich console output with customizable formatting.
- Dynamic log level configuration through environment variables.
- Detailed logging for debug levels and simpler formats for higher levels.
- Error handling decorator for consistent exception logging.
- Conditional file logging with buffering capabilities.
- Temporary log level changes for specific code blocks.
- Rotating file handler for managing log file sizes.

This logging system provides a robust and adaptable solution for application-wide logging needs, offering detailed debugging capabilities while maintaining performance through level-based formatting and conditional logging.
