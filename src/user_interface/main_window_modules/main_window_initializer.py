# src/user_interface/main_window_modules/main_window_initializer.py

class MainWindowInitializer:
    def __init__(self, main_window, db_manager):
        self.main_window = main_window
        self.db_manager = db_manager

    def initialize(self):
        self.create_menu_bar()
        self.create_status_bar()

    def create_menu_bar(self):
        menu_bar = self.main_window.menuBar()

        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Exit", self.main_window.close)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("About", self.main_window.show_about_dialog)

    def create_status_bar(self):
        self.main_window.statusBar().showMessage("Ready")

