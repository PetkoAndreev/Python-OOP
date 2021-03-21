def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        take_list = []
        for num in seq:
            if len(take_list) == n:
                return take_list
            take_list.append(num)

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

'''
Implement the three generator functions:
•	integers() - generates an infinite amount of integers (starting from 1)
•	halves() - generates the halves of those integers (each integer / 2)
•	take(n, seq) - takes the first n halves of those integers
'''
