class Trainer:
    id_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        Trainer.id_counter += 1
        return Trainer.id_counter