words = []
n = int(input("enter the size of list"))
print("enter ", n, " words")
for i in range(n):
    a = input()
    words.append(a)
print("list is ", words)
d = max(words, key=len)
print("longest word is ", d, " length is ", len(d))
