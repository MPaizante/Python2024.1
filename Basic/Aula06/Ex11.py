sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

# Create dictionary to track word occurrences
words = sent.split()
wrd_d = {}
for word in words:
    wrd_d[word] = wrd_d.get(word, 0) + 1

print("Dictionary wrd_d:", wrd_d)
