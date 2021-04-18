from project.deliveries.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list = []

    def add(self, product: Product):
        if product in self.products:
            raise ValueError(f"Product {product.name} already exists.")
        self.products.append(product)
        return f"Product {product.name} successfully added to inventory."

    def decrease(self, product: Product, quantity: int):
        # if product not in self.products:
        #     return
        # if product.quantity >= quantity:
        # if product not in self.products:
        #     return
        for prd in self.products:
            if prd == product:
                prd.quantity -= quantity
                return f"Left quantity of {prd.name}: {prd.quantity}"

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        return "None"
