# src/user_interface/common/form_input_widgets.py
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QHBoxLayout 
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import CURRENCIES, DIMENSION_UNITS, WEIGHT_UNITS

@ErrorHandler.handle_errors()
def create_combobox(parent, items, data_callback=None):
    """Create a combo box and populate it with items or using a data callback."""
    combo_box = QtWidgets.QComboBox(parent)
    if data_callback:
        populate_combobox(combo_box, data_callback)
    else:
        combo_box.addItems(items)
    logger.debug(f"Created combobox with {len(items)} items")
    return combo_box

@ErrorHandler.handle_errors()
def populate_combobox(combo_box, data_callback):
    """Populate a combo box using a data callback function."""
    try:
        items = data_callback()
        combo_box.addItems(items)
        logger.debug(f"Populated combobox with {len(items)} items from callback")
    except Exception as e:
        logger.error(f"An error occurred while fetching data for combobox: {e}")

@ErrorHandler.handle_errors()
def create_dimension_field(parent):
    """Create a field for dimension input."""
    line_edit = QtWidgets.QLineEdit(parent)
    line_edit.setValidator(QtGui.QDoubleValidator(0.0, 10000.0, 2))
    logger.debug("Created dimension field")
    return create_widget_with_line_edit_and_combobox(parent, DIMENSION_UNITS)

@ErrorHandler.handle_errors()
def create_unit_field(parent, units):
    """Create a field with a unit combo box."""
    return create_widget_with_line_edit_and_combobox(parent, units)

@ErrorHandler.handle_errors()
def create_widget_with_line_edit_and_combobox(parent, combo_items):
    """Create a widget with a line edit and a combo box."""
    widget = QtWidgets.QWidget(parent)
    layout = QHBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)

    line_edit = QtWidgets.QLineEdit(parent)
    line_edit.setValidator(QtGui.QDoubleValidator(0.0, 10000.0, 2))

    combo_box = QtWidgets.QComboBox(parent)
    combo_box.addItems(combo_items)
    combo_box.setCurrentIndex(0)

    layout.addWidget(line_edit)
    layout.addWidget(combo_box)
    logger.debug(f"Created widget with line edit and combobox ({len(combo_items)} items)")
    return widget

@ErrorHandler.handle_errors()
def create_currency_field(parent):
    """Create a field for currency input."""
    return create_widget_with_line_edit_and_combobox(parent, CURRENCIES)

@ErrorHandler.handle_errors()
def create_weight_field(parent):
    """Create a field for weight input."""
    return create_widget_with_line_edit_and_combobox(parent, WEIGHT_UNITS)