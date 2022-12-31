lst = []
n = int(input("enter the size of the list"))
print("enter elements")
for i in range(n):
    a = int(input())
    lst.append(a)
print(lst)
print("sum = ", sum(lst))
