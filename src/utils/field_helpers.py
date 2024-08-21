# src\utils\field_helpers.py
import sqlite3
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QHBoxLayout 
from controllers.database_controller import DatabaseController

def create_combobox(parent, field_name, table_name):
    """Create a combo box for a foreign key field."""
    combo_box = QtWidgets.QComboBox(parent)
    query = f"SELECT {field_name} FROM {table_name}"
    populate_combobox(combo_box, query)
    return combo_box

def populate_combobox(combo_box, query):
    """Populate a combo box with data from a query."""
    db_controller = DatabaseController()
    try:
        with sqlite3.connect(db_controller.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            combo_box.addItems([result[0] for result in results])
    except sqlite3.Error as e:
        print(f"An error occurred while fetching data: {e}")

def create_currency_field(parent):
    """Create a field for currency input."""
    return create_widget_with_line_edit_and_combobox(parent, ['CAD', 'USD'])

def create_dimension_field(parent):
    """Create a field for dimension input."""
    line_edit = QtWidgets.QLineEdit(parent)
    line_edit.setValidator(QtGui.QDoubleValidator(0.0, 10000.0, 2))
    return line_edit

def create_unit_field(parent, units):
    """Create a field with a unit combo box."""
    return create_widget_with_line_edit_and_combobox(parent, units)

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
    return widget