# my_inventory_manager
Creating an inventory management system

## Utility functions:
For logging:
- Ensure consistent use of logging across the application.
- Use logger.debug(), logger.info(), logger.warning(), logger.error(), and logger.critical() for appropriate log levels.

For path management:
- Ensure consistent use of path management across the application.
- Access paths and perform file operations using path_manager.method() to maintain consistency.
- Update PathManager if new paths are introduced during refactoring.

For error handling:
- Use the ErrorManager class from utils/error_manager.py.
- Apply the @ErrorManager.handle_errors() decorator to functions that need error handling.
- Use best judgment for specific error handling scenarios.
- This decorator catches exceptions, logs them, and returns a standardized dictionary with error information.
- Customize behavior by specifying default values, reraising exceptions, ignoring specific exceptions, and setting log levels.
- Handle the returned dictionary appropriately in the calling code.