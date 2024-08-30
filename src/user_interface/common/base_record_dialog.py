# src/user_interface/common/base_record_dialog.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger
from utils.error_handler import ErrorHandler
from configs.ui_config import DIALOG_BUTTON_LABELS

class BaseRecordDialog(QtWidgets.QDialog):
    def __init__(self, title, record_data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.record_data = record_data or {}
        self.fields = {}
        self.setup_ui()
        logger.info(f"Initialized BaseRecordDialog: {title}")

    @ErrorHandler.handle_errors()
    def setup_ui(self):
        """Set up the dialog UI."""
        layout = QtWidgets.QFormLayout(self)
        self.add_fields(layout)
        self.add_buttons(layout)
        logger.debug("BaseRecordDialog UI setup completed")

    def add_fields(self, layout):
        """Add input fields for each column."""
        raise NotImplementedError("Subclasses should implement this method.")

    @ErrorHandler.handle_errors()
    def add_buttons(self, layout):
        """Add Save and Cancel buttons."""
        button_layout = QtWidgets.QHBoxLayout()
        save_button = QtWidgets.QPushButton(DIALOG_BUTTON_LABELS['save'], self)
        save_button.clicked.connect(self.accept)
        cancel_button = QtWidgets.QPushButton(DIALOG_BUTTON_LABELS['cancel'], self)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow(button_layout)
        logger.debug(f"Added {DIALOG_BUTTON_LABELS['save']} and {DIALOG_BUTTON_LABELS['cancel']} buttons to BaseRecordDialog")

    @ErrorHandler.handle_errors()
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
        logger.debug(f"Populated fields with record data: {list(self.record_data.keys())}")

    @ErrorHandler.handle_errors()
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
        logger.debug(f"Retrieved data from input fields: {list(data.keys())}")
        return data