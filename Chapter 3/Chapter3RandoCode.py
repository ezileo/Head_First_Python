dictionary1 = { 'Name': 'Ford Prefect',
                'Gender': 'Male',
                'Occupation': 'Researcher',
                'Home Planet': 'Betelguese Seven'

}
dictionary1['Age'] = 33
print(dictionary1)

print("=====================================")
print("===============Part 2===============")
print("=====================================")


vowels = set('aeiou')
word = input("Please enter a word to find vowels: ")
found = vowels.intersection(set(word))
print (found)
if found in vowels:
    print (found)
else:
        print("No Vowels in", word)