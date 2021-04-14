from project.aquarium.base_aquarium import BaseAquarium
from project.fish.base_fish import BaseFish


class SaltwaterAquarium(BaseAquarium):
    salt_capacity: int = 25

    def __init__(self, name: str):
        super().__init__(name, self.salt_capacity)

    def add_fish(self, fish: BaseFish):
        if fish.__class__.__name__ != "SaltwaterFish":
            return "Water not suitable."
        return super().add_fish(fish)
