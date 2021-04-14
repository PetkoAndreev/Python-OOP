from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    plant_comfort: int = 5
    plant_price: float = 10

    def __init__(self):
        super().__init__(self.plant_comfort, self.plant_price)
