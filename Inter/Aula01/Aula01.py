n = [['a','b','c'],['d','e','f'],['g','h','i']]
print(n[0].append(['z']))
print(n[1].append(['w']))
n.append(['j'])
print(n)
for i in n:
    print(i)

print([10,20,30][1])


animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
idx1 = animals[1][0]

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = data[7][0][0]
print(plant)