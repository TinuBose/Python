vowels=["a","e","i","o","u"]
word=input("enter a word")
vowellist=[]
for a in word:
    if a in vowels:
        vowellist.append(a)
print(vowellist)        
