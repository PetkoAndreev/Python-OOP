class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(name=self.name, people=self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

    def __str__(self):
        names = ", ".join(str(people) for people in self.people)
        return f"Group {self.name} with members {names}"


'''
Create a class called Person. 
Upon initialization it will receive a name (str) and a surname (str). 
Create another class called Group. 
Upon initialization it should receive a name (str) and people (list of Person instances). 
Implement the needed magic methods, so the test code below works
'''
p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
# print(p0)

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

# print(len(first_group))
# print(second_group)
# print(third_group[0])

for person in third_group:
    print(person)
