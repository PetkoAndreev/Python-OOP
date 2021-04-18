from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository


class Shop:
    def __init__(self):
        self.product_repository: ProductRepository = ProductRepository()
        self.customer_repository: CustomerRepository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        product = self.__get_product_type(product_type, name)
        if not product:
            return
        return self.product_repository.add(product)

    def sell(self, customer_name: str, **shopping_list):
        customer = self.customer_repository.find(customer_name)

        if customer == "None":
            customer = Customer(customer_name)
            self.customer_repository.add(customer)

        customer_index = self.customer_repository.customers.index(customer)

        bought_products_repr = []

        for product in shopping_list:
            quantity = shopping_list[product]
            prd_repo = self.product_repository.find(product)
            if prd_repo != "None":
                if quantity < prd_repo.quantity:
                    bought_products_repr.append(self.product_repository.decrease(prd_repo, quantity))
                else:
                    quantity = prd_repo.quantity
                    bought_products_repr.append(f"Left quantity of {prd_repo.name}: {0}")
                    self.product_repository.products.remove(prd_repo)
                if product in self.customer_repository.customers[customer_index].products:
                    self.customer_repository.customers[customer_index].products[product] += quantity
                self.customer_repository.customers[customer_index].products[product] = quantity
                # customer.products[product] = quantity
        if not bought_products_repr:
            return
        return "\n".join(bought_products_repr)

    @staticmethod
    def __get_product_type(product_type, name):
        if product_type == "Drink":
            return Drink(name)
        elif product_type == "Food":
            return Food(name)

# shop = Shop()
# print(shop.deliver("Food", "Snack"))
# print(shop.deliver("Drink", "Water"))
# prd_dict = {"Snack": 2, "Chips": 3}
# print(shop.sell("Pesho", **prd_dict))
# prd_dict = {"Snack": 20, "Chips": 3}
# print(shop.sell("Pesho", **prd_dict))
