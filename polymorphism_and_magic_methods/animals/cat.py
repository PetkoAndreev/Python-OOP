from animal import Animal


class Cat(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    @staticmethod
    def make_sound():
        return "Meow meow!"


'''
The Cat class should inherit and implement the Animal class. Her repr should return 
"This is {name}. {name} is a {age} year old {gender} {class}". 
The make_sound() method should return "Meow meow!"
'''
