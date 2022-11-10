numList=[]
sqrList=[]
r=int(input("enter number to calculate square"))
print("enter a number")
for num in range(0,r):
    inp=int(input())
   
    numList.append(inp)
for num in numList:
    sqrList.append(num**2)
print(sqrList)    
