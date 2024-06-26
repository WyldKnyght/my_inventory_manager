-- Products table
CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(255) NOT NULL,
    subcategory VARCHAR(255) NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    selling_price DECIMAL(10, 2) NOT NULL
);

-- Orders table
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME NOT NULL,
    total DECIMAL(10, 2) NOT NULL
);

-- Sales table
CREATE TABLE Sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME NOT NULL,
    total DECIMAL(10, 2) NOT NULL
);

-- Inventory table
CREATE TABLE Inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

-- Sold_Items table
CREATE TABLE Sold_Items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT NOT NULL,
    inventory_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES Sales(id),
    FOREIGN KEY (inventory_id) REFERENCES Inventory(id)
);

-- Reports table
CREATE TABLE Reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME NOT NULL,
    sales_total DECIMAL(10, 2) NOT NULL,
    profit_total DECIMAL(10, 2) NOT NULL
);