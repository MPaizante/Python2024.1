f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0
    if c in letter_counts:
        letter_counts[c] = letter_counts[c] +1

for i in letter_counts:
    print(f'{i}:{letter_counts[i]}')

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
x = sentence.split()
word_counts = {}
for i in x:
    if i not in word_counts:
        word_counts[i] = 0
    if i in word_counts:
        word_counts[i] = word_counts[i] +1


stri = "what can I do"
char_d = {}
for i in stri:
    if i not in char_d:
        char_d[i] = 1
    else:
        char_d[i] = char_d[i] +1

