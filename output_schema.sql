CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_number TEXT UNIQUE NOT NULL,
    product_name TEXT,
    product_description TEXT,
    unit_type TEXT CHECK(unit_type IN ('box', 'cm', 'in', 'kg', 'lb', 'pcs')),
    category_id INTEGER,
    sku TEXT,
    company_id INTEGER,
    brand_id INTEGER,
    product_size TEXT,
    product_color TEXT,
    dimensions TEXT,
    product_weight REAL,
    upc TEXT UNIQUE,
    cost_price REAL,
    selling_price REAL,
    quantity INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    FOREIGN KEY (brand_id) REFERENCES Brand(brand_id)
);

CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT
);

CREATE TABLE Sales (
    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    sale_date DATE,
    sub_total REAL,
    discount REAL,
    shipping_charges REAL,
    adjustment REAL,
    sales_total REAL,
    customer_notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Product_Sales (
    product_sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sales_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Purchases (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id INTEGER,
    purchase_date DATE,
    purchase_order_number TEXT UNIQUE,
    purchase_amount REAL,
    payment_method TEXT,
    product_id INTEGER,
    shipping_cost REAL,
    shipping_date DATE,
    customs_fees REAL,
    reference TEXT,
    estimated_delivery_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (vendor_id) REFERENCES Vendor(vendor_id)
);

CREATE TABLE Product_Purchases (
    product_purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (purchase_id) REFERENCES Purchases(purchase_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Expense (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_date DATE,
    account_id TEXT,
    amount REAL,
    vendor_id INTEGER,
    notes TEXT,
    FOREIGN KEY (vendor_id) REFERENCES Vendor(vendor_id),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_first_name TEXT,
    customer_last_name TEXT,
    customer_email TEXT,
    customer_phone TEXT,
    customer_address TEXT
);

CREATE TABLE Brand (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_name TEXT
);

CREATE TABLE Company (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT
);

CREATE TABLE Vendor (
    vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    primary_contact TEXT,
    email TEXT,
    phone TEXT,
    website TEXT
);

CREATE TABLE Accounts (
    account_id TEXT PRIMARY KEY,
    account_name TEXT,
    account_type TEXT,
    account_description TEXT
);