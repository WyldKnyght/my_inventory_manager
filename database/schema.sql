CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE
);

CREATE TABLE Vendors (
    vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    primary_contact TEXT,
    email TEXT,
    phone TEXT,
    website TEXT
);

CREATE TABLE Customers (
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

CREATE TABLE Settings (
    setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    default_dimension_unit TEXT CHECK(default_dimension_unit IN ('cm', 'in')),
    default_currency TEXT CHECK(default_currency IN ('CAD', 'USD'))
);

CREATE TABLE UnitTypes (
    unit_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_type TEXT UNIQUE NOT NULL
);

CREATE TABLE Catalog (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_number TEXT UNIQUE NOT NULL,
    item_name TEXT,
    product_description TEXT,
    upc TEXT UNIQUE,
    manufacturer TEXT,
    brand_name TEXT,  
    category_id INTEGER,
    theme TEXT,
    product_character TEXT,
    product_height REAL,
    product_width REAL,
    product_length REAL,
    product_size REAL,
    product_weight REAL,
    product_color TEXT,
    cost_price REAL,
    selling_price REAL,
    quantity INTEGER,
    unit_type_id INTEGER,
    discontinued BOOLEAN,
    FOREIGN KEY (unit_type_id) REFERENCES UnitTypes(unit_type_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)  
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
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Product_Sales (
    product_sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sales_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
    FOREIGN KEY (product_id) REFERENCES Catalog(item_id)  -- Updated foreign key reference
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
    currency TEXT CHECK(currency IN ('CAD', 'USD')),  
    purchase_status TEXT CHECK(purchase_status IN ('Pending', 'Shipped', 'Delivered')),
    payment_method TEXT,
    shipping_cost REAL,
    shipping_date DATE,
    reference TEXT,
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id)
);

CREATE TABLE Product_Purchases (
    product_purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (purchase_id) REFERENCES Purchases(purchase_id),
    FOREIGN KEY (product_id) REFERENCES Catalog(item_id)
);

CREATE TABLE Expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_date DATE,
    account_id INTEGER, 
    amount REAL,
    vendor_id INTEGER,
    notes TEXT,
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
