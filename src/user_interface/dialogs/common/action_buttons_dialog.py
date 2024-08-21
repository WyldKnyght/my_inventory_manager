# src/user_interface/dialogs/common/action_buttons_dialog.py
from utils.ui_helpers import add_action_buttons

def create_action_buttons(dialog):
    """Create action buttons and return their layout."""
    actions = [
        ("Add", dialog.add_entry),
        ("Edit", dialog.edit_entry),
        ("Delete", dialog.delete_entry),
        ("Exit", dialog.reject)
    ]
    return add_action_buttons(dialog, actions)

