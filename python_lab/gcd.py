n1=int(input("enter first number"))
n2=int(input("enter second number"))
list1=[]
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if(n1%i==0 and n2%j==0):
            if(i==j):
                list1.append(i)
print(list1)
gcd=max(list1)
print("gcd of ",n1," and ",n2," is ",gcd)