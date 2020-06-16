vowels = set('aeiou')
word = input("Please enter a word to find vowels: ")
found = vowels.intersection(set(word))
print (found)

for vowel in found:
    print(vowel)
    #print('The vowels in the word: ', word, 'are', vowel)
else:
    print("no vowel found in word: ", word)