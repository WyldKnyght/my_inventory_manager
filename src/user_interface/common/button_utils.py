# src/user_interface/common/button_utils.py
from PyQt6.QtWidgets import QHBoxLayout, QPushButton
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import BUTTON_STYLE

@ErrorManager.handle_errors()
def create_action_button(parent, text, action):
    """Create a button and connect it to an action."""
    button = QPushButton(text, parent)
    button.clicked.connect(action)
    button.setStyleSheet(BUTTON_STYLE)
    logger.debug(f"Created action button: {text}")
    return button

@ErrorManager.handle_errors()
def add_action_buttons(parent, actions):
    """Add action buttons to a layout."""
    layout = QHBoxLayout()
    for text, action in actions:
        button = create_action_button(parent, text, action)
        layout.addWidget(button)
    logger.debug(f"Added {len(actions)} action buttons to layout")
    return layout