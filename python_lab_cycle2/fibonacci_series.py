n = int(input("enter the limit"))
num1, num2, sum = 0, 1, 0

if n <= 0:
    print("enter a positive integer")
elif n == 1:
    print("fibanacci sequence up to ", n, " is ", num1)
else:
    for i in range(1, n + 1):
        print(num1)
        sum = num1 + num2
        num1 = num2
        num2 = sum
