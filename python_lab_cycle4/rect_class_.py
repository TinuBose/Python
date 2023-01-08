class Rectangle:
    l = int(input("enter length"))
    b = int(input("enter breadth"))

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l * self.b)

    def display(self):
        print("area is ", self.area(), " perimeter is ", self.perimeter())

    @classmethod
    def change_values(cls):
        cls.l = int(input("enter length"))
        cls.b = int(input("enter breadth"))


x = Rectangle()
y = Rectangle()
print("###Rectangle 1###")
x.display()
print("###Rectangle 2###")
y.change_values()
y.display()
print("\nmax area is ", max(x.area(), y.area()))
