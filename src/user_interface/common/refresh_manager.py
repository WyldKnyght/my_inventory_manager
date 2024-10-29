# src/user_interface/common/refresh_manager.py

class RefreshManager:
    def __init__(self):
        self.refresh_functions = []

    def add_refresh_function(self, func):
        self.refresh_functions.append(func)

    def refresh_all(self):
        for func in self.refresh_functions:
            func()
