# Open the file and read the content
with open('emotion_words.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Initialize a variable to store the total number of words
num_words = 0

# Loop through each line and count the words
for line in lines:
    # Split the line into words
    words = line.split()

    # Increment the total word count
    num_words += len(words)

# Print the total number of words
print("Total number of words:", num_words)
