nested1 = [['a','b','c'],['d','e'], ['f','g','h']]
for x in nested1:
    print(f'Level 1: {x}')
    for y in x:
        print(f'    Level 2: {y}')

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for i in info:
    last_names.append(i[1])
print(last_names)

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []
for i in L:
    for x in i:
        if 'b' in x or 'B' in x:
            b_strings.append(x)
print(b_strings)

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)


