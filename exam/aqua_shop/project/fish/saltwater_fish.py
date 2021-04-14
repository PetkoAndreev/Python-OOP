from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    size_to_increase: int = 2
    salt_size: int = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.salt_size, price)

    def eat(self):
        super().eat()
