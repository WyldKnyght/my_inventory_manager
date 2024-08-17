class Product:
    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity
        self.category = category

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        # Additional business logic can be added here