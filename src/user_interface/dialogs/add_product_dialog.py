from PyQt6 import QtWidgets
from utils.database import fetch_all, execute_query

class AddProductDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Product")
        self.setup_ui()
        self.setFixedWidth(600)  # Set a fixed width to make the dialog wider

    def setup_ui(self):
        layout = QtWidgets.QFormLayout(self)  # Use QFormLayout for label-widget pairs

        # Type: Goods or Service
        type_layout = QtWidgets.QHBoxLayout()
        self.type_group = QtWidgets.QButtonGroup(self)
        goods_button = QtWidgets.QRadioButton("Goods")
        goods_button.setChecked(True)
        service_button = QtWidgets.QRadioButton("Service")
        self.type_group.addButton(goods_button)
        self.type_group.addButton(service_button)
        type_layout.addWidget(goods_button)
        type_layout.addWidget(service_button)
        layout.addRow("Type:", type_layout)

        # Input fields
        self.name_input = self.create_line_edit("Name:", layout)
        self.description_input = self.create_line_edit("Description:", layout)
        self.sku_input = self.create_line_edit("SKU:", layout)
        self.unit_input = self.create_line_edit("Unit:", layout)

        # Dimensions
        self.dimensions_input, self.dimensions_unit = self.create_line_edit_with_dropdown(
            "Dimensions (L x W x H):", ["cm", "in"], layout
        )

        # Weight
        self.weight_input, self.weight_unit = self.create_line_edit_with_dropdown(
            "Weight:", ["kg", "g", "lb", "oz"], layout
        )

        # Dropdowns
        self.manufacturer_input = self.create_dropdown(
            "Manufacturer:", "SELECT manufacturer_id, manufacturer_name FROM Manufacturer", layout
        )
        self.brand_input = self.create_dropdown(
            "Brand:", "SELECT brand_id, brand_name FROM Brand", layout
        )
        self.upc_input = self.create_line_edit("UPC:", layout)
        self.selling_price_input = self.create_line_edit("Selling Price:", layout)
        self.account_input = self.create_dropdown(
            "Account:", "SELECT account_id, account_name FROM Accounts", layout
        )
        self.cost_price_input = self.create_line_edit("Cost Price:", layout)
        self.preferred_vendor_input = self.create_dropdown(
            "Preferred Vendor:", "SELECT vendor_id, company_name FROM Vendor", layout
        )

        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        save_button = QtWidgets.QPushButton("Save")
        save_button.clicked.connect(self.save_product)
        cancel_button = QtWidgets.QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow(button_layout)

    def create_line_edit(self, label_text, layout):
        """Create a QLineEdit with a label."""
        line_edit = QtWidgets.QLineEdit(self)
        layout.addRow(label_text, line_edit)
        return line_edit

    def create_line_edit_with_dropdown(self, label_text, dropdown_options, layout):
        """Create a QLineEdit with a label and a QComboBox for units."""
        line_edit = QtWidgets.QLineEdit(self)
        combo_box = QtWidgets.QComboBox(self)
        combo_box.addItems(dropdown_options)
        sub_layout = QtWidgets.QHBoxLayout()
        sub_layout.addWidget(line_edit)
        sub_layout.addWidget(combo_box)
        layout.addRow(label_text, sub_layout)
        return line_edit, combo_box

    def create_dropdown(self, label_text, query, layout):
        """Create a QComboBox with a label and populate it with data from a database query."""
        combo_box = QtWidgets.QComboBox(self)
        self.populate_dropdown(combo_box, query)
        layout.addRow(label_text, combo_box)
        return combo_box

    def populate_dropdown(self, combo_box, query):
        """Populate a QComboBox with data from a database query."""
        results = fetch_all(query)
        for result in results:
            combo_box.addItem(result[1], result[0])  # Display name, store ID

    def save_product(self):
        """Save the new product to the database."""
        product_type = "Goods" if self.type_group.checkedButton().text() == "Goods" else "Service"
        name = self.name_input.text()
        description = self.description_input.text()
        sku = self.sku_input.text()
        unit = self.unit_input.text()
        dimensions = f"{self.dimensions_input.text()} {self.dimensions_unit.currentText()}"
        weight = f"{self.weight_input.text()} {self.weight_unit.currentText()}"
        manufacturer_id = self.manufacturer_input.currentData()
        brand_id = self.brand_input.currentData()
        upc = self.upc_input.text()
        selling_price = self.selling_price_input.text()
        account_id = self.account_input.currentData()
        cost_price = self.cost_price_input.text()
        preferred_vendor_id = self.preferred_vendor_input.currentData()

        # Insert the new product into the database
        query = """
        INSERT INTO Products (type, product_name, product_description, product_number, unit_type, 
                            dimensions, weight, manufacturer_id, brand_id, upc, selling_price, 
                            account_id, cost_price, preferred_vendor_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (product_type, name, description, sku, unit, dimensions, weight, manufacturer_id, 
                    brand_id, upc, selling_price, account_id, cost_price, preferred_vendor_id)

        try:
            execute_query(query, params)
            self.accept()  # Close the dialog on success
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to save product: {e}")