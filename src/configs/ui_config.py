# src/configs/ui_config.py
"""UI configuration constants loaded from ui_config.yaml."""

from PyQt6 import QtCore
from PyQt6.QtWidgets import QSizePolicy
from configs.config_manager import config_manager

class UIConfig:
    """General UI settings."""
    MAIN_WINDOW_SIZE = config_manager.get('ui.main_window_size', (800, 600))
    DIALOG_SIZE = config_manager.get('ui.dialog_size', (1000, 800))
    FONT_SIZE = config_manager.get('ui.font_size', 10)
    BUTTON_HEIGHT = config_manager.get('ui.button_height', 30)
    PADDING = config_manager.get('ui.padding', 10)
    DEFAULT_FONT_SIZE = config_manager.get('ui.default_font_size', 12)
    DEFAULT_ALIGNMENT = QtCore.Qt.AlignmentFlag.AlignCenter

class Titles:
    """Window, dialog, and tab titles."""
    MAIN_WINDOW = config_manager.get('ui.main_window_title', "Inventory Management System")
    SETTINGS_DIALOG = config_manager.get('ui.dialog_titles.settings', "General Settings")
    PURCHASE_ORDER_DIALOG = config_manager.get('ui.dialog_titles.purchase_order', "Purchase Order")
    INVENTORY_DIALOG = config_manager.get('ui.dialog_titles.inventory', "Inventory Management")
    EDIT_RECORD = config_manager.get('ui.dialog_titles.edit_record', "Edit Record")
    DELETE_RECORD = config_manager.get('ui.dialog_titles.delete_record', "Delete Record")
    CONFIRM_DELETION = config_manager.get('ui.dialog_titles.confirm_deletion', "Confirm Deletion")

    class Tabs:
        """Tab titles."""
        HOME = config_manager.get('ui.tab_titles.home', "Home")
        INVENTORY = config_manager.get('ui.tab_titles.inventory', "Inventory")
        PURCHASES = config_manager.get('ui.tab_titles.purchases', "Purchases")
        REPORTS = config_manager.get('ui.tab_titles.reports', "Reports")
        SALES = config_manager.get('ui.tab_titles.sales', "Sales")
        SETTINGS = config_manager.get('ui.tab_titles.settings', "Settings")

    class Subtabs:
        """Subtab titles."""
        PURCHASES = config_manager.get('ui.subtab_titles.purchases', "Purchases")
        EXPENSES = config_manager.get('ui.subtab_titles.expenses', "Expenses")

    class GroupBoxes:
        """Group box titles."""
        SEARCH = config_manager.get('ui.group_titles.search', "Search")
        CATALOG = config_manager.get('ui.group_titles.catalog', "Inventory Catalog")
        PURCHASES = config_manager.get('ui.group_titles.purchases', "Purchases")
        ACTIONS = config_manager.get('ui.group_titles.actions', "Actions")
        DATA_MANAGEMENT = config_manager.get('ui.group_titles.data_management', "Data Management")
        APP_SETTINGS = config_manager.get('ui.group_titles.app_settings', "Application Settings")

class Placeholders:
    """Placeholder texts."""
    SETTINGS = config_manager.get('ui.placeholders.settings', "General settings configuration goes here.")
    SEARCH = config_manager.get('ui.placeholders.search', "Search...")
    EXPENSES = config_manager.get('ui.placeholders.expenses', "Expenses tab content will be implemented here.")
    APP_SETTINGS = config_manager.get('ui.placeholders.app_settings', "Application settings will be added here.")

class Buttons:
    """Button texts and configurations."""
    ADD = config_manager.get('ui.button_texts.add', "Add")
    EDIT = config_manager.get('ui.button_texts.edit', "Edit")
    DELETE = config_manager.get('ui.button_texts.delete', "Delete")
    SAVE = config_manager.get('ui.button_texts.save', "Save")
    CANCEL = config_manager.get('ui.button_texts.cancel', "Cancel")

    ACTION_LABELS = config_manager.get('ui.action_button_labels', {
        'add': "Add",
        'edit': "Edit",
        'delete': "Delete",
        'exit': "Exit"
    })

    DIALOG_LABELS = config_manager.get('ui.dialog_button_labels', {
        'save': "Save",
        'cancel': "Cancel"
    })

    CONFIG = config_manager.get('ui.button_config', [
        ("Manage Categories", "Categories"),
        ("Manage Catalog", "Catalog"),
        ("Manage Unit Types", "UnitTypes")
    ])

class MessageBoxTitles:
    """Message box titles."""
    ERROR = config_manager.get('ui.message_titles.error', "Error")
    WARNING = config_manager.get('ui.message_titles.warning', "Warning")
    INFO = config_manager.get('ui.message_titles.info', "Information")
    CONFIRM = config_manager.get('ui.message_titles.confirm', "Confirm")

class TableSettings:
    """Table settings."""
    POLICY = (QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    HEADERS = config_manager.get('ui.table_headers', {
        "purchase_order_items": ["Product", "Quantity", "Unit Price", "Total", ""],
        "inventory": ["ID", "Item Number", "Name", "Description", "Quantity", "Price"],
    })

class FormFieldSizes:
    """Form field sizes."""
    SHORT = config_manager.get('ui.field_widths.short', 100)
    MEDIUM = config_manager.get('ui.field_widths.medium', 200)
    LONG = config_manager.get('ui.field_widths.long', 300)

class Units:
    """Currency and units."""
    CURRENCIES = config_manager.get('ui.currencies', ['CAD', 'USD'])
    PURCHASE_STATUSES = config_manager.get('ui.purchase_statuses', ['Pending', 'Shipped', 'Delivered'])
    DIMENSION_UNITS = config_manager.get('ui.dimension_units', ['cm', 'in'])
    WEIGHT_UNITS = config_manager.get('ui.weight_units', ['kg', 'lb'])

class Styles:
    """UI styles."""
    BUTTON = config_manager.get('ui.button_style', """
        QPushButton {
            background-color: #4a86e8;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #3a76d8;
        }
    """)

    TABLE = config_manager.get('ui.table_style', """
        QTableWidget {
            background-color: #ffffff;
            alternate-background-color: #f0f0f0;
        }
        QHeaderView::section {
            background-color: #4a86e8;
            color: white;
            padding: 5px;
        }
    """)