# src/main.py
import sys
from PyQt6 import QtWidgets
from user_interface.main_window import MainWindow

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()