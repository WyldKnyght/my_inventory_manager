CREATE TABLE Category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT
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

CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_first_name TEXT,
    customer_last_name TEXT,
    customer_email TEXT,
    customer_phone TEXT,
    customer_address TEXT
);

CREATE TABLE Accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT,
    account_type TEXT,
    account_description TEXT
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_number TEXT UNIQUE NOT NULL,
    product_name TEXT,
    product_description TEXT,
    upc TEXT UNIQUE,
    company_name TEXT,
    brand_name TEXT,
    category_name TEXT,
    theme TEXT,
    product_character TEXT,
    product_height REAL,
    product_width REAL,
    product_length REAL,
    product_size REAL,
    product_weight_unit TEXT CHECK(product_weight_unit IN ('g', 'kg', 'oz','lb')),
    product_color TEXT,
    cost_price REAL,
    selling_price REAL,
    quantity INTEGER,
    unit_type TEXT CHECK(unit_type IN ('box', 'cm', 'in', 'kg', 'lb', 'pcs')),
    discontinued BOOLEAN,
    FOREIGN KEY (category_name) REFERENCES Category(category_name),
    FOREIGN KEY (company_name) REFERENCES Company(company_name),
    FOREIGN KEY (brand_name) REFERENCES Brand(brand_name)
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
    vendor_order_number TEXT,
    purchase_order_number TEXT UNIQUE,
    purchase_date DATE,
    purchase_amount REAL,
    taxes REAL,
    discount REAL,
    customs_fees REAL,
    currency TEXT CHECK(currency IN ('CAD', 'USD')),  -- Constraint for currency
    purchase_status TEXT CHECK(purchase_status IN ('Pending', 'Shipped', 'Delivered')),
    payment_method TEXT,
    shipping_cost REAL,
    shipping_date DATE,
    reference TEXT,
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
