Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for i in Junior:
    credits += Junior[i]
print(credits)

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for i in str1:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)

s1 = "hello"
counts = {}
for i in s1:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
print(counts)


def total(x):
    tot = 0
    for i in x:
        tot += i
    return tot


def count(x):
    tot = len(x)
    return tot
