def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")


a = int(input("enter the number"))
print("factors of ", a, " are ", end=" "), factors(a)
