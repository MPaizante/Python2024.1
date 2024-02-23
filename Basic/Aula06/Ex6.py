f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

for x in letter_counts.keys():
    print(f'{x} : {letter_counts[x]}')




txt_lines = f.readlines()
q = list(txt_lines)
for e in q:
    print(e)

# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))
