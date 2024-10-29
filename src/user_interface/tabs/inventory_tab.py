# src/user_interface/tabs/inventory_tab.py

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QPushButton, QTableWidgetItem, QLineEdit, QDialog, 
                             QFormLayout, QDialogButtonBox, QSpinBox, QComboBox,
                             QDoubleSpinBox, QCheckBox)
from PyQt6.QtCore import Qt

class InventoryTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.schema_manager = db_manager.schema_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search inventory...")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_inventory)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)
        
        # Create table
        self.inventory_table = QTableWidget()
        columns = self.schema_manager.get_column_names('inventory', 'catalog')
        self.inventory_table.setColumnCount(len(columns))
        self.inventory_table.setHorizontalHeaderLabels(columns)
        layout.addWidget(self.inventory_table)

        # Buttons
        button_layout = QHBoxLayout()
        add_item_button = QPushButton("Add Item")
        add_item_button.clicked.connect(self.add_item)
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.load_inventory)
        button_layout.addWidget(add_item_button)
        button_layout.addWidget(refresh_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Load initial data
        self.load_inventory()

    def load_inventory(self):
        self.inventory_table.setRowCount(0)
        inventory_data = self.db_manager.inventory_manager.get_inventory()
        self._populate_table(inventory_data)

    def _populate_table(self, data):
        self.inventory_table.setRowCount(0)
        for row, item in enumerate(data):
            self.inventory_table.insertRow(row)
            for col, value in enumerate(item):
                if col < self.inventory_table.columnCount():  # Ensure we don't exceed the number of columns
                    table_item = QTableWidgetItem(str(value))
                    table_item.setFlags(table_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.inventory_table.setItem(row, col, table_item)

    def add_item(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Inventory Item")
        layout = QFormLayout(dialog)

        columns = self.schema_manager.get_column_names('inventory', 'catalog')
        input_widgets = {}

        for column in columns:
            if column == 'item_id':
                continue  # Skip item_id as it's auto-generated

            column_type = self.schema_manager.get_column_type('inventory', 'catalog', column)

            if column_type.upper() in ['INTEGER', 'REAL']:
                widget = QSpinBox() if column_type.upper() == 'INTEGER' else QDoubleSpinBox()
                widget.setRange(-1000000, 1000000)
            elif column_type.upper() == 'TEXT':
                widget = QLineEdit()
            elif column_type.upper() == 'BOOLEAN':
                widget = QCheckBox()
            else:
                widget = QLineEdit()  # Default to QLineEdit for unknown types

            input_widgets[column] = widget
            layout.addRow(column.replace('_', ' ').title() + ':', widget)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addRow(button_box)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_item = {}
            for column, widget in input_widgets.items():
                if isinstance(widget, QComboBox):
                    new_item[column] = widget.currentIndex() + 1  # Assuming IDs start from 1
                elif isinstance(widget, QCheckBox):
                    new_item[column] = widget.isChecked()
                else:
                    new_item[column] = widget.text() if isinstance(widget, QLineEdit) else widget.value()

            self.db_manager.inventory_manager.add_item(new_item)
            self.load_inventory()

    def search_inventory(self):
        if search_term := self.search_input.text():
            inventory_data = self.db_manager.inventory_manager.search_inventory(search_term)
        else:
            inventory_data = self.db_manager.inventory_manager.get_inventory()

        self.inventory_table.setRowCount(0)
        self._populate_table(inventory_data)