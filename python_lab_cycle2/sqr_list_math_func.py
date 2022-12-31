import math

sqr_list = [5555, 1024, 3600, 4444, 9801, 9000]
sqr_list2 = []
for i in sqr_list:
    for j in range(0, i):
        a = math.sqrt(i)
        if a == j:
            sqr_list2.append(i)
print(sqr_list2)
