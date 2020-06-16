nums = [1, 2, 3, 4, 5]
print(len(nums))
print(nums)

nums.remove(3)
print(len(nums))
print(nums)

nums.pop()
print(len(nums))
print(nums)


nums.extend(['a', 'b'])
print(len(nums))
print(nums)

nums.insert(0, 0)
print(len(nums))
print(nums)

nums.insert(4, 5)
print(len(nums))
print(nums)
print()
print("=========================================")
print("=========================================")

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
# for char in letters:
   # print ('\t', char)
for char in letters[:6]:
    print('\t'*2, char)
print()
for char in letters[-7:]:
    print('\t'*3, char)
print()
for char in letters[12:20]:
    print('\t'*4, char)
print()