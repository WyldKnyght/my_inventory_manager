
from user_interface.framework.base_widget import BaseWidget

class PurchasesTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Main layout for the Purchases tab
        main_layout = self.create_vertical_layout()
        self.setLayout(main_layout)
