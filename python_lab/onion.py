str="onion"
first=str[0]
word=first
for i in range(1,len(str)):
    if str[i]==first:
        word+="$"
    else:
        word+=str[i]
print(word)