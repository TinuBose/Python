class Cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def area(self):
        return (2 * self.length * self.breadth) + (2 * self.length * self.height) + 2 * (self.height * self.breadth)

    def perimeter(self):
        return 4 * (self.length + self.breadth + self.height)
