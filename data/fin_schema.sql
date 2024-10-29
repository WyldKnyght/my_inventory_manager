-- data/finance_schema.sql

-- Chart of Accounts table
DROP TABLE IF EXISTS chart_of_accounts;
CREATE TABLE chart_of_accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT NOT NULL UNIQUE,
    account_type TEXT NOT NULL CHECK(account_type IN ('asset', 'liability', 'income', 'expense', 'equity')),
    description TEXT
);

-- Finance Categories table
DROP TABLE IF EXISTS finance_categories;
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    account_type TEXT NOT NULL CHECK(account_type IN ('income', 'expense'))
);

-- Transactions table
DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    account_id INTEGER NOT NULL,
    category_id INTEGER,
    sender_receiver TEXT,
    description TEXT,
    invoice_number TEXT,
    income REAL,
    expense REAL,
    FOREIGN KEY (account_id) REFERENCES chart_of_accounts(id),
    FOREIGN KEY (category_id) REFERENCES finance_categories(id)
);

-- Vendors table
DROP TABLE IF EXISTS vendors;
CREATE TABLE vendors (
    vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    primary_contact TEXT,
    email TEXT,
    phone TEXT,
    website TEXT
);

-- Purchases table
DROP TABLE IF EXISTS purchases;
CREATE TABLE purchases (
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

-- Product Purchases table
DROP TABLE IF EXISTS product_purchases;
CREATE TABLE product_purchases (
    product_purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY (purchase_id) REFERENCES purchases(purchase_id)
);

-- Balanace Sheet table
DROP TABLE IF EXISTS balance_sheet;
CREATE VIEW balance_sheet AS
SELECT 
    t.id AS Trans_ID,
    t.date AS Date,
    coa.account_name AS Account,
    c.name AS Category,
    t.sender_receiver AS "Sender/Receiver",
    t.description AS Description,
    t.invoice_number AS "Invoice #",
    t.income AS Income,
    t.expense AS Expense,
    (SELECT SUM(COALESCE(income, 0) - COALESCE(expense, 0)) 
     FROM transactions 
     WHERE id <= t.id AND account_id = t.account_id) AS Balance
FROM 
    transactions t
LEFT JOIN 
    chart_of_accounts coa ON t.account_id = coa.id
LEFT JOIN 
    categories c ON t.category_id = c.id
ORDER BY 
    t.date, t.id;

-- Invoices table
DROP TABLE IF EXISTS invoices;
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT UNIQUE NOT NULL,
    date TEXT NOT NULL,
    due_date TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    total_amount REAL NOT NULL,
    status TEXT CHECK(status IN ('draft', 'sent', 'paid', 'overdue'))
);

-- Invoice_Items table
DROP TABLE IF EXISTS invoice_items;
CREATE TABLE invoice_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

-- Recurring_Transactions table
DROP TABLE IF EXISTS recurring_transactions;
CREATE TABLE recurring_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    category_id INTEGER,
    frequency TEXT CHECK(frequency IN ('daily', 'weekly', 'monthly', 'yearly')),
    start_date TEXT NOT NULL,
    end_date TEXT,
    last_occurrence TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Budgets table
DROP TABLE IF EXISTS budgets;
CREATE TABLE budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    period TEXT NOT NULL CHECK(period IN ('monthly', 'yearly')),
    start_date TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);


