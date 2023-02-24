vowel_list = []
vowels = "aeiouAEIOU"
word = input("Enter the word")
for alphabets in word:
    if alphabets in vowels:
        vowel_list.append(alphabets)
print(vowel_list)
