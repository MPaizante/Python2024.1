# Open the file and read the first 30 characters
with open('school_prompt.txt', 'r') as file:
    # Read the first 30 characters
    beginning_chars = file.read(30)

# Print the variable
print("First 30 characters:", beginning_chars)
