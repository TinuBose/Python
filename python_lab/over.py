
n=int(input("enter anumber"))
list=[]
for i in range(n):
    x=int(input("enter element"))
    if x>100:
        list.append("over")
    else:
        list.append(x)
print(list)            