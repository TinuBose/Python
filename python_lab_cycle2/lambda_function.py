sqr = lambda a: a * a
rect = lambda l, b: l * b
tri = lambda b, h: (1 / 2) * b * h
shape = input("enter shape : ")
if shape == "square":
    a = int(input("enter side : "))
    print("area is ", sqr(a))
elif shape == "rectangle":
    l, b = int(input("enter length and breadth : ")), int(input())
    print("area is ", rect(l, b))
elif shape == "triangle":
    h, b = int(input("enter height and breadth : ")), int(input())
    print("area is ", tri(b, h))
else:
    print("enter a valid choice")
