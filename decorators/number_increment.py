def number_increment(numbers):

    def increase():
        return [s + 1 for s in numbers]

    return increase()


print(number_increment([1, 2, 3]))