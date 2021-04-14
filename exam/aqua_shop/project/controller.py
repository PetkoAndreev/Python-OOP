from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: list = []

    @staticmethod
    def __get_aquarium_type(aquarium_type):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium

        elif aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium

    @staticmethod
    def __get_decoration_type(decoration_type):
        if decoration_type == "Ornament":
            return Ornament

        elif decoration_type == "Plant":
            return Plant

    @staticmethod
    def __get_fish_type(fish_type):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish

        elif fish_type == "SaltwaterFish":
            return SaltwaterFish

    def __get_aquarium_by_name(self, name):
        return [a for a in self.aquariums if a.name == name][0]

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = self.__get_aquarium_type(aquarium_type)
        if not aquarium:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium(aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = self.__get_decoration_type(decoration_type)
        if not decoration:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        decoration = [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type]
        if not aquarium:
            return

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        decoration = decoration[0]

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = self.__get_fish_type(fish_type)
        aquarium = self.__get_aquarium_by_name(aquarium_name)

        if not fish:
            return f"There isn't a fish of type {fish_type}."

        if not aquarium:
            return

        return aquarium.add_fish(fish(fish_name, fish_species, price))

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        if not aquarium:
            return

        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        if not aquarium:
            return
        aquarium_value = aquarium.total_price
        return f"The value of Aquarium {aquarium_name} is {aquarium_value:.2f}."

    def report(self):
        result = ""
        for a in self.aquariums:
            result += str(a)
        return result
