sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
x = sentence.split()
word_counts = {}
for i in x:
    if i not in word_counts:
        word_counts[i] = 0
    word_counts[i] += 1
print(word_counts)



stri = "what can I do"
char_d = {}
x = stri.split()
for i in x:
    for u in i:
        if u not in char_d:
            char_d[u] = 0
        char_d[u] += 1

print(char_d)
