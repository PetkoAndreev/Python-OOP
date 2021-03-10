import random


class RandomList(list):
    def get_random_element(self):
        # element_index = random.randint(0, len(self) - 1)
        element = random.choice(self)
        # self.pop(element_index)
        self.remove(element)
        return element


rl = RandomList([1, 2, 1, 3, 4, 5])
while rl:
    print(rl.get_random_element())
