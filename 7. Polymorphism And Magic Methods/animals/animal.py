from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


'''
Your task is to create a class hierarchy like the described below. 
The Animal class (abstract) should take, as attributes, a name, an age and a gender. It should have 2 methods: repr() and make_sound().

Submit in judge a zip file named project, containing a separate file for each of the classes.
'''
