from project.deliveries.product import Product


class Drink(Product):
    drink_quantity: int = 10

    def __init__(self, name: str):
        super().__init__(name, self.drink_quantity)
