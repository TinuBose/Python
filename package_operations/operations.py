from graphics.addition import *
from graphics.subtraction import sub
from graphics.sub_graphics.multiplication import mul
from graphics.sub_graphics import division

print("....arithmetic operations....")
a, b = int(input("enter two numbers")), int(input())
choice = int(input("enter choice\n1.addition\n2.subtration\n3.multiplication\n4.division"))
if choice == 1:
    print("sum = ", add(a, b))
if choice == 2:
    print("differnce = ", sub(a, b))
if choice == 3:
    print("product = ", mul(a, b))
if choice == 4:
    print("quotient = ", division.div(a, b))
