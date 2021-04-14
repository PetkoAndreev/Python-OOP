from project.aquarium.base_aquarium import BaseAquarium
from project.fish.base_fish import BaseFish


class FreshwaterAquarium(BaseAquarium):
    fresh_capacity: int = 50

    def __init__(self, name: str):
        super().__init__(name, self.fresh_capacity)

    def add_fish(self, fish: BaseFish):
        if fish.__class__.__name__ != "FreshwaterFish":
            return "Water not suitable."
        return super().add_fish(fish)
