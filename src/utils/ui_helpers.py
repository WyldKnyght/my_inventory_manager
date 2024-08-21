from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

def create_action_button(parent, text, action):
    """Create a button and connect it to an action."""
    button = QPushButton(text, parent)
    button.clicked.connect(action)
    return button

def add_action_buttons(parent, actions):
    """Add action buttons to a layout."""
    layout = QHBoxLayout()
    for text, action in actions:
        button = create_action_button(parent, text, action)
        layout.addWidget(button)
    return layout

def configure_table_headers(table: QTableWidget, column_headers):
    """Configure the table headers."""
    table.setColumnCount(len(column_headers))
    table.setHorizontalHeaderLabels(column_headers)

def populate_table_with_data(table: QTableWidget, data, column_headers):
    """Populate the table with data."""
    table.setRowCount(len(data))
    table.setUpdatesEnabled(False)
    for row, item in enumerate(data):
        populate_table_row(table, row, item, column_headers)
    table.setUpdatesEnabled(True)

def populate_table_row(table: QTableWidget, row, item, column_headers):
    """Populate a single row in the table."""
    for col, header in enumerate(column_headers):
        value = item.get(header, "")
        table.setItem(row, col, QTableWidgetItem(str(value)))