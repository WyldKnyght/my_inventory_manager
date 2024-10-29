# Custom Logging System

This document outlines the custom logging system implemented in the project.

## Overview

The custom logging system provides enhanced logging capabilities, including:

- Configurable log levels
- Ring buffer for storing recent log messages
- Rich console output
- File logging with rotation
- Decorators for error handling and temporary log level changes

## Components

### 1. Main Module (`__init__.py`)

The main module exports key functions and classes:

- `setup_logging`: Configures the logging system
- `error_handler`: Decorator for handling and logging errors
- `temporary_log_level`: Context manager for temporary log level changes
- `logger`: Pre-configured logger instance
- `get_logger`: Function to get a logger by name
- `get_update_logger`: Function to get a logger for updates
- `enable_file_logging`: Function to enable file logging
- `ConditionalFileHandler`: Custom file handler class

### 2. Constants (`constants.py`)

Defines constants used throughout the logging system:

- Log format strings
- Default logging configuration

### 3. Decorators (`decorators.py`)

Provides utility decorators:

- `error_handler`: For catching and logging exceptions
- `temporary_log_level`: For temporarily changing log levels

### 4. Handlers (`handlers.py`)

Custom logging handlers:

- `RingBuffer`: Stores recent log messages in a circular buffer
- `DetailedRichHandler`: Provides rich console output
- `ConditionalFileHandler`: Allows conditional file logging

### 5. File Logging Setup (`setup_file_logging.py`)

Functions for setting up file logging:

- `setup_file_logging`: Creates a file handler
- `get_update_logger`: Gets a logger for updates
- `enable_file_logging`: Enables logging to file

### 6. Logging Setup (`setup_logging.py`)

Main function for configuring the logging system:

- `setup_logging`: Sets up the entire logging configuration

## Usage

1. Import the necessary components from `utils.custom_logging`.
2. Call `setup_logging()` at the start of your application.
3. Use `logger` or `get_logger()` to obtain a logger instance.
4. Use the `@error_handler` decorator on functions that need error logging.
5. Use `with temporary_log_level(logger, level):` for temporary log level changes.

## Customization

The logging system can be customized by modifying the `DEFAULT_LOGGING_CONFIG` in `constants.py` or by passing a custom configuration to `setup_logging()`.

## File Logging

File logging is set up to use rotation, with a maximum file size of 10MB and keeping up to 5 backup files.

## Environment Variables

The log level can be set using the `LOG_LEVEL` environment variable.
