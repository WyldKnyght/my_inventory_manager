from PyQt6 import QtWidgets
from user_interface.framework.base_widget import BaseWidget
from user_interface.dialogs.purchases.purchase_order_dialog import PurchaseOrderDialog

class PurchasesTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Main layout for the Purchases tab
        main_layout = self.create_vertical_layout()
        self.setLayout(main_layout)

        # Create tab widget
        tab_widget = QtWidgets.QTabWidget(self)
        main_layout.addWidget(tab_widget)

        # Product Purchases tab
        product_purchases_tab = QtWidgets.QWidget()
        tab_widget.addTab(product_purchases_tab, "Product Purchases")
        product_purchases_layout = self.create_vertical_layout()
        product_purchases_tab.setLayout(product_purchases_layout)

        # Table to display purchased products
        self.purchases_table = QtWidgets.QTableWidget(self)
        self.purchases_table.setColumnCount(4)
        self.purchases_table.setHorizontalHeaderLabels([
            'Product', 'Quantity', 'Unit Price', 'Total'
        ])
        product_purchases_layout.addWidget(self.purchases_table)

        # Buttons for actions
        button_layout = self.create_horizontal_layout()
        product_purchases_layout.addLayout(button_layout)

        add_order_button = QtWidgets.QPushButton("Add Purchase Order")
        add_order_button.clicked.connect(self.open_add_order_dialog)
        button_layout.addWidget(add_order_button)

        edit_order_button = QtWidgets.QPushButton("Edit Purchase Order")
        edit_order_button.clicked.connect(self.open_edit_order_dialog)
        button_layout.addWidget(edit_order_button)

        delete_order_button = QtWidgets.QPushButton("Delete Purchase Order")
        delete_order_button.clicked.connect(self.delete_purchase_order)
        button_layout.addWidget(delete_order_button)

    def open_add_order_dialog(self):
        dialog = PurchaseOrderDialog(self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            product_name, quantity, unit_price = dialog.get_order_details()
            self.insert_new_row(product_name, quantity, unit_price)

    def open_edit_order_dialog(self):
        current_row = self.purchases_table.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(self, "Edit Error", "Please select a purchase order to edit.")
            return

        product_item = self.purchases_table.item(current_row, 0)
        quantity_item = self.purchases_table.item(current_row, 1)
        unit_price_item = self.purchases_table.item(current_row, 2)

        dialog = PurchaseOrderDialog(
            self, 
            product_item.text(), 
            int(quantity_item.text()), 
            float(unit_price_item.text().replace('$', ''))
        )
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            product_name, quantity, unit_price = dialog.get_order_details()
            self.update_row(current_row, product_name, quantity, unit_price)

    def delete_purchase_order(self):
        current_row = self.purchases_table.currentRow()
        if current_row >= 0:
            self.purchases_table.removeRow(current_row)
        else:
            QtWidgets.QMessageBox.warning(self, "Delete Error", "Please select a purchase order to delete.")

    def insert_new_row(self, product_name, quantity, unit_price):
        total = quantity * unit_price
        row_position = self.purchases_table.rowCount()
        self.purchases_table.insertRow(row_position)
        self.purchases_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(product_name))
        self.purchases_table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(quantity)))
        self.purchases_table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(f"${unit_price:.2f}"))
        self.purchases_table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(f"${total:.2f}"))

    def update_row(self, row, product_name, quantity, unit_price):
        total = quantity * unit_price
        self.purchases_table.setItem(row, 0, QtWidgets.QTableWidgetItem(product_name))
        self.purchases_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(quantity)))
        self.purchases_table.setItem(row, 2, QtWidgets.QTableWidgetItem(f"${unit_price:.2f}"))
        self.purchases_table.setItem(row, 3, QtWidgets.QTableWidgetItem(f"${total:.2f}"))