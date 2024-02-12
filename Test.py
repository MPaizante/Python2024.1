words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for list in words:
    if len(list) > 3:
        num_words += 1

print(num_words)