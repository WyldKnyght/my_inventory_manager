# ErrorManager

The ErrorManager is a utility class that provides error handling and logging functionality for the application. It offers a decorator for wrapping functions with error handling and methods for logging errors and displaying critical error messages.

## Features

- Decorator for handling exceptions in functions
- Customizable error handling behavior
- Logging of errors with different severity levels
- Display of critical error messages to the user

## Usage

### Error Handling Decorator

The `handle_errors` decorator can be used to wrap functions with error handling:

```python
from utils.error_manager import ErrorManager

@ErrorManager.handle_errors(default_value=None, reraise=False)
def some_function():
    # Function implementation
    pass
```

#### Decorator Parameters

- `default_value`: The value to return if an exception occurs (default: None)
- `reraise`: Whether to re-raise the caught exception (default: False)
- `ignore_exceptions`: Tuple of exception types to ignore (default: ())
- `log_exceptions`: Tuple of exception types to log (default: None, meaning log all)
- `log_level`: The logging level to use ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")

### Using the Decorated Function

When using a function decorated with `handle_errors`, the return value will be a dictionary with the following keys:

- `success`: Boolean indicating if the function executed successfully
- `data`: The return value of the function (or the default value if an error occurred)
- `is_default`: Boolean indicating if the default value was returned due to an error
- `error`: Error message (if an error occurred, otherwise None)
- `exception_type`: The type of exception that occurred (if any)
- `stack_trace`: The stack trace of the error (if any)

Example:

```python
result = some_function()
if result['success']:
    # Process the result
    data = result['data']
else:
    # Handle the error
    error_message = result['error']
    exception_type = result['exception_type']
    stack_trace = result['stack_trace']
```

### Logging Errors

To manually log an error:

```python
ErrorManager.log_error(
    function_name="my_function",
    error_message="An error occurred",
    stack_trace=traceback.format_exc(),
    log_level="ERROR"
)
```

### Handling Critical Errors

To display a critical error message to the user:

```python
try:
    # Some critical operation
except Exception as e:
    ErrorManager.handle_critical_error(e, parent_widget)
```

## Best Practices

- Use the `handle_errors` decorator for functions that may raise exceptions, especially in areas where graceful error handling is crucial.
- Choose appropriate `log_level` values based on the severity of the error.
- Use `handle_critical_error` for errors that require immediate user attention and potentially application termination.
- Always provide meaningful error messages to aid in debugging and user understanding.
