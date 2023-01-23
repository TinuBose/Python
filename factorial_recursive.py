def factorial(n):
    if (n == 1):
        return n
    else:
        return n * factorial(n - 1)


limit = int(input("enter the limit : "))
print("factorial of ", limit, "is : ", factorial(limit))
