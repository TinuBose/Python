word = input("enter the word : ");
ord_list = []
ord_dict = {}
for alphabets in word:
    ord_list.append([alphabets, ord(alphabets)])

ord_dict.update(ord_list)
print(ord_dict)
