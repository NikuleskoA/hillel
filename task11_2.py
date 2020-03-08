class Point:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"{self.__class__.__name__}{self.x, self.y, self.z}"

p1 = Point(2, 2, 1)
p2 = Point(2, 1, 1)
print(p1 + p2)


