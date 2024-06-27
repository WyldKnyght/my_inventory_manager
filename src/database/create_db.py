# src/database/create_db.py

import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Append the path to the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.create_app import db  
from models.brand import Brand
from models.category import Category
from models.inventory_item import InventoryItem
from models.inventory_status import InventoryStatus
from models.supplier import Supplier

# Define your database URL
DB_URL = 'sqlite:///database/small_business.db'

# Create an engine and bind it to the metadata of your base
engine = create_engine(DB_URL)
db.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# You can optionally add initialization logic here, like adding default data

# Commit the session and close it
session.commit()
session.close()

print("Database created successfully.")
