# src/configs/style_manager.py
from PyQt6.QtWidgets import QApplication
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.path_manager import path_manager

class StyleManager:
    _style_content = ""

    @classmethod
    @ErrorManager.handle_errors()
    def load_style(cls):
        style_path = path_manager.get_style_path()
        with open(style_path, 'r') as f:
            cls._style_content = f.read()
        logger.info("Style loaded from QSS file")

    @classmethod
    @ErrorManager.handle_errors()
    def apply_style(cls, **kwargs):
        if not cls._style_content:
            cls.load_style()

        style = cls._style_content
        for key, value in kwargs.items():
            placeholder = f"{{{{{key}}}}}"
            style = style.replace(placeholder, str(value))

        QApplication.instance().setStyleSheet(style)
        logger.info("Style applied to application")

    @classmethod
    def get_raw_style(cls):
        if not cls._style_content:
            cls.load_style()
        return cls._style_content