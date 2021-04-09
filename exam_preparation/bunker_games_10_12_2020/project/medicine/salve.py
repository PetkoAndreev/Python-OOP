from project.medicine.medicine import Medicine


class Salve(Medicine):
    health = 50

    def __init__(self):
        super().__init__(self.health)
