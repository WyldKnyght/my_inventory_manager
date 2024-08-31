from user_interface.common.base_widget import BaseWidget
from configs.ui_config import UIConfig, Titles
from utils.error_manager import ErrorManager
from utils.custom_logging import logger

class HomeTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(Titles.Tabs.HOME)
        self.setup_ui()

    @ErrorManager.handle_errors()
    def setup_ui(self):
        layout = self.create_vertical_layout()
        welcome_label = self.create_label(
            text=UIConfig.WELCOME_MESSAGE,
            font_size=UIConfig.FONT_SIZE
        )
        layout.addWidget(welcome_label)
        
        self.add_quick_access_buttons(layout)
        
        self.setLayout(layout)

    @ErrorManager.handle_errors()
    def add_quick_access_buttons(self, layout):
        for button_text, action in UIConfig.QUICK_ACCESS_BUTTONS:
            button = self.create_button(button_text, callback=self.button_clicked)
            layout.addWidget(button)

    @ErrorManager.handle_errors()
    def button_clicked(self):
        sender = self.sender()
        logger.info(f"Button clicked: {sender.text()}")
        # Implement the action associated with the button