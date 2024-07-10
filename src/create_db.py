# src/database/create_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.create_app import db  
from models.tab_inventory import InventoryTab
from models.tab_purchase import PurchaseTab
from models.tab_report import ReportTab
from models.tab_sale import SaleTab
from models.admin_brand import Brand
from models.admin_category import Category
from models.admin_customer import Customer
from models.admin_inventory import InventoryItem
from models.admin_inventory_status import InventoryStatus
from models.admin_supplier import Supplier

# Define your database URL
DB_URL = 'sqlite:///database/small_business.db'

# Create an engine and bind it to the metadata of your base
engine = create_engine(DB_URL)
db.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

def add_default_data(session):
    # Add default data here
    pass

try:
    db.metadata.create_all(engine)
    add_default_data(session)
    session.commit()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()

print("Database created successfully.")