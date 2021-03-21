class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.max_index = len(self.sequence) - 1
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration == self.number:
            raise StopIteration
        value = self.sequence[self.index]
        self.iteration += 1
        if self.index == self.max_index:
            self.index = 0
        else:
            self.index += 1

        return value


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
