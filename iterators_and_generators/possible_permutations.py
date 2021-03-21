from itertools import permutations


def possible_permutations(sequence):
    for per in permutations(sequence):
        yield list(per)

'''
Create a generator function called possible_permutations() which should receive a list and return lists with all possible permutations between it's elements.
'''


[print(n) for n in possible_permutations([1, 2, 3])]