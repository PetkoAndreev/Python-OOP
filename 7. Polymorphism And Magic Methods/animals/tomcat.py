from cat import Cat


class Tomcat(Cat):
    gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.gender)

    @staticmethod
    def make_sound():
        return "Hiss"


'''
The Tomcat class should inherit and implement the Cat class. 
The tomcat should not accept "gender" as a parameter, but it should have its value set to "Male".  
The make_sound() method should return "Hiss".
'''
