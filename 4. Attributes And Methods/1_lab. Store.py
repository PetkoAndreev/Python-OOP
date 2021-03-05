class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.current_capacity = 0

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item):
        if self.capacity < self.current_capacity:
            return 'Not enough capacity in the store'
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        self.current_capacity += 1
        return f'{item} added to the store'

    def remove_item(self, item, amount):
        if item not in self.items or amount > self.items[item]:
            return f'Cannot remove {amount} {item}'
        self.current_capacity -= amount
        self.items[item] -= amount
        return f'{amount} {item} removed from the store'


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(first_store.remove_item("potato", 1))
print(second_store.remove_item("jeans", 1))
