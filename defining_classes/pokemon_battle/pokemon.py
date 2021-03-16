from trainer import Trainer


class Pokemon():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f'{self.name} with health {self.health}'


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())