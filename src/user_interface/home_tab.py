# src/user_interface/home_tab.py
from user_interface.common.base_widget import BaseWidget
from configs.ui_config import HOME_TAB_TITLE

class HomeTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(HOME_TAB_TITLE)
        self.setup_ui()

    def setup_ui(self):
        # Setup UI for Home Tab
        pass