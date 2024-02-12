s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"

num_vowels = 0
a = s.split()
vowels = ['a','e','i','o','u']

for x in s:
    if x in vowels:
        num_vowels +=1

print(num_vowels)

