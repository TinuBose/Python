list=[]
n=int(input("enter size of list"))
print("enter", n ,"elements")

for i in range(0,n):
    e=int(input())
    list.append(e)
print("positive numbers in",list,"are:")
positive_num=[num for num in list if num>=0]
print(positive_num)
