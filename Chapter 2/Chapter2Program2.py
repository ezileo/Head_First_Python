phrase = "Don't Panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.remove("'")
plist.remove("D")
print(plist)
for i in range(7):
    plist.pop()
    print(plist)
plist.insert(2, ' ')
plist.insert(4, 'a')
plist.insert(5, 'p')
print(plist)
new_phrase = "".join(plist)
print(plist)
print(new_phrase)
print()
print("==============================")
print("============Part 2============")
print("==============================")
print()
print()

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
print(plist)
for i in range(4):
    plist.pop()
    print("".join(plist))
plist.pop(0)
plist.remove("'")
print("".join(plist))
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
print(plist)
new_phrase = "".join(plist)
print(plist)
print(new_phrase)