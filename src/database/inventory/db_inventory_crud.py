# db_inventory_crud.py
from database.db_base_crud import BaseCRUD

class InventoryCRUD(BaseCRUD):
    def create_product(self, product_data):
        return self.execute_db_operation(self._create_product, product_data)

    def get_product(self, id):
        return self.execute_db_operation(self._get_product, id)

    def update_product(self, id, product_data):
        return self.execute_db_operation(self._update_product, id, product_data)

    def delete_product(self, id):
        return self.execute_db_operation(self._delete_product, id)

    def get_all_products(self):
        return self.execute_db_operation(self._get_all_products)

    @staticmethod
    def _create_product(conn, cursor, product_data):
        cursor.execute("""
            INSERT INTO Products (ProductName, ProductCode, Description, CategoryID, BrandID, Size, Color, Condition, 
                                  CostPrice, Markup, RetailPrice, ProductStatus, Notes, SupplierID, SinglesInStock, 
                                  CasesInStock, QtyPerCase)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (product_data['ProductName'], product_data['ProductCode'], product_data['Description'], 
              product_data['CategoryID'], product_data['BrandID'], product_data['Size'], product_data['Color'], 
              product_data['Condition'], product_data['CostPrice'], product_data['Markup'], product_data['RetailPrice'], 
              product_data['ProductStatus'], product_data['Notes'], product_data['SupplierID'], 
              product_data['SinglesInStock'], product_data['CasesInStock'], product_data['QtyPerCase']))
        return cursor.lastrowid

    @staticmethod
    def _get_product(conn, cursor, id):
        cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (id,))
        return cursor.fetchone()

    @staticmethod
    def _update_product(conn, cursor, id, product_data):
        cursor.execute("""
            UPDATE Products
            SET ProductName = ?, ProductCode = ?, Description = ?, CategoryID = ?, BrandID = ?, Size = ?, Color = ?, 
                Condition = ?, CostPrice = ?, Markup = ?, RetailPrice = ?, ProductStatus = ?, Notes = ?, SupplierID = ?, 
                SinglesInStock = ?, CasesInStock = ?, QtyPerCase = ?
            WHERE ProductID = ?
        """, (product_data['ProductName'], product_data['ProductCode'], product_data['Description'], 
              product_data['CategoryID'], product_data['BrandID'], product_data['Size'], product_data['Color'], 
              product_data['Condition'], product_data['CostPrice'], product_data['Markup'], product_data['RetailPrice'], 
              product_data['ProductStatus'], product_data['Notes'], product_data['SupplierID'], 
              product_data['SinglesInStock'], product_data['CasesInStock'], product_data['QtyPerCase'], id))

    @staticmethod
    def _delete_product(conn, cursor, id):
        cursor.execute("DELETE FROM Products WHERE ProductID = ?", (id,))

    @staticmethod
    def _get_all_products(conn, cursor):
        cursor.execute("SELECT * FROM Products")
        return cursor.fetchall()