class Sphere:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 4 * (3.14 * self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius
