from cat import Cat


class Kitten(Cat):
    gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.gender)

    @staticmethod
    def make_sound():
        return "Meow"


'''
The Kitten class should inherit and implement the Cat class. 
The kitten should not accept "gender" as a parameter, but it should have its value set to "Female".  
The make_sound() method should return "Meow".
'''
