# src/user_interface/common/base_widget.py
from PyQt6 import QtWidgets
from utils.custom_logging import logger

from .base_widget_components import (
    LayoutWidgetsMixin,
    InputWidgetsMixin,
    ContainerWidgetsMixin,
    UtilityMethodsMixin
)

class BaseWidget(QtWidgets.QWidget, LayoutWidgetsMixin, InputWidgetsMixin, ContainerWidgetsMixin, UtilityMethodsMixin):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.info(f"Initialized {self.__class__.__name__}")
