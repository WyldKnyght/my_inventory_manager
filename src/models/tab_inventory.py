# src/models/tab_inventory.py
# Display the contents of the inventory table (View-Only)
from utils.create_app import db
from .admin_inventory import InventoryItem

class InventoryTab(InventoryItem):
    __table__ = InventoryItem.__table__
    __mapper_args__ = {
        'polymorphic_identity': 'inventory_tab',
        'concrete': True
    }

    # You can add any additional methods or properties specific to the view-only version here