# src/controllers/sales_controller.py

from controllers.database_controller import DatabaseController

class SalesController:
    def __init__(self):
        self.db_controller = DatabaseController()
