from graphics.rectangle import *
from graphics.circle import *
from graphics.sub_graphics.cuboid import Cuboid
from graphics.sub_graphics.sphere import Sphere

print("### enter shape ###")
shape = int(input("1.rectangle\n2.circle\n3.cuboid\n4.sphere : "))
if (shape == 1):
    print("###Rectangle###")
    len = int(input("length = "))
    bre = int(input("breadth = "))
    a = Rectangle(len, bre)
    print("area = ", a.area())
    print("perimeter = ", a.perimeter())
elif (shape == 2):
    print("###circle###")
    radius = int(input("radius = "))
    a = Circle(radius)
    print("area = ", a.area())
    print("perimeter = ", a.perimeter())

elif (shape == 3):
    print("###cuboid###")
    len = int(input("length = "))
    bre = int(input("breadth = "))
    hei = int(input("height = "))
    a = Cuboid(len, bre, hei)
    print("area = ", a.area())
    print("perimeter = ", a.perimeter())

elif (shape == 4):
    print("###sphere###")
    radius = int(input("radius = "))
    a = Sphere(radius)
    print("area = ", a.area())
    print("perimeter = ", a.perimeter())
else:
    print("enter a valid option")
