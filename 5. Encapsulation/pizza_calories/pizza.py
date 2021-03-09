class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping):
        '''
        add_topping(topping: Topping) - Adds a new topping to the dictionary.
        •	If there is no space left for a new topping, raise a ValueError: "Not enough space for another topping"
        •	If the topping is already in the dictionary, increase the value of its weight.
        '''
        if topping.weight + self.calculate_total_weight() > self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            return
        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        # returns the total weight of the pizza.
        return sum([topping for topping in self.toppings.values()]) + self.dough.weight
