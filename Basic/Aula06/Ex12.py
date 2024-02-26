sally = "sally sells sea shells by the sea shore"
characters = {}
best_char = ''
y = sally.split()
for x in y:
    for a in x:
        if a not in characters:
            characters[a] = 0

        characters[a] = characters[a] + 1

b = []
for x in characters:
    b.append(x)

b.sort()
print(b[-1])
