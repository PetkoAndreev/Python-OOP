def read_next(*args):
    for el in args:
        for ch in el:
            yield ch

'''
Create a generator function called read_next() which should receive different number of arguments (all iterable). 
On each iteration it should return the next element from the current iterable, or the first element from the subsequent iterable.
'''

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
