def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    stripped_word = ''.join(char for char in word if char not in punctuation_chars)

    return stripped_word

example_word = "Hello, world! @example; #punctuation"
stripped_example_word = strip_punctuation(example_word)
print(stripped_example_word)
