from project.deliveries.product import Product


class Food(Product):
    food_quantity: int = 15

    def __init__(self, name: str):
        super().__init__(name, self.food_quantity)
