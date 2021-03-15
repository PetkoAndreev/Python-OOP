from animal import Mammal
from food import *


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.get_weight_food_eaten(self.WEIGHT_INCREASE, food)


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.get_weight_food_eaten(self.WEIGHT_INCREASE, food)


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.get_weight_food_eaten(self.WEIGHT_INCREASE, food)


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.get_weight_food_eaten(self.WEIGHT_INCREASE, food)
