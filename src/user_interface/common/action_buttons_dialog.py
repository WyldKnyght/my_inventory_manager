# src/user_interface/common/action_buttons_dialog.py
from user_interface.common.button_utils import add_action_buttons
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import ACTION_BUTTON_LABELS

@ErrorHandler.handle_errors()
def create_action_buttons(dialog):
    """Create action buttons and return their layout."""
    actions = [
        (ACTION_BUTTON_LABELS['add'], dialog.add_entry),
        (ACTION_BUTTON_LABELS['edit'], dialog.edit_entry),
        (ACTION_BUTTON_LABELS['delete'], dialog.delete_entry),
        (ACTION_BUTTON_LABELS['exit'], dialog.reject)
    ]
    layout = add_action_buttons(dialog, actions)
    logger.debug(f"Created action buttons: {[action[0] for action in actions]}")
    return layout