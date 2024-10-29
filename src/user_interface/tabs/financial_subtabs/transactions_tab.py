# src/user_interface/tabs/financial_subtabs/transactions_tab.py

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QPushButton, QTableWidgetItem, QComboBox, QLineEdit, 
                             QDateEdit, QDialog, QDialogButtonBox, QFormLayout, QDoubleSpinBox)
from PyQt6.QtCore import Qt, QDate
from datetime import date, timedelta

class TransactionsTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create filter controls
        filter_layout = QHBoxLayout()
        self.account_combo = QComboBox()
        self.account_combo.addItem("All Accounts")
        # TODO: Populate with actual accounts from the database
        filter_layout.addWidget(self.account_combo)

        self.date_from = self._extracted_from_init_ui_11(
            "From Date (YYYY-MM-DD)", filter_layout
        )
        self.date_to = self._extracted_from_init_ui_11(
            "To Date (YYYY-MM-DD)", filter_layout
        )
        filter_button = QPushButton("Apply Filter")
        filter_button.clicked.connect(self.apply_filter)
        filter_layout.addWidget(filter_button)

        layout.addLayout(filter_layout)

        # Create table
        self.transactions_table = QTableWidget()
        self.transactions_table.setColumnCount(7)
        self.transactions_table.setHorizontalHeaderLabels(["Date", "Account", "Category", "Description", "Income", "Expense", "Balance"])
        layout.addWidget(self.transactions_table)

        # Buttons
        button_layout = QHBoxLayout()
        add_transaction_button = QPushButton("Add Transaction")
        add_transaction_button.clicked.connect(self.add_transaction)
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.load_transactions)
        button_layout.addWidget(add_transaction_button)
        button_layout.addWidget(refresh_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Set default date range (e.g., last 30 days)
        today = date.today()
        self.date_from.setText((today - timedelta(days=30)).strftime('%Y-%m-%d'))
        self.date_to.setText(today.strftime('%Y-%m-%d'))

        # Load initial data
        self.load_transactions()

    # TODO Rename this here and in `init_ui`
    def _extracted_from_init_ui_11(self, arg0, filter_layout):
        result = QLineEdit()
        result.setPlaceholderText(arg0)
        filter_layout.addWidget(result)

        return result

    def load_transactions(self):
        # Clear existing items
        self.transactions_table.setRowCount(0)
        
        # Get date range
        start_date = self.date_from.text()
        end_date = self.date_to.text()
        
        # Fetch transaction data from database
        transactions = self.db_manager.transaction_manager.get_transactions(start_date, end_date)
        
        # Populate table
        for row, transaction in enumerate(transactions):
            self.transactions_table.insertRow(row)
            for col, value in enumerate(transaction):
                table_item = QTableWidgetItem(str(value))
                table_item.setFlags(table_item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make item read-only
                self.transactions_table.setItem(row, col, table_item)

    def apply_filter(self):
        account = self.account_combo.currentText()
        date_from = self.date_from.text()
        date_to = self.date_to.text()
        
        # Update the transactions table with the new filter
        self.load_transactions()


    def add_transaction(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Transaction")
        layout = QFormLayout(dialog)

        date_edit = QDateEdit(QDate.currentDate())
        account_combo = QComboBox()
        # TODO: Populate account_combo with actual accounts
        account_combo.addItem("Account 1")
        account_combo.addItem("Account 2")
        category_combo = QComboBox()
        # TODO: Populate category_combo with actual categories
        category_combo.addItem("Category 1")
        category_combo.addItem("Category 2")
        description_edit = QLineEdit()
        amount_edit = QDoubleSpinBox()
        amount_edit.setRange(-1000000, 1000000)
        amount_edit.setDecimals(2)

        layout.addRow("Date:", date_edit)
        layout.addRow("Account:", account_combo)
        layout.addRow("Category:", category_combo)
        layout.addRow("Description:", description_edit)
        layout.addRow("Amount:", amount_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addRow(button_box)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            # Process the new transaction
            new_transaction = {
                'date': date_edit.date().toString(Qt.DateFormat.ISODate),
                'account': account_combo.currentText(),
                'category': category_combo.currentText(),
                'description': description_edit.text(),
                'amount': amount_edit.value()
            }
            # TODO: Add the new transaction to the database
            print(f"New transaction: {new_transaction}")
            self.load_transactions()  # Refresh the transaction list