x= {}

for i in range(10):

    c = input("Digite: ")
    if not c in x:
        x[c] = 1
    else:
        x[c] += x[c] +1


print(x)