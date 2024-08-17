from PyQt6 import QtWidgets

class RecordDialog(QtWidgets.QDialog):
    def __init__(self, table_name, product_data=None, parent=None):
        super().__init__(parent)
        self.table_name = table_name
        self.product_data = product_data
        self.setWindowTitle(f"{'Edit' if product_data else 'Add'} {table_name}")
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QFormLayout(self)
        
        # Initialize fields based on the table
        self.fields = {}
        if self.table_name == "Vendor":
            self.add_line_edit_fields('company_name', 'primary_contact', 'email', 'phone', 'website')
        elif self.table_name == "Manufacturer":
            self.add_line_edit_fields('manufacturer_name')
        elif self.table_name == "Brand":
            self.add_line_edit_fields('brand_name')
        elif self.table_name == "Customer":
            self.add_line_edit_fields('customer_first_name', 'customer_last_name', 'customer_email', 'customer_phone', 'customer_address')
        elif self.table_name == "Categories":
            self.add_line_edit_fields('product_category_name')
        elif self.table_name == "Accounts":
            # Do not include 'account_id' as it is auto-incremented
            self.add_line_edit_fields('account_name', 'account_type', 'account_description')

        for label, widget in self.fields.items():
            layout.addRow(label.replace('_', ' ').title() + ":", widget)

        # Populate fields if editing
        if self.product_data:
            for key, value in self.product_data.items():
                if key in self.fields:
                    self.fields[key].setText(value)

        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        save_button = QtWidgets.QPushButton("Save")
        save_button.clicked.connect(self.accept)
        cancel_button = QtWidgets.QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow(button_layout)

    def add_line_edit_fields(self, *args):
        """Add multiple QLineEdit fields to the fields dictionary."""
        for arg in args:
            self.fields[arg] = QtWidgets.QLineEdit(self)

    def get_data(self):
        """Retrieve data from input fields."""
        return {key: widget.text() for key, widget in self.fields.items()}