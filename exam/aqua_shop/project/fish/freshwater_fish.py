from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    size_to_increase: int = 3
    fresh_size: int = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.fresh_size, price)

    def eat(self):
        super().eat()
