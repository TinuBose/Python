integers=[1,2,3,4,5,6,7,8]
non_even=[]
for i in integers:
    if(i%2==0):
        integers.remove(i)
print(integers)

