# main_gui.py
import tkinter as tk
from tkinter import ttk
from user_interface.gui_inventory import InventoryTab
from user_interface.gui_sales import SalesTab
from user_interface.gui_purchases import PurchasesTab
from user_interface.gui_reports import ReportsTab
from user_interface.app_mediator import AppMediator

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Database Management System")
        self.mediator = AppMediator()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        self.inventory_tab = InventoryTab(self.notebook, self.mediator)
        self.sales_tab = SalesTab(self.notebook, self.mediator)
        self.purchases_tab = PurchasesTab(self.notebook, self.mediator)
        self.reports_tab = ReportsTab(self.notebook, self.mediator)

        # Set tabs in mediator
        self.mediator.set_inventory(self.inventory_tab)
        self.mediator.set_sales(self.sales_tab)
        self.mediator.set_purchases(self.purchases_tab)
        self.mediator.set_reports(self.reports_tab)

    def run(self):
        self.root.mainloop()

def start_app():
    app = Application()
    app.run()