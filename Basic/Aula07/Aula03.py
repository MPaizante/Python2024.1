def total(l):
    c = 0
    for x in l:
        c += x
    return c
x = total([5,6,7])
print(x)

def count(y):
    x = 0
    for i in y:
        x+=1
    return x

a = count([1, 5, 9, -2, 9, 23])

print(a)