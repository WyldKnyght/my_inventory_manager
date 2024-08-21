# src/dialogs/record_dialog/base_record_dialog.py

from PyQt6 import QtWidgets

class BaseRecordDialog(QtWidgets.QDialog):
    def __init__(self, title, record_data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.record_data = record_data or {}
        self.fields = {}
        self.setup_ui()

    def setup_ui(self):
        """Set up the dialog UI."""
        layout = QtWidgets.QFormLayout(self)
        self.add_fields(layout)
        self.add_buttons(layout)

    def add_fields(self, layout):
        """Add input fields for each column."""
        raise NotImplementedError("Subclasses should implement this method.")

    def add_buttons(self, layout):
        """Add Save and Cancel buttons."""
        button_layout = QtWidgets.QHBoxLayout()
        save_button = QtWidgets.QPushButton("Save", self)
        save_button.clicked.connect(self.accept)
        cancel_button = QtWidgets.QPushButton("Cancel", self)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow(button_layout)

    def populate_fields(self):
        """Populate fields with existing record data."""
        for key, value in self.record_data.items():
            if key in self.fields:
                widget = self.fields[key]
                if isinstance(widget, QtWidgets.QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QtWidgets.QComboBox):
                    index = widget.findData(value)
                    widget.setCurrentIndex(index)
                elif isinstance(widget, QtWidgets.QCheckBox):
                    widget.setChecked(value.lower() == 'yes')

    def get_data(self):
        """Retrieve data from input fields."""
        data = {}
        for key, widget in self.fields.items():
            if isinstance(widget, QtWidgets.QLineEdit):
                data[key] = widget.text()
            elif isinstance(widget, QtWidgets.QComboBox):
                data[key] = widget.currentData()
            elif isinstance(widget, QtWidgets.QCheckBox):
                data[key] = 'Yes' if widget.isChecked() else 'No'
        return data