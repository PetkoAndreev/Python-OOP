class HashTable:
    '''
    Hashable reperesents a custom dictionary implementation
    where we use two private list to achieve storing and hashing
    of key-value pairs.
    '''

    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __getitem__(self, key):
        index = self.__keys.index(key)
        return self.__values[index]

    def __setitem__(self, key, value):
        # If we try to add key which already exists - change its value in the second list (values)
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        if self.actual_length == self.max_capacity:
            self.__resize()
        index = self.__hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __len__(self):
        return self.max_capacity

    def __repr__(self):
        result = [
        f"{self.__keys[index]}: {self.__values[index]}"
        for index in range(len(self.__keys))
        if self.__keys[index] is not None
        ]
        return "{" + "{}".format(", ".join(result)) + "}"

    @property
    def keys(self):
        return self.__keys

    @property
    def values(self):
        return self.__values

    @property
    def actual_length(self):
        return len(([el for el in self.__keys if el is not None]))

    def add(self, key, value):
        self[key] = value

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2


    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def __check_available_index(self, index):
        '''
        Checks if there is empty slot on this index,
        if not implement the linear approach when there is a
        collision between two hash indexes and returns the next available index
        :param index: int
        :return: int -> next current available index
        '''
        if index == len(self.__keys):
            return self.__check_available_index(0)
        # Linear approach implementation
        if self.__keys[index] is None:
            return index
        # Try next index
        return self.__check_available_index(index + 1)

    def __hash(self, key):
        index = sum([ord(ch) for ch in key]) % self.max_capacity
        available_index = self.__check_available_index(index)
        return available_index

# table = HashTable()

# print(table.keys)

# table["name"] = "Peter"
# table["age"] = 25  # Collision if we try it with max_capacity = 4
# table["age"] = 26
# table.add("work", "Some title")
# table["eyes color"] = "blue"
# table["eyes color2"] = "brown"
#
# print(table["name"])
# print(table["age"])
# print(table.get(5, "Not in dict"))
# print(len(table))
# print(table.actual_length)
# print(table)
