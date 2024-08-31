# src/user_interface/common/base_widget_components/input_widgets.py
from PyQt6 import QtWidgets, QtCore
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.ui_config import UIConfig

class InputWidgetsMixin:
    @ErrorManager.handle_errors()
    def create_label(self, text: str, font_size: int = UIConfig.DEFAULT_FONT_SIZE, 
                        alignment: QtCore.Qt.AlignmentFlag = UIConfig.DEFAULT_ALIGNMENT, parent=None) -> QtWidgets.QLabel:
        """Create a label with specified font size, text, and alignment."""
        self._validate_font_size(font_size)
        label = self._create_widget(QtWidgets.QLabel, parent, text=text)
        self._set_font(label, font_size)
        label.setAlignment(alignment)
        logger.debug(f"Created label: {text}")
        return label

    @ErrorManager.handle_errors()
    def create_button(self, text: str, callback=None, parent=None) -> QtWidgets.QPushButton:
        """Create a button with specified text and an optional callback."""
        button = self._create_widget(QtWidgets.QPushButton, parent, text=text)
        self._connect_callback(button.clicked, callback)
        logger.debug(f"Created button: {text}")
        return button

    @ErrorManager.handle_errors()
    def create_line_edit(self, placeholder_text: str = "", parent=None) -> QtWidgets.QLineEdit:
        """Create a line edit with an optional placeholder text."""
        line_edit = self._create_widget(QtWidgets.QLineEdit, parent)
        line_edit.setPlaceholderText(placeholder_text)
        logger.debug(f"Created line edit with placeholder: {placeholder_text}")
        return line_edit

    @ErrorManager.handle_errors()
    def create_combo_box(self, items: list, parent=None) -> QtWidgets.QComboBox:
        combo_box = self._create_widget(QtWidgets.QComboBox, parent)
        combo_box.addItems(items)
        logger.debug(f"Created combo box with {len(items)} items")
        return combo_box

    @ErrorManager.handle_errors()
    def create_checkbox(self, text: str, checked: bool = False, parent=None) -> QtWidgets.QCheckBox:
        checkbox = self._create_widget(QtWidgets.QCheckBox, parent, text=text)
        checkbox.setChecked(checked)
        logger.debug(f"Created checkbox: {text}")
        return checkbox

    @ErrorManager.handle_errors()
    def create_date_edit(self, parent=None) -> QtWidgets.QDateEdit:
        date_edit = self._create_widget(QtWidgets.QDateEdit, parent)
        date_edit.setCalendarPopup(True)
        logger.debug("Created date edit widget")
        return date_edit