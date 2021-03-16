import math


class Integer:
    ROMAN_NUMBERS = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000,
                     'IV': 4,
                     'IX': 9,
                     'XL': 40,
                     'XC': 90,
                     'CD': 400,
                     'CM': 900
                     }

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) != float:
            return 'value is not a float'
        return cls(math.floor(value))

    @classmethod
    def from_roman(cls, value):
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in cls.ROMAN_NUMBERS:
                num += cls.ROMAN_NUMBERS[value[i:i + 2]]
                i += 2
            else:
                num += cls.ROMAN_NUMBERS[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if type(value) != str:
            return 'wrong type'
        return cls(int(value))

    def add(self, integer):
        if type(integer) != Integer:
            return 'number should be an Integer instance'
        return self.value + integer.value


'''
Create a class called Integer. Upon initialization it should receive a single parameter value (int). It should have 4 methods:
•	from_float(value) - creates a new instance by flooring the provided floating number. 
    If the value is not a float return a message "value is not a float"
•	from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
•	from_string(value) - creates a new instance by converting the string to an integer 
    (if the value cannot be converted, return a message "wrong type")
•	add(integer:Integer) - adds the values of the two instances and returns the result 
    (if the integer is not an instance of Integer, return the message "number should be an Integer instance")
Output
value is not a float
wrong type
14
'''
first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
