class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

# Rectangle
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
print(a1 != a2)
print(a1 >= a3)
print(a1 <= a2)
print(a1 < a3)

class ImageAreaSquare:
    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.width

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()
# Square
a1 = ImageAreaSquare(7)
a2 = ImageAreaSquare(7)
a3 = ImageAreaSquare(8)
print(a1 == a2)
print(a1 != a3)
print(a1 != a2)
print(a1 >= a3)
print(a1 <= a2)
print(a1 < a3)
