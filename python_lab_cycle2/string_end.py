str1 = input("enter a string")
n = 3
if str1[-n:] == "ing":
    str2 = str1.replace("ing", "ly")
    print(str2)
else:
    print(str1 + "ing")
