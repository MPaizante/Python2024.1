Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for x in Junior:
    credits += Junior[x]

print(credits)


str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for a in str1:
    if a not in freq:
        # we have not seen this character before, so initialize a counter for it
        freq[a] = 0

        # whether we've seen it before or not, increment its counter
    freq[a] = freq[a] + 1