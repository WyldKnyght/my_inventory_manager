# src/main.py
import sys
from PyQt6.QtWidgets import QApplication
from user_interface.main_window import MainWindow
from controllers.db_modules.database_manager import DatabaseManager
from utils.custom_logging import setup_logging, logger

setup_logging()

def main():
    app = QApplication(sys.argv)
    logger.info("Starting application...")

    db_manager = DatabaseManager()
    db_manager.initialize_database()  # Initialize the database

    window = MainWindow(db_manager)
    window.show()
    logger.info("Application started successfully.")

    exit_code = app.exec()
    sys.exit(exit_code)
    logger.info("Application closed.")

if __name__ == "__main__":
    main()