# src/user_interface/sales_tab.py
from user_interface.common.base_widget import BaseWidget
from configs.ui_config import SALES_TAB_TITLE

class SalesTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(SALES_TAB_TITLE)
        self.setup_ui()

    def setup_ui(self):
        # Setup UI for Sales Tab
        pass