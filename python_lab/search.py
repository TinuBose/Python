list=["amal","athira"]
count=0
for word in list:
    for letter in word:
        if(letter=="a"):
            count+=1
print(count)