import os
import sqlite3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the database path from the environment variables
db_path = os.getenv('DB_PATH')

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_path)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create the Product table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT NOT NULL,
    ProductCode TEXT,
    Description TEXT,
    CategoryID TEXT,
    BrandID TEXT,
    Size TEXT,
    Color TEXT,
    Condition TEXT,
    CostPrice REAL,
    Markup INTEGER,
    RetailPrice REAL,
    ProductStatus TEXT,
    Notes TEXT,
    SupplierID TEXT,
    SinglesInStock INTEGER,
    CasesInStock INTEGER,
    QtyPerCase INTEGER,
    TotalInStock AS (SinglesInStock + CasesInStock * QtyPerCase),
    TotalNumberOfSales INTEGER,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (BrandID) REFERENCES Brand(BrandID),
    FOREIGN KEY (ProductStatus) REFERENCES InventoryStatus(InventoryStatusID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
)
""")

# Create the Category table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Category (
    CategoryID TEXT PRIMARY KEY,
    CategoryName TEXT NOT NULL,
    CategoryPrefix TEXT NOT NULL,
    ParentCategoryID TEXT,
    SubCategoriesName TEXT,
    FOREIGN KEY (ParentCategoryID) REFERENCES Category(CategoryID)
)
""")

# Create the Brand table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Brand (
    BrandID TEXT PRIMARY KEY,
    BrandName TEXT NOT NULL
)
""")

# Create the Supplier table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Supplier (
    SupplierID TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    ContactPerson TEXT,
    Address TEXT,
    Phone TEXT,
    Email TEXT,
    Website TEXT
)
""")

# Create the Purchase table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Purchase (
    PurchaseID TEXT PRIMARY KEY,
    PurchaseOrderNumber TEXT,
    OrderNumber TEXT,
    ProductID TEXT,
    PurchaseDate DATE,
    ShippingDate DATE,
    ShippingTrackingNumber TEXT,
    SupplierID TEXT,
    SinglesQuantity INTEGER,
    CasesQuantity INTEGER,
    ProductStatus TEXT,
    PaymentMethod TEXT,
    Currency TEXT,
    ExchangeRate INTEGER,
    CostPrice REAL,
    Discount INTEGER,
    Shipping REAL,
    Taxes REAL,
    TotalCost AS (CostPrice * (1 - Discount / 100) + Shipping + Taxes),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID),
    FOREIGN KEY (ProductStatus) REFERENCES InventoryStatus(InventoryStatusID)
)
""")

# Create the Sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    SaleID TEXT PRIMARY KEY,
    SalesOrderNumber TEXT,
    ProductID TEXT,
    OrderDate DATE,
    ShipDeliveryPickupDate DATE,
    CustomerID TEXT,
    Quantity INTEGER,
    RetailPrice REAL,
    Shipping REAL,
    Taxes REAL,
    TotalCost AS (Quantity * RetailPrice + Shipping + Taxes),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
)
""")

# Create the Customer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    ContactInformation TEXT
)
""")

# Create the Report table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Report (
    ReportID TEXT PRIMARY KEY,
    Date DATE,
    SalesTotal REAL,
    ProfitTotal REAL,
    BalanceSheet TEXT,
    StockWaitingToBeReceived TEXT
)
""")

# Create the Inventory Status table
cursor.execute("""
CREATE TABLE IF NOT EXISTS InventoryStatus (
    InventoryStatusID TEXT PRIMARY KEY,
    StatusName TEXT NOT NULL,
    StatusPrefix TEXT NOT NULL
)
""")

# Commit the changes and close the connection
conn.commit()
conn.close()