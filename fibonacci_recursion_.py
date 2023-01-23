def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


limit = int(input("enter range : "))

if limit <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence up to ", limit, " is ", end=" ")
    for i in range(limit):
        print(fibonacci(i), end=" ")
