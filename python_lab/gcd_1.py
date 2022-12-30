n1=int(input("enter first number"))
n2=int(input("enter second number"))
for i in range(1,max(n1,n2)):
    print(i)
    if(n1%i==0 and n2%i==0):
        gcd=i
print("gcd of ",n1," and ",n2," is ",gcd)