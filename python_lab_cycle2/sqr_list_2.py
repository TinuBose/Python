num_lst = [5555, 1024, 3600, 4444, 9801, 9000]
sqr_lst = []
for i in num_lst:
    for j in range(0, i):
        if j * j == i:
            sqr_lst.append(i)
print(sqr_lst)
