from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    ornament_comfort: int = 1
    ornament_price: float = 5

    def __init__(self):
        super().__init__(self.ornament_comfort, self.ornament_price)
