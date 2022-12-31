n = int(input("enter pattern size"))
for i in range(0, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")
for i in reversed(range(0, n + 1)):
    for j in range(2, i + 1):
        print("*", end=" ")
    print("\n")
