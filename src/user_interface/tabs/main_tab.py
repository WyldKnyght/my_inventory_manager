from user_interface.base_widget import BaseWidget
from PyQt6 import QtWidgets

class MainTab(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Main vertical layout for the tab
        main_layout = QtWidgets.QVBoxLayout(self)

        # Top Section: Time Frame
        time_frame_group = self.create_group_box("Time Frame")
        time_frame_layout = self.create_grid_layout()
        time_frame_group.setLayout(time_frame_layout)

        self.time_frame_combo_box = QtWidgets.QComboBox(self)
        time_frame_options = [
            "Today", "Yesterday", "This Week", "This Month",
            "This Year", "Previous Week", "Previous Month", 
            "Previous Year", "Custom"
        ]
        self.time_frame_combo_box.addItems(time_frame_options)
        time_frame_layout.addWidget(self.time_frame_combo_box, 0, 0)

        main_layout.addWidget(time_frame_group)

        # Bottom Section: Sales Activity and Top Selling Products
        bottom_layout = QtWidgets.QHBoxLayout()

        # Sales Activity Group
        sales_activity_group = self.create_group_box("Sales Activity")
        sales_activity_layout = self.create_grid_layout()
        sales_activity_group.setLayout(sales_activity_layout)

        # Add labels to the sales activity grid
        sales_labels = [
            ("To be Packed", "1"),
            ("To be Shipped", "2"),
            ("To be Delivered", "3"),
            ("To be Picked Up", "4")
        ]
        self.add_labels_to_grid(sales_activity_layout, sales_labels)

        bottom_layout.addWidget(sales_activity_group, 1)

        # Top Selling Products Group
        top_selling_products_group = self.create_group_box("Top Selling Products")
        top_selling_products_layout = self.create_vertical_layout()
        top_selling_products_group.setLayout(top_selling_products_layout)

        # Add labels to the top selling Products layout
        top_selling_products = [f"#{i} Item" for i in range(1, 6)]
        self.add_labels_to_layout(top_selling_products_layout, top_selling_products)

        bottom_layout.addWidget(top_selling_products_group, 2)

        main_layout.addLayout(bottom_layout)

        # Section 3: Product Details, Inventory Summary, Purchase Orders
        bottom_section_layout = QtWidgets.QHBoxLayout()

        # Product Details Group
        product_details_group = self.create_group_box("Product Details")
        product_details_layout = self.create_grid_layout()
        product_details_group.setLayout(product_details_layout)

        # Add labels to the product details grid
        product_details_labels = [
            ("Products Low Stock", "0"),
            ("All Product Groups", "0"),
            ("All Products", "0")
        ]
        self.add_labels_to_grid(product_details_layout, product_details_labels)

        bottom_section_layout.addWidget(product_details_group)

        # Inventory Summary Group
        inventory_summary_group = self.create_group_box("Inventory Summary")
        inventory_summary_layout = self.create_grid_layout()
        inventory_summary_group.setLayout(inventory_summary_layout)

        # Add labels to the inventory summary grid
        inventory_summary_labels = [
            ("In Stock", "0"),
            ("Back Ordered", "0"),
            ("Pending Delivery", "0")
        ]
        self.add_labels_to_grid(inventory_summary_layout, inventory_summary_labels)

        bottom_section_layout.addWidget(inventory_summary_group)

        # Purchase Orders Group
        purchase_orders_group = self.create_group_box("Purchase Orders")
        purchase_orders_layout = self.create_grid_layout()
        purchase_orders_group.setLayout(purchase_orders_layout)

        # Add labels to the purchase orders grid
        purchase_orders_labels = [
            ("Qty. Ordered", "0"),
            ("Qty. Shipped", "0"),
            ("Qty. Pre-Ordered", "0"),
            ("Total Cost", "$1000.00")
        ]
        self.add_labels_to_grid(purchase_orders_layout, purchase_orders_labels)

        bottom_section_layout.addWidget(purchase_orders_group)

        main_layout.addLayout(bottom_section_layout)

    def add_labels_to_grid(self, layout, labels, font_size=8):
        if layout is None:
            raise ValueError("Layout is not initialized.")
        for row, (text, value) in enumerate(labels):
            self.add_label_to_grid(layout, text, row, 0, font_size)
            self.add_label_to_grid(layout, value, row, 1, font_size)

    def add_labels_to_layout(self, layout, labels, font_size=8):
        if layout is None:
            raise ValueError("Layout is not initialized.")
        for text in labels:
            self.add_label_to_layout(layout, text, font_size)

    def add_label_to_grid(self, layout, text, row, col, font_size=8):
        label = self.create_label(font_size, text)
        layout.addWidget(label, row, col)

    def add_label_to_layout(self, layout, text, font_size=8):
        label = self.create_label(font_size, text)
        layout.addWidget(label)