-- data/inv_schema.sql

-- Categories table
DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE
);

-- Unit Types table
DROP TABLE IF EXISTS unit_types;
CREATE TABLE unit_types (
    unit_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_type TEXT UNIQUE NOT NULL
);

-- Catalog table
DROP TABLE IF EXISTS catalog;
CREATE TABLE catalog (
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
    quantity INTEGER,
    unit_type_id INTEGER,
    discontinued BOOLEAN,
    FOREIGN KEY (unit_type_id) REFERENCES unit_types(unit_type_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)  
);