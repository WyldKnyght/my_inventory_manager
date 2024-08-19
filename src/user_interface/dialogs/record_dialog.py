from PyQt6 import QtWidgets
from utils.ui_helpers import create_button
from utils.database import get_table_columns, fetch_all

class RecordDialog(QtWidgets.QDialog):
    def __init__(self, table_name, product_data=None, parent=None):
        super().__init__(parent)
        self.table_name = table_name
        self.product_data = product_data
        self.setWindowTitle(f"{'Edit' if product_data else 'Add'} {table_name}")
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QFormLayout(self)  # Unique layout for this dialog

        self.fields = {}
        column_info = get_table_columns(self.table_name)
        field_definitions = [name for name, is_auto_increment in column_info if not is_auto_increment]

        self.add_fields(*field_definitions)
        for label, widget in self.fields.items():
            layout.addRow(label.replace('_', ' ').title() + ":", widget)

        if self.product_data:
            self.populate_fields()

        button_layout = QtWidgets.QHBoxLayout()  # Ensure this layout is not reused
        save_button = create_button(self, "Save", self.accept)
        cancel_button = create_button(self, "Cancel", self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow(button_layout)

    def add_fields(self, *args):
        field_creators = {
            'discontinued': lambda: QtWidgets.QCheckBox(self),
            'company_id': lambda: self.create_combobox('company_id'),
            'brand_id': lambda: self.create_combobox('brand_id'),
            'category_id': lambda: self.create_combobox('category_id'),
            'product_weight_unit': lambda: self.create_unit_combobox('product_weight_unit'),
            'unit_type': lambda: self.create_unit_combobox('unit_type'),
            'cost_price': lambda: self.create_currency_field('cost_price'),
            'selling_price': lambda: self.create_currency_field('selling_price')
        }
        for arg in args:
            self.fields[arg] = field_creators.get(arg, lambda: QtWidgets.QLineEdit(self))()

    def populate_fields(self):
        fields = self.fields
        for key, value in self.product_data.items():
            if key in fields:
                self.update_field(key, value)

    def create_combobox(self, field_name):
        combo_box = QtWidgets.QComboBox(self)
        table_name = field_name.replace('_id', '').capitalize()
        query = f"SELECT {field_name}, {table_name}_name FROM {table_name}"
        results = fetch_all(query)
        combo_box.addItems([result[1] for result in results])
        return combo_box

    def create_unit_combobox(self, field_name):
        combo_box = QtWidgets.QComboBox(self)
        units = ['g', 'kg', 'oz', 'lb'] if field_name == 'product_weight_unit' else ['box', 'cm', 'in', 'kg', 'lb', 'pcs']
        combo_box.addItems(units)
        return combo_box

    def create_currency_field(self, arg):
        line_edit = QtWidgets.QLineEdit(self)
        currency_combo = self.create_currency_combobox(['CAD', 'USD'])
        self.fields[f'{arg}_currency'] = currency_combo
        return line_edit

    def create_currency_combobox(self, currencies):
        combo_box = QtWidgets.QComboBox(self)
        combo_box.addItems(currencies)
        return combo_box

    def update_field(self, key, value):
        widget = self.fields[key]
        if isinstance(widget, QtWidgets.QLineEdit):
            widget.setText(value)
        elif isinstance(widget, QtWidgets.QCheckBox):
            widget.setChecked(bool(value))
        elif isinstance(widget, QtWidgets.QComboBox):
            index = widget.findText(value)
            widget.setCurrentIndex(index)

    def get_data(self):
        data = {}
        fields = self.fields
        for key, widget in fields.items():
            if isinstance(widget, QtWidgets.QLineEdit):
                data[key] = widget.text()
            elif isinstance(widget, QtWidgets.QCheckBox):
                data[key] = widget.isChecked()
            elif isinstance(widget, QtWidgets.QComboBox):
                data[key] = widget.currentText()
        return data
