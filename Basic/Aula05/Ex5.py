# Initialize an empty list to store the third words
three = []

# Open the file and process each line
with open('school_prompt.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

    # Loop through each line
    for line in lines:
        # Split the line into words
        words = line.split()

        # Check if the line has at least three words
        if len(words) >= 3:
            # Append the third word to the 'three' list
            three.append(words[2])

# Print the list containing the third word of every line
print("List of third words:", three)
