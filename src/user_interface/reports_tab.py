# src/user_interface/tabs/reports_tab.py
from user_interface.common.base_widget import BaseWidget
from configs.ui_config import REPORTS_TAB_TITLE

class ReportsTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(REPORTS_TAB_TITLE)
        self.setup_ui()

    def setup_ui(self):
        # Setup UI for Reports Tab
        pass