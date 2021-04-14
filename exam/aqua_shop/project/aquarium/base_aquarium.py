from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    def capacity_left(self):
        return self.capacity - len(self.fish) > 0

    @property
    def total_price(self):
        result = sum(d.price for d in self.decorations)
        result += sum(f.price for f in self.fish)
        return result

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    @abstractmethod
    def add_fish(self, fish: BaseFish):
        if not self.capacity_left:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.species} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        result = f"{self.name}:\nFish: {' '.join(f.name for f in self.fish) if self.fish else 'none'}\n" \
                 f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}\n"

        return result
