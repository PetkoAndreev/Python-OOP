from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    health = 20

    def __init__(self):
        super().__init__(self.health)
