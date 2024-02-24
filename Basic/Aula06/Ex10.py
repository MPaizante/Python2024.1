s1 = "hello"
counts = {}
for x in s1:
    if x not in counts:
        counts[x] = 0
    counts[x] = counts[x] + 1



str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
x = str1.split()
print(x)
for a in x:
    if a not in freq_words:
        freq_words[a] = 0
    freq_words[a] = freq_words[a] + 1

print(freq_words)