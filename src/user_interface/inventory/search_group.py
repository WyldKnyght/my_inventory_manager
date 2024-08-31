# src/user_interface/inventory/search_group.py
from configs.config_manager import config_manager
from utils.error_manager import ErrorManager
from utils.custom_logging import logger
from user_interface.common.base_widget import BaseWidget

class SearchGroup(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    @ErrorManager.handle_errors()
    def setup_ui(self):
        layout = self.create_horizontal_layout()
        self.search_bar = self.create_line_edit(config_manager.get('ui.placeholders.search', "Search..."))
        self.search_bar.textChanged.connect(self.filter_inventory)
        layout.addWidget(self.search_bar)
        self.setLayout(layout)

    @ErrorManager.handle_errors()
    def filter_inventory(self):
        search_text = self.search_bar.text().lower()
        logger.debug(f"Filtering inventory with search text: {search_text}")
        table = self.parent().catalog_table.table
        for row in range(table.rowCount()):
            row_hidden = True
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item and search_text in item.text().lower():
                    row_hidden = False
                    break
            table.setRowHidden(row, row_hidden)
        logger.info("Inventory filtered")