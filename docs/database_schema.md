Database schema design for a small business:

**Tables:**

1. **Products**
	* `id` (primary key, auto-increment): unique product ID
	* `name`: product name (e.g., "Pikachu Card", "Charizard Figure")
	* `description`: brief product description
	* `category`: product category (e.g., "Pokémon Cards", "Collectible Figures")
	* `subcategory`: product subcategory (e.g., "Base Set", "Expedition Base Set")
	* `cost price`: product purchase price
    *  `selling price`: product selling price

2. **Inventory**
	* `id` (primary key, auto-increment): unique inventory ID
	* `product_id` (foreign key referencing Products.id): associated product ID
	* `condition`: condition of the product (e.g., "New", "Used", "Near Mint")
	* `quantity`: current quantity in stock

3. **Orders**
	* `id` (primary key, auto-increment): unique order ID
    *   date: order date and time
    *   total: total cost of the order

4. **Sales**
    *   id (primary key, auto-increment): unique sale ID 
    *   date: sale date and time
    *   total: total revenue from the sale

5. **Sold Items**
    *   id (primary key, auto-increment): unique sold item ID 
    *   sale_id (foreign key referencing Sales.id): associated sale ID 
    *   inventory_id (foreign key referencing Inventory.id): associated inventory ID 
    *   quantity: quantity of the product sold

6. **Reports**
    *   id (primary key, auto-increment): unique report ID 
    *   date: report date and time
    *   sales_total: total sales revenue for the report period
    *   profit_total: total profit for the report period

The relationships between tables are as follows:
* A product can have multiple inventory entries (`Products -> Inventory`)
* An order can have multiple ordered items (`Orders -> Ordered Items`)
* A sale can have multiple sold items (`Sales -> Sold Items`)
* A sold item is linked to an inventory entry (`Sold Items -> Inventory`)
* Reports are standalone and don't have direct relationships with other tables
