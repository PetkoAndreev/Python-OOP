from abc import ABC, abstractmethod


class Animal():
    pass


class SoundMakingAnimal(ABC, Animal):
    @abstractmethod
    def get_sound(self):
        pass


class Cat(SoundMakingAnimal):
    def get_sound(self):
        return 'meow'

    def get_eat(self):
        return 'Cat eat meat'


class Dog(SoundMakingAnimal):
    def get_sound(self):
        return 'woof-woof'

    def get_eat(self):
        return 'Dog eat meat'


class Dragon(SoundMakingAnimal):
    def get_sound(self):
        return 'rawr'

    def get_eat(self):
        return 'Dragon eat meat'


class Mole(Animal):
    def get_eat(self):
        return 'Mole eat worms'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


def animal_eat(animals: list[Animal]):
    for animal in animals:
        print(animal.get_eat())


animals = [Cat(), Dog(), Dragon()]
animal_sound(animals)
animal_eat(animals + [Mole()])
