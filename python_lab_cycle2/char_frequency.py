a = input("enter a string : ")
count = dict()
b = a.replace(" ", "")
print(b)
for i in b:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
