# gui_sales.py
import tkinter as tk
from tkinter import ttk

class SalesTab:
    def __init__(self, notebook, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Sales")
        self.create_widgets()

    def create_widgets(self):
        # Create sales-specific widgets here
        pass