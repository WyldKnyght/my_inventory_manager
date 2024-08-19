import sys
from PyQt6 import QtWidgets
from utils.config_loader import load_config
from user_interface.main_window import MainWindow
from utils.logging_colors import setup_logging, logger

def handle_initialization_error(e):
    logger.error(f"Initialization error: {e}")
    raise

def initialize_app():
    app = QtWidgets.QApplication(sys.argv)

    try:
        config_data = load_config()
    except Exception as e:
        handle_initialization_error(e)

    main_window = MainWindow(config_data)
    main_window.show()

    return app

def run_app():
    setup_logging() 
    try:
        app = initialize_app()
    except Exception as e:
        logger.error(f"Failed to initialize the application: {e}")
        return

    try:
        sys.exit(app.exec())
    except SystemExit as e:
        logger.info(f"Application exited with code: {e}")
        raise  # Re-raise SystemExit to stop the application
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise  # Re-raise the exception to stop the application
    finally:
        # Only quit the app if it was successfully initialized
        if app:
            app.quit()
            
if __name__ == "__main__":
    run_app()