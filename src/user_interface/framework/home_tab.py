from user_interface.framework.base_widget import BaseWidget
from PyQt6 import QtWidgets

class HomeTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Set up the main UI components."""
        layout = self.create_vertical_layout(self)
        time_frame_group = self.create_time_frame_group()
        layout.addWidget(time_frame_group)

    def create_time_frame_group(self) -> QtWidgets.QGroupBox:
        """Create and configure the Time Frame group box."""
        time_frame_group = self.create_group_box("Time Frame", self)
        time_frame_layout = self.create_grid_layout()
        time_frame_group.setLayout(time_frame_layout)

        label = self.create_time_frame_label()
        time_frame_layout.addWidget(label, 0, 0)

        self.time_frame_combo_box = self.create_time_frame_combo_box()
        time_frame_layout.addWidget(self.time_frame_combo_box, 0, 1)

        return time_frame_group

    def create_time_frame_label(self) -> QtWidgets.QLabel:
        """Create the label for the Time Frame selection."""
        return self.create_label(10, "Select Time Frame:", parent=self)

    def create_time_frame_combo_box(self) -> QtWidgets.QComboBox:
        """Create and configure the Time Frame combo box."""
        combo_box = QtWidgets.QComboBox(self)
        time_frame_options = [
            "Today", "Yesterday", "This Week", "This Month",
            "This Year", "Previous Week", "Previous Month", 
            "Previous Year", "Custom"
        ]
        combo_box.addItems(time_frame_options)
        return combo_box