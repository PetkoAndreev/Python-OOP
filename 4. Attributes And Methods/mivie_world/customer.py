class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        # count_dvd = len(self.rented_dvds)
        dvd_names = [dvd.name for dvd in self.rented_dvds]
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd_names)})"
# class Customer:
#
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.rented_dvds = []
#
#     def __repr__(self):
#         dvd_name_list = [dvd.name for dvd in self.rented_dvds]
#         return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd_name_list)})"