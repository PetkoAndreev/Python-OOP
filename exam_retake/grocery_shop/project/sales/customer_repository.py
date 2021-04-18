from project.sales.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.customers: list = []

    def add(self, customer: Customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")
        self.customers.append(customer)

    def remove(self, customer_name: str):
        customer = self.find(customer_name)
        if customer == "None": # not in self.customers:
            raise ValueError(f"Customer {customer_name} does not exist.")
        self.customers.remove(customer)
        return f"Removed customer: {customer_name}"

    def find(self, customer_name: str):
        for customer in self.customers:
            if customer.name == customer_name:
                return customer
        return "None"
