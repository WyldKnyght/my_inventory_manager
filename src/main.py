# src/main.py
import sys
from PyQt6 import QtWidgets
from user_interface.main_window_components import MainWindow
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.config_manager import config_manager

@ErrorManager.handle_errors()
def initialize_app():
    """Initialize the application and apply styles."""
    app = QtWidgets.QApplication(sys.argv)
    
    # Initialize ConfigManager (if not already done)
    config_manager._initialize()
    
    # Apply styles
    config_manager.apply_styles()
    
    logger.info("Application initialized and styles applied")
    return app

@ErrorManager.handle_errors()
def run_app():
    """Initialize and run the main application."""
    app = initialize_app()
    
    main_window = MainWindow()
    main_window.show()
    logger.info("Main window displayed")
    
    sys.exit(app.exec())

if __name__ == "__main__":
    try:
        run_app()
    except Exception as e:
        logger.critical(f"Unhandled exception: {str(e)}")
        sys.exit(1)