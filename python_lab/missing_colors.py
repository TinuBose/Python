list1=["red","green","blue","pink"]
list2=["red","blue","pink"]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)