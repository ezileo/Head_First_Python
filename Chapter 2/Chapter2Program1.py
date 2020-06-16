vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please enter a letter to find vowels in it: ")
found = []
for letter in word:
    # print(letter)
    # print(found)
    if letter in vowels:
        # print(letter)
        # print (found)
        if letter not in found:
            found.append(letter)
for vowel in found:
        print(vowel)
print(found)
print(len(found))
